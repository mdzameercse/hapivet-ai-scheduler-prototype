# 🐾 HapiVet – AI Appointment Scheduler Prototype

## 1. Problem Statement
Currently, veterinary scheduling and task management are handled manually.  
This causes delays in urgent cases and inefficient workload distribution among doctors.  

Our solution automates the scheduling system using AI to categorize appointments as:
- **Normal (1–2 days)**
- **Urgent (2–4 hours)**
- **Very Urgent (Immediate, 0–1 hour)**

The chatbot automatically connects users with available doctors, reschedules rejected slots, and handles instant video (Normal) calls using Jitsi Meet API.
Output Preview

Normal Appointment: Schedules for next day

Urgent Appointment: Notifies doctor for 2–4 hours slot

Very Urgent Appointment: Generates instant Jitsi Meet call link
---

## 2. Tools & Technologies Used
| Component | Technology |
|------------|-------------|
| Backend | FastAPI (Python) |
| Frontend | HTML, JavaScript |
| Database | JSON File (prototype) |
| AI Scheduling | Rule-based (expandable to ML) |
| Video Calls | Jitsi Meet (Free API) |
| Hosting (optional) | Render / Azure Free Tier |
| Version Control | GitHub |

---

## 3. Code & Team Details
**Team Name:** Pulse  

**Repository:** [GitHub link to this repo]

---

## 4. How to Run Locally
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
