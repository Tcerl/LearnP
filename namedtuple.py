from collections import namedtuple

n = int(input())

columns = input().split()

students = namedtuple('Student', columns)

total_marks = 0

for _ in range(n):
    student = students(*input().split())
    total_marks += int(student.MARKS)

ending_test = total_marks / n

print(f"{ending_test:.2f}")