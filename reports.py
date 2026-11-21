from datetime import date

from config import (
    STUDENTS_FILE,
    ASSIGNMENTS_FILE,
    SUBMISSIONS_FILE
)

from storage import load_data
from utils import print_line


def assignment_report():
    assignments = load_data(ASSIGNMENTS_FILE)
    students = load_data(STUDENTS_FILE)
    submissions = load_data(SUBMISSIONS_FILE)

    if not assignments:
        print("No assignments available.")
        return

    print("\nAVAILABLE ASSIGNMENTS")

    for assignment in assignments:
        print(
            f"{assignment['id']}. "
            f"{assignment['title']}"
        )

    try:
        assignment_id = int(
            input("\nEnter assignment ID: ")
        )
    except ValueError:
        print("Invalid ID.")
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

    submitted_ids = {
        s["student_id"]
        for s in submissions
        if s["assignment_id"] == assignment_id
    }

    submitted = [
        s for s in students
        if s["id"] in submitted_ids
    ]

    pending = [
        s for s in students
        if s["id"] not in submitted_ids
    ]

    print_line()
    print(f"REPORT: {assignment['title']}")
    print_line()

    print(f"Total Students: {len(students)}")
    print(f"Submitted: {len(submitted)}")
    print(f"Pending: {len(pending)}")

    print("\nSUBMITTED STUDENTS")

    if submitted:
        for student in submitted:
            record = next(
                s for s in submissions
                if s["student_id"] == student["id"]
                and s["assignment_id"] == assignment_id
            )

            print(
                f"{student['name']} | "
                f"{student['roll_number']} | "
                f"{record['status']} | "
                f"{record['submission_date']}"
            )
    else:
        print("No submissions yet.")

    print("\nPENDING STUDENTS")

    if pending:
        for student in pending:
            print(
                f"{student['name']} | "
                f"{student['roll_number']}"
            )
    else:
        print("No pending submissions.")


def dashboard():
    students = load_data(STUDENTS_FILE)
    assignments = load_data(ASSIGNMENTS_FILE)
    submissions = load_data(SUBMISSIONS_FILE)

    total_expected = len(students) * len(assignments)

    submitted_count = len({
        (s["student_id"], s["assignment_id"])
        for s in submissions
        if any(st["id"] == s["student_id"] for st in students)
        and any(a["id"] == s["assignment_id"] for a in assignments)
    })

    pending_count = max(total_expected - submitted_count, 0)

    late_count = sum(
        1 for s in submissions
        if s["status"] == "Late"
    )

    today = date.today().isoformat()

    overdue_count = sum(
        1 for assignment in assignments
        if assignment["deadline"] < today
        and any(
            student["id"] not in {
                s["student_id"]
                for s in submissions
                if s["assignment_id"] == assignment["id"]
            }
            for student in students
        )
    )

    print_line()
    print("CLASSROOM DASHBOARD")
    print_line()

    print(f"Total Students: {len(students)}")
    print(f"Total Assignments: {len(assignments)}")
    print(f"Total Submissions: {submitted_count}")
    print(f"Pending Submissions: {pending_count}")
    print(f"Late Submissions: {late_count}")
    print(f"Overdue Assignments: {overdue_count}")
