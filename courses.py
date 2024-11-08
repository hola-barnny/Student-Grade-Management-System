# courses.py
def get_highest_score(students, course):
    """Return the student with the highest grade in a specific course."""
    highest_student = None
    highest_grade = -1
    for student, courses in students.items():
        grade = courses.get(course, -1)
        print(f"Checking grade for {student} in {course}: {grade}")
        if grade > highest_grade:
            highest_student = student
            highest_grade = grade
    return highest_student, highest_grade

def get_lowest_score(students, course):
    """Return the student with the lowest grade in a specific course."""
    lowest_student = None
    lowest_grade = 101
    for student, courses in students.items():
        grade = courses.get(course, 101)
        print(f"Checking grade for {student} in {course}: {grade}")
        if grade < lowest_grade:
            lowest_student = student
            lowest_grade = grade
    return lowest_student, lowest_grade


















































    # Check if we found any student with the given course
    if lowest_student is None:
        print(f"No grades found for the course: {course}")
        return None, None
    
    return lowest_student, lowest_grade

