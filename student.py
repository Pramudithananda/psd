class Student:
    def __init__(self, name, grade, class_name):
        self.name = name
        self.grade = grade
        self.class_name = class_name
        self.marks = {'Maths': [[], [], []], 'Science': [[], [], []], 'Art': [[], [], []]}

    def add_marks(self, subject, term, marks):
        if subject in self.marks and 1 <= term <= 3:
            self.marks[subject][term-1].append(marks)
        else:
            print('Invalid subject or term.')

    def get_marks(self, subject, term):
        if subject in self.marks and 1 <= term <= 3:
            return self.marks[subject][term-1]
        else:
            print('Invalid subject or term.')

    def calculate_average_marks(self, subject, term):
        marks = self.get_marks(subject, term)
        if marks:
            return sum(marks) / len(marks)
        else:
            return None

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Class: {self.class_name}")
        print("Marks:")
        for subject, term_marks in self.marks.items():
            print(f"Subject: {subject}")
            for term, marks in enumerate(term_marks, start=1):
                print(f"  Term {term}: {marks}")


def find_max_average(students, subject, term):
    max_average = -1
    top_student = None
    for student in students:
        average = student.calculate_average_marks(subject, term)
        if average is not None and average > max_average:
            max_average = average
            top_student = student
    if top_student:
        print(f"The student with the highest average marks for {subject} in Term {term} is {top_student.name}")
        print(f"Average marks: {max_average}")
    else:
        print(f"No student has marks for {subject} in Term {term}")


def find_lowest_science_marks(students):
    lowest_marks = float('inf')
    lowest_student = None
    for student in students:
        marks = student.get_marks('Science', 1) + student.get_marks('Science', 2) + student.get_marks('Science', 3)
        if marks and min(marks) < lowest_marks:
            lowest_marks = min(marks)
            lowest_student = student
    if lowest_student:
        print(f"The student with the lowest marks in Science is {lowest_student.name}")
        print(f"Lowest marks: {lowest_marks}")
    else:
        print("No student has marks for Science")


def insert_students():
    students = []
    while True:
        name = input("Enter student name (or 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        grade = int(input("Enter grade: "))
        class_name = input("Enter class: ")
        student = Student(name, grade, class_name)
        students.append(student)
        print("Student details added successfully!")
        print()
    return students
