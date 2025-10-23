# 🐾 HapiVet – AI Appointment Scheduler Prototype

# 🧠 PROBLEM STATEMENT

Currently, the **veterinary scheduling and task management system** is handled **manually**.  
Doctors’ availability, appointment prioritization, and communication with clients are all managed by human staff, which often leads to:

- ⚠️ **Delays in attending urgent or emergency cases**
- ⚖️ **Uneven workload distribution among doctors**
- 💬 **Lack of real-time communication between clients and veterinarians**
- 🧾 **Manual errors in booking and follow-up tracking**

---

# 💡 PROPOSED AI-DRIVEN SOLUTION

We propose an **AI-enabled chatbot-based appointment scheduling system** that automates the entire workflow — especially focusing on **AI-assisted calling** and **immediate doctor connection** in critical cases.

The system categorizes consultations into three urgency levels and handles them intelligently:

---

## 🚨 1. VERY URGENT CASE (IMMEDIATE: 0–1 HOUR)

**Scenario:**  
The pet is in an emergency condition that needs immediate attention.

### 🧩 AI WORKFLOW:
1. The user opens the chatbot and selects **“Very Urgent.”**  
2. The **AI Scheduler** checks the **doctor dataset** to identify doctors who are **currently within their working hours** and **free** (not consulting another case).  
3. The system immediately initiates a **call connection** (via a free service such as **Jitsi Meet**).  
4. The bot says:  
   > “Connecting you with the nearest available veterinarian for emergency support.”  
5. If the first doctor **doesn’t respond within 30 seconds**, the AI automatically tries the **next available doctor**.  
6. This loop continues until a doctor **accepts the call**.  
7. Once connected, both doctor and user receive **instant call links and notifications**.

**🎯 KEY GOAL:**  
👉 Minimize response time to **seconds** and **save lives during emergencies**.

---

## ⚡ 2. URGENT CASE (2–4 HOURS WINDOW)

**Scenario:**  
The pet needs quick medical attention, but not an immediate emergency.

### 🧩 AI WORKFLOW:
1. User selects **“Urgent Appointment.”**  
2. The **AI Scheduler** checks for doctors with **available slots** in the next **2–4 hours**.  
3. The system sends **notification requests** to available doctors, showing the proposed time.  
4. If the first doctor **accepts**, the appointment is **confirmed** and updated in the system.  
5. If the doctor **rejects** (busy or unavailable), the AI automatically forwards the request to the **next available doctor**.  
6. If all doctors are busy, the AI **adjusts the time slot** and retries automatically.

**🎯 KEY GOAL:**  
👉 Ensure that **urgent cases** are **scheduled within the same day** without manual coordination.

---

## 🕐 3. NORMAL CASE (1–2 DAYS)

**Scenario:**  
Routine check-ups, vaccinations, or follow-up visits.

### 🧩 AI WORKFLOW:
1. User selects **“Normal Appointment.”**  
2. The AI Scheduler allocates a slot **1–2 days later** based on the doctor’s normal working schedule.  
3. The appointment is automatically visible in the **doctor’s dashboard**.  
4. A day before, the doctor can **accept** or **reject** any slot.  
5. If a doctor **rejects**, the AI reassigns the booking to another available doctor.  
6. The user gets a **reschedule notification automatically** — no manual calls needed.

**🎯 KEY GOAL:**  
👉 Automate regular appointments efficiently and **reduce administrative workload**.

---

# 🤖 CHATBOT AS CENTRAL INTERFACE

The **chatbot** acts as the **main entry point** for all users.  
It doesn’t require typing — only **button-based selections** for simplicity:

- 🐾 **Normal Appointment**
- ⚡ **Urgent Appointment**
- 🚨 **Very Urgent (Call Now)**

The bot communicates with the **AI Scheduler backend**, checks doctor availability, and returns:

- ✅ **Confirmation messages**  
- 📞 **Call links (for Very Urgent)**  
- 🔔 **Notifications (for Urgent)**  
- 🔁 **Reschedule alerts (for Normal)**
---

# 🖥️ OUTPUT PREVIEW

| **Appointment Type** | **Action Performed by System** |
|-----------------------|--------------------------------|
| 🐾 **Normal Appointment** | Schedules for next day (visible to doctor in dashboard) |
| ⚡ **Urgent Appointment** | Notifies available doctor for 2–4 hours slot |
| 🚨 **Very Urgent Appointment** | Generates instant **Jitsi Meet call link** and connects doctor immediately |

---
## 🧭 AI APPOINTMENT SCHEDULING & CALLING WORKFLOW

```mermaid



## 🧩 Technologies Proposed

| **Function** | **Suggested Technology** | **Free / Integration** |
|---------------|---------------------------|-------------------------|
| 💬 Chatbot Interface | Botpress / Rasa / Microsoft Bot Framework | Free tier |
| 🧠 Scheduling Logic | Python (FastAPI backend) | Open source |
| 🗄️ Database | Firebase / MongoDB Atlas | Free tier |
| 📞 Calling & Video Consult | Jitsi Meet API | Free & instant |
| 🔔 Notifications | Firebase Cloud Messaging / Email | Free tier |
| ☁️ Hosting | Render / Azure Free Tier | Free deployment |

🎯 Key Benefits

✅ Zero manual scheduling — completely automated workflow.
✅ Real-time doctor availability tracking.
✅ Emergency “call now” feature through AI-driven routing.
✅ Efficient use of doctors’ working hours.
✅ Scalable and modular for future AI learning (predictive load balancing).

---

## 3. Code & Team Details
**Team Name:** Pulse  

**Repository:** https://github.com/mdzameercse/hapivet-ai-scheduler-prototype

---

## 4. How to Run Locally
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000

## 📸 VISUAL PREVIEW

Here are sample screenshots from the prototype demonstrating the AI Chatbot and Scheduling system:

1. 🗨️ Chatbot conversation interface  
2. ⚡ Urgent scheduling notification  
3. 📞 Very urgent case call popup  
## 🖼️ PROJECT SCREENSHOTS

### Chatbot Interface
![Chatbot UI](screenshots/chatbot_ui.png)

### Urgent Scheduling Flow
![Urgent Flow](screenshots/urgent_flow.png)

### Doctor Dashboard View
![Doctor Dashboard](screenshots/normal_schedule.png)

