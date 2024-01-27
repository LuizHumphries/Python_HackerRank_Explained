if __name__ == '__main__':
    student_grade = [[input(), float(input())] for _ in range(int(input()))]
    student_grade = [x for x in student_grade if x[1] != min(student_grade, key=lambda x: x[1])[1]]
    student_grade = sorted([x[0] for x in student_grade if x[1] == min(student_grade, key=lambda x: x[1])[1]])
    print("\n".join(student_grade))
        