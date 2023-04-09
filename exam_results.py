num_students = int(input("Enter the number of students: "))

total_grade = 0
results = []
exam_results = []
students = []

for i in range(num_students):
    name = input("Enter student name: ")
    result = int(input("Enter student result: "))
    exam_results.append(result)
    students.append(name)
    
    if result >= 90:
        grade = 'A'
    elif result >= 80:
        grade = 'B'
    elif result >= 70:
        grade = 'C'
    elif result >= 60:
        grade = 'D'
    else:
        grade = 'F'
    total_grade += result
    results.append((name, result, grade))
    
    answer = input ('Are you sure continue Y/N : ')
    if answer.lower() == "n":
        break
average_grade = sum(exam_results) / len(students)

print("Results:")
for name, result, grade in results:
    print(f"{name}: Result = {result}, Grade = {grade}")
print(f"Average grade: {average_grade}")
