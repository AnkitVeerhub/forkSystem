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

## ⚙️ Getting Started

### 📦 Requirements

- Python 3.8+
- pip

### 📥 Installation

```bash
git clone https://github.com/AnkitVeerhub/forkSystem.git
cd forkSystem

🛠️ Set Up Virtual Environment

python -m venv venv
source venv/bin/activate 

📚 Install Dependencies

pip install -r requirements.txt

🚀 Run the App

uvicorn app.main:app --reload

For Local Test

Then open your browser:
👉 http://127.0.0.1:8000/docs – Interactive Swagger UI
👉 http://127.0.0.1:8000/redoc – Redoc API docs
---

🧪 Example Tasks
You can use the Swagger UI to:

POST /tasks: Create a task

GET /tasks: View all tasks

PATCH /tasks/{id}: Update name or status

DELETE /tasks/{id}: Delete a task

💾 Tech Stack
Python 🐍

FastAPI ⚡

SQLAlchemy 💻

SQLite 🗂️

# Deployed API

The backend service is deployed and available at the following URL:

[**Fork System Task Manager API**](https://forksystem-production.up.railway.app/)

You can access the API's Swagger UI documentation by navigating to:

[**Swagger UI**](https://forksystem-production.up.railway.app/docs)

Swagger / OpenAPI 📘

✅ Sample Endpoints
POST /tasks → Create a task

GET /tasks → List all tasks

PATCH /tasks/{id} → Update task

DELETE /tasks/{id} → Delete task

📌 Future Improvements
Add user authentication

Support PostgreSQL / MongoDB

Task deadlines and scheduling

🙌 Acknowledgment
Built with ❤️ to showcase backend architecture inspired by low-level systems programming (fork() logic).

📌 License
MIT License. See LICENSE file.

👨‍💻 Author
Ankit Kumar
## Connect with Me

- [GitHub](https://github.com/AnkitVeerhub)
- [LinkedIn](https://www.linkedin.com/in/ankit-codes/)
