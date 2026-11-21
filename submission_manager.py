from datetime import date

from config import (
    STUDENTS_FILE,
    ASSIGNMENTS_FILE,
    SUBMISSIONS_FILE
)

from storage import load_data, save_data
from utils import get_next_id, get_valid_date


def record_submission():
    students = load_data(STUDENTS_FILE)
    assignments = load_data(ASSIGNMENTS_FILE)
    submissions = load_data(SUBMISSIONS_FILE)

    if not students:
        print("Add students first.")
        return

    if not assignments:
        print("Create assignments first.")
        return

    print("\nSTUDENTS")

    for student in students:
        print(
            f"{student['id']}. "
            f"{student['name']} ({student['roll_number']})"
        )

    try:
        student_id = int(input("\nEnter student ID: "))
    except ValueError:
        print("Invalid student ID.")
        return

    student = next(
        (s for s in students if s["id"] == student_id),
        None
    )

    if not student:
        print("Student not found.")
        return

    print("\nASSIGNMENTS")

    for assignment in assignments:
        print(
            f"{assignment['id']}. "
            f"{assignment['title']} "
            f"({assignment['subject']})"
        )

    try:
        assignment_id = int(input("\nEnter assignment ID: "))
    except ValueError:
        print("Invalid assignment ID.")
        return

    assignment = next(
        (
            a for a in assignments
            if a["id"] == assignment_id
        ),
        None
    )

    if not assignment:
        print("Assignment not found.")
        return

    existing = next(
        (
            s for s in submissions
            if s["student_id"] == student_id
            and s["assignment_id"] == assignment_id
        ),
        None
    )

    if existing:
        print("This student has already submitted this assignment.")
        return

    submission_date = get_valid_date(
        "Enter submission date (YYYY-MM-DD): "
    )

    status = (
        "Late"
        if submission_date > assignment["deadline"]
        else "On Time"
    )

    submission = {
        "id": get_next_id(submissions),
        "student_id": student_id,
        "assignment_id": assignment_id,
        "submission_date": submission_date,
        "status": status
    }

    submissions.append(submission)
    save_data(SUBMISSIONS_FILE, submissions)

    print("Submission recorded successfully!")
    print(f"Student: {student['name']}")
    print(f"Assignment: {assignment['title']}")
    print(f"Status: {status}")


def update_submission():
    submissions = load_data(SUBMISSIONS_FILE)

    try:
        submission_id = int(
            input("Enter submission ID to update: ")
        )
    except ValueError:
        print("Invalid ID.")
        return

    submission = next(
        (
            s for s in submissions
            if s["id"] == submission_id
        ),
        None
    )

    if not submission:
        print("Submission not found.")
        return

    assignments = load_data(ASSIGNMENTS_FILE)

    assignment = next(
        (
            a for a in assignments
            if a["id"] == submission["assignment_id"]
        ),
        None
    )

    if not assignment:
        print("Related assignment not found.")
        return

    new_date = get_valid_date(
        "Enter corrected submission date (YYYY-MM-DD): "
    )

    submission["submission_date"] = new_date
    submission["status"] = (
        "Late"
        if new_date > assignment["deadline"]
        else "On Time"
    )

    save_data(SUBMISSIONS_FILE, submissions)

    print("Submission updated successfully!")
