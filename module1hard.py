grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(list(students))
aver_n = []
for i in grades:
    aver = sum(i) / len(i)
    aver_n.append(aver)
book = {students_sort[0]: aver_n[0], students_sort[1]: aver_n[1], students_sort[2]: aver_n[2], students_sort[3]: aver_n[3], students_sort[4]: aver_n[4]}
print(book)
