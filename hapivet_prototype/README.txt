HapiVet Prototype - Button-based Chatbot + Scheduler (Free)
-------------------------------------------------------------

Structure:
- backend/      -> FastAPI app and doctors.json
- frontend/     -> Simple static HTML chatbot UI

Run locally (Python 3.8+):
1. cd backend
2. pip install -r requirements.txt
3. uvicorn app:app --reload --host 0.0.0.0 --port 8000
4. Open browser at http://localhost:8000/

How it works:
- Frontend shows three buttons: Normal, Urgent, Very Urgent
- Clicking a button sends a POST /schedule to the backend
- Backend reads doctors.json and returns either a scheduled time or a Jitsi call link
- For Very Urgent, a Jitsi Meet link is generated (opens in new tab)

Notes:
- This is a simple prototype for demo purposes. Doctor status is stored in doctors.json.
- For production: use a database, authentication, proper concurrency control, and real notification/call services.
