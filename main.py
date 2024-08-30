#                 0             1               2           3             4
from typing import Final

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]#list
# как упорядочить по Алфавиту Оо
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #set
Final={}
#Без функции sort не нашел как можно упорядочить
AStudents = list(students)
AStudents.sort()
print(AStudents)
#print(sum(grades[0])/len(grades[0])) Среднее значение
Averaga = (sum(grades[0])/len(grades[0])) , (sum(grades[1])/len(grades[1])) , (sum(grades[2])/len(grades[2])), (sum(grades[3])/len(grades[3])) , (sum(grades[4])/len(grades[4]))
print(Averaga)
#
Final.update({AStudents[0] : Averaga[0],AStudents[1] : Averaga[1],AStudents[2] : Averaga[2],AStudents[3] : Averaga[3],AStudents[4] : Averaga[4]})
print(Final)
#Если я не правильно сделал задание (оно скорее всего так и есть)
#прошу объяснить как можно было бы сделать иначе, или как можно дополнить\исправить