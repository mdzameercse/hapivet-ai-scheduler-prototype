# 🐾 HapiVet – AI Appointment Scheduler Prototype

🧠 Problem Statement

Currently, the veterinary scheduling and task management system is handled manually.
Doctors’ availability, appointment prioritization, and communication with clients are all managed by human staff, which often leads to:

Delays in attending urgent or emergency cases.

Uneven workload distribution among doctors.

Lack of real-time communication between clients and veterinarians.

Manual errors in booking and follow-up tracking.

💡 Proposed AI-Driven Solution

We propose an AI-enabled chatbot-based appointment scheduling system that automates the entire workflow — especially focusing on AI-assisted calling and immediate doctor connection in critical cases.

The system categorizes consultations into three urgency levels and handles them intelligently:

🚨 1. Very Urgent Case (Immediate: 0 – 1 hour)

Scenario: The pet is in an emergency condition that needs immediate attention.

AI Workflow:

The user opens the chatbot and selects “Very Urgent.”

The AI scheduler checks the doctor dataset to identify doctors who are currently within their working hours and free (not consulting another case).

The system immediately initiates a call connection (via a free service such as Jitsi Meet).

The bot says:

“Connecting you with the nearest available veterinarian for emergency support.”

If the first doctor doesn’t respond within 30 seconds, the AI automatically tries the next available doctor.

This loop continues until a doctor accepts the call.

Once connected, both doctor and user receive instant call links and notifications.

Key Goal:
Minimize response time to seconds and save lives during emergencies.

⚡ 2. Urgent Case (2 – 4 hours window)

Scenario: The pet needs quick medical attention, but not an immediate emergency.

AI Workflow:

User selects “Urgent Appointment.”

AI scheduler checks for doctors with available slots in the next 2–4 hours.

The system sends notification requests to available doctors, showing the proposed time.

If the first doctor accepts, the appointment is confirmed and updated in the system.

If the doctor rejects (busy or unavailable), the AI automatically forwards the request to the next available doctor.

If all doctors are busy, AI slightly adjusts the time slot and retries.

Key Goal:
Ensure that urgent cases are scheduled within the same day without manual coordination.

🕐 3. Normal Case (1 – 2 days)

Scenario: Routine check-ups, vaccinations, or follow-up visits.

AI Workflow:

User selects “Normal Appointment.”

AI scheduler allocates a slot 1–2 days later based on the doctor’s normal working schedule.

The appointment is automatically visible in the doctor’s dashboard.

A day before, the doctor can accept or reject any slot.

If a doctor rejects, the AI reassigns the booking to another doctor with availability.

User gets a reschedule notification automatically — no manual calls needed.

Key Goal:
Automate regular appointments efficiently and reduce administrative workload.

🤖 Chatbot as Central Interface

The chatbot acts as the main entry point for users.
It doesn’t require typing — only button-based selections for simplicity:

“Normal Appointment”

“Urgent Appointment”

“Very Urgent (Call Now)”

The bot communicates with the AI Scheduler backend, checks doctor availability, and returns:

Confirmation messages

Call links (for Very Urgent)

Notifications (for Urgent)

Reschedule alerts (for Normal)

🧩 Technologies Proposed
Function	Suggested Technology	Free / Integration
Chatbot Interface	Botpress / Rasa / Microsoft Bot Framework	Free tier
Scheduling Logic	Python (FastAPI backend)	Open source
Database	Firebase / MongoDB Atlas	Free tier
Calling & Video Consult	Jitsi Meet API	Free & instant
Notifications	Firebase Cloud Messaging / Email	Free tier
Hosting	Render / Azure Free Tier	Free deployment

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
