# grades.py
from prettytable import PrettyTable

def calculate_course_average(students, course):
    """Calculate and return the average grade for a course."""
    total = 0
    count = 0
    for student, courses in students.items():
        total += courses.get(course, 0)
        count += 1
    return total / count if count > 0 else 0

def display_student_grades(students):
    """Display all student grades in a neat table."""
    table = PrettyTable()
    table.field_names = ["Student Name", "Course", "Grade"]
    for student, courses in students.items():
        for course, grade in courses.items():
            table.add_row([student, course, grade])
    print(table)
    
# Example usage
if __name__ == "__main__":
    students = {
        "Banire Olaitan": {
            "Gross Anatomy III": 85, "Neuroanatomy": 90, "Nutritional Biochemistry": 78, 
            "Practical in Biochemistry": 88, "General Pharmacology": 92, "Neurophysiology I": 87, 
            "Special Senses": 91, "Skin and Body Temperature Regulation": 84, 
            "Research Methodology": 89, "Laboratory Teaching": 93, "Instrumentation": 95
        },
        "Korede Ayibowu": {
            "Gross Anatomy III": 76, "Neuroanatomy": 82, "Nutritional Biochemistry": 70, 
            "Practical in Biochemistry": 75, "General Pharmacology": 79, "Neurophysiology I": 80, 
            "Special Senses": 85, "Skin and Body Temperature Regulation": 78, 
            "Research Methodology": 81, "Laboratory Teaching": 84, "Instrumentation": 87
        }
    }

    # Call the function to display grades
    display_student_grades(students)

def display_all_courses_averages(students, courses):
    """Display average grade for each course."""
    for course in courses:
        average = calculate_course_average(students, course)
        print(f"Average grade for {course}: {average:.2f}")
