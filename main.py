"""Minor Project 2 - Student Information System.

Author: Gurtejbir Singh
"""


def calculate_total(marks):
    """Return the total marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average marks."""
    return calculate_total(marks) / len(marks)


def is_pass(average_mark):
    """Return True if the student passed."""
    return average_mark >= 50


def get_age_category(age):
    """Return the age category for a student."""
    if age < 13:
        return "Child"
    if age <= 18:
        return "Teenager"
    return "Adult"


def is_prime(num):
    """Return True if num is prime."""
    if num <= 1:
        return False

    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False

    return True


def is_palindrome(s):
    """Return True if the text is a palindrome."""
    cleaned_text = s.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


def reverse_roll_number(roll_no):
    """Reverse a roll number using a while loop."""
    number = abs(roll_no)
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number = number // 10

    if roll_no < 0:
        return -reversed_number

    return reversed_number


def generate_fibonacci(count):
    """Return the first count Fibonacci numbers."""
    sequence = []
    first = 0
    second = 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


def primes_between_1_and_100():
    """Return all prime numbers between 1 and 100."""
    primes = []

    for number in range(1, 101):
        if is_prime(number):
            primes.append(number)

    return primes


def get_integer_input(prompt, minimum=None, maximum=None):
    """Ask for an integer until the user enters a valid value."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Value must be at most {maximum}.")
            continue

        return value


def input_student_details(student_number):
    """Read and return details for one student."""
    print(f"\nEnter details for student {student_number}")
    name = input("Name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Name: ").strip()

    roll_no = get_integer_input("Roll number: ")
    age = get_integer_input("Age: ", minimum=1)
    marks = []

    for subject_number in range(1, 6):
        mark = get_integer_input(
            f"Marks in subject {subject_number} (0-100): ",
            minimum=0,
            maximum=100,
        )
        marks.append(mark)

    return {
        "name": name,
        "roll_no": roll_no,
        "age": age,
        "marks": marks,
    }


def print_student_report(student):
    """Print a detailed report for one student."""
    name = student["name"]
    roll_no = student["roll_no"]
    age = student["age"]
    marks = student["marks"]
    total_marks = calculate_total(marks)
    average_marks = calculate_average(marks)
    pass_status = "Pass" if is_pass(average_marks) else "Fail"
    prime_status = "Prime" if is_prime(roll_no) else "Not Prime"
    palindrome_status = "Palindrome" if is_palindrome(name) else "Not Palindrome"
    reversed_roll_no = reverse_roll_number(roll_no)
    highest_mark = max(marks)
    lowest_mark = min(marks)

    print("\n----------------------------------------")
    print("Student Summary Report")
    print("----------------------------------------")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_no}")
    print(f"Age Category: {get_age_category(age)}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Pass/Fail Status: {pass_status}")
    print(f"Roll Number Prime Status: {prime_status}")
    print(f"Name Palindrome Status: {palindrome_status}")
    print(f"Reversed Roll Number: {reversed_roll_no}")
    print(f"Highest Mark: {highest_mark}")
    print(f"Lowest Mark: {lowest_mark}")


def main():
    """Run the student information program."""
    print("Minor Project 2 - Student Information System")
    print("Prepared by: Gurtejbir Singh")

    number_of_students = get_integer_input(
        "\nEnter number of students (minimum 3): ",
        minimum=3,
    )

    students = []

    for student_number in range(1, number_of_students + 1):
        student = input_student_details(student_number)
        students.append(student)

    print("\n========== Detailed Reports ==========")
    for student in students:
        print_student_report(student)

    fibonacci_sequence = generate_fibonacci(len(students))
    print("\nFibonacci sequence:")
    print(fibonacci_sequence)

    print("\nRoll numbers from 100 to 200 that are multiples of both 3 and 5:")
    for roll_no in range(100, 201):
        if roll_no % 3 == 0 and roll_no % 5 == 0:
            print(roll_no, end=" ")
    print()

    print("\nPrime numbers between 1 and 100:")
    print(primes_between_1_and_100())


if __name__ == "__main__":
    main()
