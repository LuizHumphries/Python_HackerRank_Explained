from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input())
print(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n)