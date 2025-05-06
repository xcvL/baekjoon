# 평균

n = int(input())
grade = input()
grade = list(map(int, grade.split(" ")))
maxgrade = max(grade)
mpt_grade = [i / maxgrade * 100 for i in grade]
print(sum(mpt_grade) / n)