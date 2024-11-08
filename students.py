# students.py
def register_student(students, student_name, courses):
    """Register a new student and initialize grades."""
    students[student_name] = {course: 0 for course in courses}
    print(f"Student {student_name} registered successfully.")

def update_grade(students, student_name, course, grade):
    """Update the grade for a student in a specific course."""
    if student_name in students:
        if course in students[student_name]:
            students[student_name][course] = grade
            print(f"Grade for {student_name} in {course} updated to {grade}.")
        else:
            print(f"{course} not found for {student_name}.")
    else:
        print(f"Student {student_name} not found.")
