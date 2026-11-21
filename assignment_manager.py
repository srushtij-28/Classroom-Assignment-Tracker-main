from config import ASSIGNMENTS_FILE
from storage import load_data, save_data
from utils import get_next_id, get_valid_date, print_line


def add_assignment():
    assignments = load_data(ASSIGNMENTS_FILE)

    title = input("Enter assignment title: ").strip()
    subject = input("Enter subject name: ").strip()
    description = input("Enter assignment description: ").strip()

    if not title or not subject:
        print("Title and subject are required.")
        return

    deadline = get_valid_date(
        "Enter submission deadline (YYYY-MM-DD): "
    )

    assignment = {
        "id": get_next_id(assignments),
        "title": title,
        "subject": subject,
        "description": description,
        "deadline": deadline
    }

    assignments.append(assignment)
    save_data(ASSIGNMENTS_FILE, assignments)

    print("Assignment created successfully!")


def view_assignments():
    assignments = load_data(ASSIGNMENTS_FILE)

    print_line()
    print("ASSIGNMENT LIST")
    print_line()

    if not assignments:
        print("No assignments available.")
        return

    for assignment in assignments:
        print(f"ID: {assignment['id']}")
        print(f"Title: {assignment['title']}")
        print(f"Subject: {assignment['subject']}")
        print(f"Description: {assignment['description']}")
        print(f"Deadline: {assignment['deadline']}")
        print_line()


def delete_assignment():
    assignments = load_data(ASSIGNMENTS_FILE)

    try:
        assignment_id = int(
            input("Enter assignment ID to delete: ")
        )
    except ValueError:
        print("Invalid ID.")
        return

    assignment = next(
        (a for a in assignments if a["id"] == assignment_id),
        None
    )

    if not assignment:
        print("Assignment not found.")
        return

    confirm = input(
        f"Delete '{assignment['title']}'? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    assignments = [
        a for a in assignments
        if a["id"] != assignment_id
    ]

    save_data(ASSIGNMENTS_FILE, assignments)

    print("Assignment deleted successfully!")
