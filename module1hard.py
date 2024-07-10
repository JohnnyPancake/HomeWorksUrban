grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
len_grades = len(grades)
len_students = len(students)
if len_grades == len_students:
    students = list(students)
    students.sort()
n = 0
dict_students = {}
while n < len_students:
    average = sum(grades[n]) / len(grades[n])
    dict_students[students[n]] = average
    n = n + 1
else:
    print('количество учеников и оценок не совпадает!')
print(dict_students)
