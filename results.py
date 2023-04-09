# ask user for input for each subject score
subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5']
scores = []
for subject in subjects:
    while True:
        try:
            score = float(input(f'Enter score for {subject}: '))
            if score < 0 or score > 100:
                raise ValueError('Score must be between 0 and 100.')
            break
        except ValueError as e:
            print(e)
    scores.append(score)

# calculate overall percentage and letter grade
total = sum(scores)
percentage = total / len(scores)
if percentage >= 90:
    letter_grade = 'A'
elif percentage >= 80:
    letter_grade = 'B'
elif percentage >= 70:
    letter_grade = 'C'
elif percentage >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# print result
print(f'Total score: {total}')
print(f'Overall percentage: {percentage:.2f}%')
print(f'Overall grade: {letter_grade}')
