from datetime import date


def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def get_valid_date(message):
    while True:
        value = input(message).strip()

        try:
            return date.fromisoformat(value).isoformat()
        except ValueError:
            print("Enter date in YYYY-MM-DD format.")


def get_valid_integer(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Enter a number greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def print_line():
    print("-" * 60)
