from students import register_student, update_grade
from courses import get_highest_score, get_lowest_score
from grades import display_student_grades, display_all_courses_averages
from utils import display_welcome_message

# List of courses offered
courses = ["Gross Anatomy III", "Neuroanatomy", "Nutritional Biochemistry", "Practical in Biochemistry", 
           "General Pharmacology", "Neurophysiology I", "Special Senses", "Skin and Body Temperature Regulation", 
           "Research Methodology", "Laboratory Teaching", "Instrumentation"]

students = {}

def pre_register_students():
    """Pre-register the students and assign them grades."""
    student_data = {
        "Ayodele Awojobi": {"Gross Anatomy III": 85, "Neuroanatomy": 90, "Nutritional Biochemistry": 78, 
                           "Practical in Biochemistry": 88, "General Pharmacology": 92, "Neurophysiology I": 87, 
                           "Special Senses": 91, "Skin and Body Temperature Regulation": 84, 
                           "Research Methodology": 89, "Laboratory Teaching": 93, "Instrumentation": 95}, 
        "Lawrence Garuba": {course: 0 for course in courses},
        "Folashade Ogedengbe": {course: 0 for course in courses},
        "David Adio": {course: 0 for course in courses},
        "Akin Araba": {course: 0 for course in courses},
        "Cornelius Taiwo": {course: 0 for course in courses},
        "Chike Obi": {course: 0 for course in courses},
        "Taslim Olawale": {course: 0 for course in courses},
        "Folasade Ogunsola": {course: 0 for course in courses},
        "Oluwatoyin Ogundipe": {course: 0 for course in courses},
        "Rahmon Bello": {course: 0 for course in courses},
        "Babatunde Sofoluwe": {course: 0 for course in courses},
        "Tolu Odugbemi": {course: 0 for course in courses},
        "Oyewusi Obe": {course: 0 for course in courses},
        "Jelili Omotola": {course: 0 for course in courses}
    }
    
    # Register students with initial grades of 0 for each course
    for student_name, grades in student_data.items():
        students[student_name] = grades
    print("Students pre-registered successfully.")
    print(students)

def main():
    display_welcome_message()
    
    while True:
        print("\n1. Register Student")
        print("2. Update Grade")
        print("3. Display All Grades")
        print("4. Display Course Averages")
        print("5. Get Highest Score in a Course")
        print("6. Get Lowest Score in a Course")
        print("7. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            student_name = input("Enter student name: ")
            register_student(students, student_name, courses)
        
        elif choice == "2":
            student_name = input("Enter student name: ")
            if student_name not in students:
                print(f"Student '{student_name}' not found.")
                continue
            course = input("Enter course: ")
            if course not in courses:
                print(f"Course '{course}' is not recognized.")
                continue
            try:
                grade = float(input(f"Enter grade for {course}: "))
            except ValueError:
                print("Invalid input. Please enter a valid number for the grade.")
                continue
            update_grade(students, student_name, course, grade)
        
        elif choice == "3":
            display_student_grades(students)
        
        elif choice == "4":
            display_all_courses_averages(students, courses)
        
        elif choice == "5":
            course = input("Enter course to find highest score: ")
            student, grade = get_highest_score(students, course)
            print(f"The highest score in {course} is {grade} by {student}.")
        
        elif choice == "6":
            course = input("Enter course to find lowest score: ")
            student, grade = get_lowest_score(students, course)
            print(f"The lowest score in {course} is {grade} by {student}.")
        
        elif choice == "7":
            print("Exiting system...")
            break

if __name__ == "__main__":
    pre_register_students()
    main()
