from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime, timedelta
import json, os, threading

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "doctors.json")
LOCK = threading.Lock()

app = FastAPI(title="HapiVet Prototype Scheduler")

# serve frontend static
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "..", "frontend")), name="static")

class ScheduleRequest(BaseModel):
    type: str  # normal | urgent | very_urgent
    pet_id: int = None
    user_id: int = None

def load_doctors():
    with LOCK:
        with open(DATA_FILE, "r") as f:
            return json.load(f)

def save_doctors(docs):
    with LOCK:
        with open(DATA_FILE, "w") as f:
            json.dump(docs, f, indent=2)

def now_time_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def parse_hours(h):
    start, end = h.split("-")
    return datetime.strptime(start, "%H:%M").time(), datetime.strptime(end, "%H:%M").time()

def is_within_working(wh):
    start, end = parse_hours(wh)
    t = datetime.now().time()
    return start <= t <= end

@app.get("/", response_class=HTMLResponse)
async def index():
    path = os.path.join(BASE_DIR, "..", "frontend", "index.html")
    return FileResponse(path)

@app.post("/schedule")
async def schedule(req: ScheduleRequest):
    appt_type = req.type
    doctors = load_doctors()

    # find doctors available now
    available_now = [d for d in doctors if d["status"] == "available" and is_within_working(d["working_hours"])]
    response = {"timestamp": now_time_str(), "type": appt_type}

    if appt_type == "very_urgent":
        # Try to connect immediately: return Jitsi link for first available doctor
        if not available_now:
            # try next doctors irrespective of status but within working hours
            fallback = [d for d in doctors if is_within_working(d["working_hours"])]
            if not fallback:
                response.update({"message": "No doctors are currently working. Please try again later."})
                return JSONResponse(response)
            doctor = fallback[0]
        else:
            doctor = available_now[0]

        # mark doctor busy
        doctor["status"] = "busy"
        save_doctors(doctors)

        room = f"hapivet-{doctor['name'].replace(' ', '')}-{int(datetime.now().timestamp())}"
        link = f"https://meet.jit.si/{room}"
        response.update({"message": f"Connecting you to {doctor['name']}. Click the link to join the immediate call.", "doctor": doctor["name"], "link": link})
        return JSONResponse(response)

    elif appt_type == "urgent":
        # schedule within 2-4 hours: pick an available doctor in upcoming hours
        # For prototype: choose first doctor who has working hours and mark a provisional slot 2 hours from now
        upcoming = []
        for d in doctors:
            if is_within_working(d["working_hours"]) or True:
                upcoming.append(d)
        if not upcoming:
            response.update({"message": "No doctors available for urgent scheduling."})
            return JSONResponse(response)
        doctor = upcoming[0]
        # propose time 2 hours from now
        proposed_time = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M")
        # mark provisional status
        doctor["status"] = "provisional"
        save_doctors(doctors)
        response.update({"message": f"Urgent appointment requested. Sending notification to {doctor['name']} for {proposed_time}.", "doctor": doctor["name"], "proposed_time": proposed_time})
        return JSONResponse(response)

    elif appt_type == "normal":
        # schedule for next day morning - pick any doctor with working hours
        doctor = None
        for d in doctors:
            # simple pick
            doctor = d
            break
        proposed_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 10:00")
        response.update({"message": f"Normal appointment scheduled with {doctor['name']} on {proposed_time}.", "doctor": doctor["name"], "proposed_time": proposed_time})
        return JSONResponse(response)

    else:
        raise HTTPException(status_code=400, detail="Invalid appointment type")
