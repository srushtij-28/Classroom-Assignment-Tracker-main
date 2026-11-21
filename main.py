from student_manager import (
    add_student,
    view_students,
    search_student,
    delete_student
)

from assignment_manager import (
    add_assignment,
    view_assignments,
    delete_assignment
)

from submission_manager import (
    record_submission,
    update_submission
)

from reports import (
    assignment_report,
    dashboard
)


def main():
    while True:
        print("\n======================================")
        print("      CLASSROOM ASSIGNMENT TRACKER")
        print("======================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Create Assignment")
        print("6. View Assignments")
        print("7. Delete Assignment")
        print("8. Record Submission")
        print("9. Update Submission")
        print("10. Assignment Report")
        print("11. View Dashboard")
        print("12. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            add_assignment()

        elif choice == "6":
            view_assignments()

        elif choice == "7":
            delete_assignment()

        elif choice == "8":
            record_submission()

        elif choice == "9":
            update_submission()

        elif choice == "10":
            assignment_report()

        elif choice == "11":
            dashboard()

        elif choice == "12":
            print("Thank you for using Classroom Assignment Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
