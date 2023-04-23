from datetime import datetime

def find_oldest_student(*students):
    """
    This function takes the name and birthday of several students and returns the name of the oldest student.

    Parameters:
    *students (tuple): Each tuple should contain the name and birthday of a student in the format ('name', 'YYYY-MM-DD').

    Returns:
    str: The name of the oldest student.
    """
    today = datetime.today()
    oldest_age = None
    oldest_student = None
    for student in students:
        name, birthday_str = student
        birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
        age = (today - birthday).days
        if oldest_age is None or age > oldest_age:
            oldest_age = age
            oldest_student = name
    return oldest_student
students = [
    ('Amila', '1999-01-01'),
    ('Banduls', '2000-02-02'),
    ('Chamila', '1998-03-03'),
]

oldest_student = find_oldest_student(*students)

print(f"The oldest student is {oldest_student}.")
