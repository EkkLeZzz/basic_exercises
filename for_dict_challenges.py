# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count=0
dict_stud={}
for name in students:
    if name['first_name'] not in dict_stud.keys():
        dict_stud[name['first_name']] = 0
    dict_stud[name['first_name']]+=1
    
print(dict_stud, '\n')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


dict_stud={}
for name in students1:
    if name['first_name'] not in dict_stud.keys():
        dict_stud[name['first_name']] = 0
    dict_stud[name['first_name']]+=1

print("Самое встречающееся имя среди учеников: ",max(dict_stud, key=dict_stud.get))
print('\n')





# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

dict_stud={}
for name in school_students[0]:
    if name['first_name'] not in dict_stud.keys():
        dict_stud[name['first_name']] = 0
    dict_stud[name['first_name']]+=1
print("Самое встречающееся имя среди учеников первого класса: ",max(dict_stud, key=dict_stud.get))
dict_stud={}

for name in school_students[1]:
    if name['first_name'] not in dict_stud.keys():
        dict_stud[name['first_name']] = 0
    dict_stud[name['first_name']]+=1
print("Самое встречающееся имя среди учеников второго класса: ",max(dict_stud, key=dict_stud.get))
dict_stud={}

for name in school_students[2]:
    if name['first_name'] not in dict_stud.keys():
        dict_stud[name['first_name']] = 0
    dict_stud[name['first_name']]+=1
print("Самое встречающееся имя среди учеников третьего класса: ",max(dict_stud, key=dict_stud.get))



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
dict_stud ={}

for name in school:
    girl = 0
    boys = 0
    for gender in name['students']:
        if is_male[gender['first_name']] == True:
            boys+=1
        else:
            girl+=1
    print(f"В классе {name['class']} девочки {girl}, мальчики {boys} ")
print(f'\n \n \n \n \n \n')




# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}



for name in school:
    girl = 0
    boys = 0
    for gender in name['students']:
        if is_male[gender['first_name']] == True:
            boys+=1
        else:
            girl+=1
    if boys > girl:
        
        print(f"Больше всего мальчиков в классе {name['class']}")
    else:
        print(f"Больше всего девочек в классе {name['class']}")
