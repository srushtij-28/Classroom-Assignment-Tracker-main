from config import STUDENTS_FILE, SUBMISSIONS_FILE
from storage import load_data, save_data
from utils import get_next_id, print_line


def add_student():
    students = load_data(STUDENTS_FILE)

    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()
    department = input("Enter department: ").strip()

    if not name or not roll_number or not department:
        print("All fields are required.")
        return

    if any(
        student["roll_number"].lower() == roll_number.lower()
        for student in students
    ):
        print("Roll number already exists.")
        return

    student = {
        "id": get_next_id(students),
        "name": name,
        "roll_number": roll_number,
        "department": department
    }

    students.append(student)
    save_data(STUDENTS_FILE, students)

    print("Student added successfully!")


def view_students():
    students = load_data(STUDENTS_FILE)

    print_line()
    print("STUDENT LIST")
    print_line()

    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Roll No: {student['roll_number']} | "
            f"Department: {student['department']}"
        )


def search_student():
    students = load_data(STUDENTS_FILE)

    keyword = input(
        "Enter student name or roll number: "
    ).strip().lower()

    if not keyword:
        print("Search value cannot be empty.")
        return

    results = [
        student for student in students
        if keyword in student["name"].lower()
        or keyword in student["roll_number"].lower()
    ]

    if not results:
        print("No matching student found.")
        return

    for student in results:
        print(
            f"{student['name']} | "
            f"Roll No: {student['roll_number']} | "
            f"Department: {student['department']}"
        )


def delete_student():
    students = load_data(STUDENTS_FILE)
    submissions = load_data(SUBMISSIONS_FILE)

    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    student = next(
        (s for s in students if s["id"] == student_id),
        None
    )

    if not student:
        print("Student not found.")
        return

    confirm = input(
        f"Delete {student['name']} and their submission records? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    students = [
        s for s in students if s["id"] != student_id
    ]

    submissions = [
        s for s in submissions
        if s["student_id"] != student_id
    ]

    save_data(STUDENTS_FILE, students)
    save_data(SUBMISSIONS_FILE, submissions)

    print("Student and related submission records deleted.")
