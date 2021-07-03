number_of_students = int(input("Enter number of students: "))

students_marks = {}
for _ in range(number_of_students):
    name, *line = input().split()
    scores = list(map(float, line))
    students_marks[name] = scores
query_name = input()

from decimal import Decimal
query_score = students_marks[query_name]
total_score = sum(query_score)
avg = Decimal(total_score/3)
print(round(avg, 2))

