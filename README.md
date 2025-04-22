# 🚀 Unix Fork-Inspired Task Manager (FastAPI)

This project is a backend task management API inspired by the behavior of the Unix `fork()` system call. It allows users to create, list, update, and delete tasks — each represented with a UUID, name, and status.

---

## 🧱 Features

- Create tasks with unique UUIDs
- List all tasks
- Update task name/status
- Delete tasks
- Swagger UI for testing
- SQLite for lightweight storage

---

## 📂 Project Structure
task-manager/ │ ├── app/ │ ├── init.py │ ├── main.py # FastAPI app with all endpoints │ ├── models.py # SQLAlchemy models │ ├── schemas.py # Pydantic schemas │ ├── database.py # DB engine and session │ ├── scripts/ │ └── view_tasks.py # Optional CLI script to view tasks from DB │ ├── requirements.txt ├── README.md └── .gitignore



---

## ⚙️ Installation & Running Locally

1. **Clone the repository**
```bash
git clone https://github.com/AnkitVeerhub/forkSysytem.git
cd forkSysytem

2. Create a virtual environment & install dependencies
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt

3. Run the server
uvicorn app.main:app --reload

4. Visit Swagger UI
http://127.0.0.1:8000/docs
