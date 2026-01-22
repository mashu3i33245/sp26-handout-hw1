"""
Functions to ask the user questions to determine their housing priority.
"""


def ask_class_year() -> int:
    """Ask the student for their class year and return it as int."""
    while True:
        try:
            prompt = "Enter your class year (1=Freshman, 2=Sophomore, 3=Junior, 4=Senior): "
            year = int(input(prompt))
            if 1 <= year <= 4:
                return year
            print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


def ask_graduation_status() -> bool:
    """Ask if the student is graduating this semester."""
    while True:
        response = input("Are you graduating this semester? (y/n): ")
        if response in ['y', 'Y']:
            return True
        if response in ['n', 'N']:
            return False
        print("Invalid input. Please enter 'y' or 'n'.")


def ask_credits_earned() -> int:
    """Ask for credits earned and return as int."""
    while True:
        try:
            num_credits = int(input("How many credits have you earned? "))
            if num_credits >= 0:
                return num_credits
            print("Invalid input. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def ask_additional_questions() -> dict[str, bool]:
    """Ask at least two yes/no questions and return a dict of responses."""
    # Question 1: Are you older than 23?
    while True:
        response1 = input("Are you older than 23? (y/n): ")
        if response1 in ['y', 'Y']:
            old23 = True
            break
        if response1 in ['n', 'N']:
            old23 = False
            break
        print("Invalid input. Please enter 'y' or 'n'.")

    # Question 2: Are you in the honors program?
    while True:
        response2 = input("Are you in the honors program? (y/n): ")
        if response2 in ['y', 'Y']:
            honors = True
            break
        if response2 in ['n', 'N']:
            honors = False
            break
        print("Invalid input. Please enter 'y' or 'n'.")

    return {'old23': old23, 'honors': honors}
