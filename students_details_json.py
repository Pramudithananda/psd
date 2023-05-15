import json

class Student:
    def __init__(self, name, grade, class_, marks):
        self.name = name
        self.grade = grade
        self.class_ = class_
        self.marks = {
            'Term 1': {'Maths': marks[0][0], 'Science': marks[0][1], 'Art': marks[0][2]},
            'Term 2': {'Maths': marks[1][0], 'Science': marks[1][1], 'Art': marks[1][2]},
            'Term 3': {'Maths': marks[2][0], 'Science': marks[2][1], 'Art': marks[2][2]}
        }

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Class: {self.class_}")
        for term, subject_marks in self.marks.items():
            print(f"{term}:")
            for subject, marks in subject_marks.items():
                print(f"\t{subject}: {marks}")

    def get_average_marks(self, term):
        if term in self.marks:
            total_marks = sum(self.marks[term].values())
            return total_marks / len(self.marks[term])
        else:
            return None

    def get_lowest_science_marks(self):
        return min(self.marks.values(), key=lambda x: x['Science'])['Science']

def insert_student(students):
    name = input("Enter name: ")
    grade = input("Enter grade: ")
    class_ = input("Enter class: ")
    marks = []
    for i in range(3):
        term_marks = []
        for subject in ['Maths', 'Science', 'Art']:
            mark = int(input(f"Enter marks for {subject} in Term {i+1}: "))
            term_marks.append(mark)
        marks.append(term_marks)
    student = Student(name, grade, class_, marks)
    students.append(student)
    print("Student added successfully.")

def update_student_marks(students):
    name = input("Enter name: ")
    for student in students:
        if student.name == name:
            term = input("Enter term (Term 1 / Term 2 / Term 3): ")
            subject = input("Enter subject (Maths / Science / Art): ")
            marks = int(input("Enter marks: "))
            if term in student.marks and subject in student.marks[term]:
                student.marks[term][subject] = marks
                print("Marks updated successfully.")
            else:
                print("Invalid term or subject.")
            break
    else:
        print("Student not found.")

def find_student(students):
    name = input("Enter name: ")
    for student in students:
        if student.name == name:
            student.display_details()
            break
    else:
        print("Student not found.")

def get_maximum_average_marks(students, term):
    max_average_marks = 0
    max_average_marks_student = None
    for student in students:
        average_marks = student.get_average_marks(term)
        if average_marks and average_marks > max_average_marks:
            max_average_marks = average_marks
            max_average_marks_student = student
    return max_average_marks_student
def get_student_with_lowest_science_marks(students):
    lowest_science_marks = float('inf')
    lowest_science_marks_student = None
    for student in students:
        science_marks = student.get_lowest_science_marks()
        if science_marks and science_marks < lowest_science_marks:
            lowest_science_marks = science_marks
            lowest_science_marks_student = student
    return lowest_science_marks_student

def save_data_to_json(students):
    data = []
    for student in students:
        student_data = {
            'name': student.name,
            'grade': student.grade,
            'class': student.class_,
            'marks': student.marks
        }
        data.append(student_data)

    with open('students.json', 'w') as file:
        json.dump(data, file)

def load_data_from_json():
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
            students = []
            for student_data in data:
                name = student_data['name']
                grade = student_data['grade']
                class_ = student_data['class']
                marks = student_data['marks']
                student = Student(name, grade, class_, marks)
                students.append(student)
            return students
    except FileNotFoundError:
        return []

def main():
    students = load_data_from_json()
    while True:
        print("\nSelect an option:")
        print("1. Insert new student")
        print("2. Update student marks")
        print("3. Display student details")
        print("4. Find student with maximum average marks for a term")
        print("5. Find student with lowest marks for Science")
        print("6. Save data to JSON file")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")
        if choice == '1':
            insert_student(students)
        elif choice == '2':
            update_student_marks(students)
        elif choice == '3':
            find_student(students)
        elif choice == '4':
            term = input("Enter term (Term 1 / Term 2 / Term 3): ")
            student = get_maximum_average_marks(students, term)
            if student:
                print(f"{student.name} has the maximum average marks ({student.get_average_marks(term)}) in {term}.")
            else:
                print("No student found.")
        elif choice == '5':
            student = get_student_with_lowest_science_marks(students)
            if student:
                print(f"{student.name} has the lowest marks ({student.get_lowest_science_marks()}) in Science.")
            else:
                print("No student found.")
        elif choice == '6':
            save_data_to_json(students)
            print("Data saved to JSON file.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

