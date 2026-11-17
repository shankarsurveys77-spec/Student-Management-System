🎓 Student Management System

A web-based Student Management System built using Python, FastAPI, SQLite, HTML, and CSS. This application helps manage student records efficiently with features to add, view, update, and delete student information.

🚀 Features

- ➕ Add new student records
- 📋 View all registered students
- ✏️ Update student details
- 🗑️ Delete student records
- 🗄️ Store student information using SQLite
- 🎨 User-friendly interface
- ⚡ Fast and lightweight backend using FastAPI

🛠️ Technologies Used

Technology| Purpose
Python| Backend programming
FastAPI| Web framework
SQLite| Database
HTML| Page structure
CSS| Styling
Jinja2| HTML templating
Pydantic| Data validation

📂 Project Structure

Student-Management-System/
│
├── main.py
├── students.db
│
├── templates/
│   ├── add-student.html
│   ├── home.html
│   ├── single-std.html
│   └── update-student.html
│
├── README.md
└── .gitignore
⚙️ Installation and Setup

1. Clone the repository

git clone YOUR_REPOSITORY_URL

2. Navigate to the project folder

cd Student-Management-System

3. Install dependencies

pip install fastapi uvicorn jinja2 python-multipart

4. Run the application

uvicorn main:app --reload

5. Open in your browser

http://127.0.0.1:8000

📌 CRUD Operations

- Create: Add new student details.
- Read: Display student records.
- Update: Edit existing student information.
- Delete: Remove student records.

🎯 Project Objective

The main objective of this project is to understand Python backend development, database connectivity, RESTful web application concepts, and CRUD operations using FastAPI and SQLite.

👨‍💻 Author

Are Shankar

Python Full Stack Developer | Aspiring Software Developer
---

⭐ If you find this project useful, feel free to star the repository!
