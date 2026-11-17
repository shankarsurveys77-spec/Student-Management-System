from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
import sqlite3



class Student(BaseModel):
    name: str
    age: int = Field(ge=18, le=30)
    gender: str
    marks: int
    course: str
    image: str
    status: int



def get_connection():
    return sqlite3.connect("students.db")



def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    q = """
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        marks INTEGER,
        course TEXT,
        image TEXT,
        status INTEGER
    )
    """

    cursor.execute(q)
    connection.commit()
    connection.close()


create_table()


templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def home(req: Request):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"stds": students}
    )


@app.get("/students/add")
def send_std_form(req: Request):

    return templates.TemplateResponse(
        request=req,
        name="add-student.html",
        context={}
    )


@app.post("/students/add")
def create_std(
    name: str = Form(),
    age: int = Form(),
    gender: str = Form(),
    marks: int = Form(),
    course: str = Form(),
    image: str = Form(),
    status: int = Form()
):

    student = Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )

    values = (
        student.name,
        student.age,
        student.gender,
        student.marks,
        student.course,
        student.image,
        student.status
    )

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, age, gender, marks, course, image, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, values)

    connection.commit()
    connection.close()

    return RedirectResponse("/", status_code=303)


@app.get("/students/{std_id}")
def single_std(req: Request, std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (std_id,)
    )

    student = cursor.fetchone()
    connection.close()

    if student is None:
        return {"detail": "Student not found"}

    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={"std": student}
    )


@app.get("/students/update/{std_id}")
def update_student_form(req: Request, std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (std_id,)
    )

    student = cursor.fetchone()
    connection.close()

    if student is None:
        return {"detail": "Student not found"}

    return templates.TemplateResponse(
        request=req,
        name="update-student.html",
        context={"std": student}
    )


@app.post("/students/update/{std_id}")
def update_student(
    std_id: int,
    name: str = Form(),
    age: int = Form(),
    gender: str = Form(),
    marks: int = Form(),
    course: str = Form(),
    image: str = Form(),
    status: int = Form()
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET name=?, age=?, gender=?, marks=?,
            course=?, image=?, status=?
        WHERE id=?
    """, (name, age, gender, marks,course, image, status, std_id )
    )

    connection.commit()
    connection.close()

    return RedirectResponse("/", status_code=303)


@app.post("/students/delete/{std_id}")
def delete_student(std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (std_id,)
    )

    connection.commit()
    connection.close()

    return RedirectResponse("/", status_code=303)