
class Student:
    def __init__(self, name, age, student_id, grades):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = grades

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.student_id)
        print("Grades:", self.grades)
        print("-" * 20)

students = []

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    student_id = input("Enter student ID: ")
    grades = input("Enter grades (comma separated): ")
    student = Student(name, age, student_id, grades)
    students.append(student)
    print("Student added!\n")

def view_students():
    if len(students) == 0:
        print("No students to show.\n")
    else:
        for student in students:
            student.display()

def search_student():
    target_id = input("Enter student ID to search: ")
    found = False
    for student in students:
        if student.student_id == target_id:
            student.display()
            found = True
            break
    if not found:
        print("Student not found.\n")

def update_student():
    target_id = input("Enter student ID to update: ")
    for student in students:
        if student.student_id == target_id:
            print("Leave blank to keep current value.")
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            grades = input("Enter new grades (comma separated): ")

            if name != "":
                student.name = name
            if age != "":
                student.age = age
            if grades != "":
                student.grades = grades

            print("Student info updated!\n")
            return
    print("Student not found.\n")

def save_to_file():
    file = open("students.txt", "w")
    for student in students:
        line = student.name + ";" + student.age + ";" + student.student_id + ";" + student.grades + "\n"
        file.write(line)
    file.close()
    print("Data saved!\n")

def load_from_file():
    try:
        file = open("students.txt", "r")
        students.clear()
        for line in file:
            parts = line.strip().split(";")
            if len(parts) == 4:
                name, age, student_id, grades = parts
                student = Student(name, age, student_id, grades)
                students.append(student)
        file.close()
        print("Data loaded!\n")
    except:
        print("No file found.\n")

def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by ID")
        print("4. Update Student Info")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")
        choice = input("Enter choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            print("Exiting")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
