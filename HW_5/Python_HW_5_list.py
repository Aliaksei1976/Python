#Python HW 5 Functions, Lists
# - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
# - Все результаты выводить в консоль.

#1)	Написать скрипт который создаст список целых чисел.
number_list = list(range(71))
print('number_list = ',number_list)

#2)	Написать скрипт который создаст список целых чётных чисел.
even_numbers_list = list(range(0,71,2))
print('even_numbers = ', even_numbers_list)

#3)	Написать скрипт который создаст список целых нечётных чисел.
number_list_odd = list(range(71))[1::2]
print('number_list_odd = ', number_list_odd)

#4)	Написать скрипт который из списка целых чисел выведет чётные числа.
even_list = [i for i in range(0,71) if i%2==0]
print('even_list = ', even_list)

#5)	Написать скрипт который из списка целых чисел выведет нечётные числа.
odd_list = [i for i in range(0,71) if i%2==1]
print('odd_list = ', odd_list)

#6)	Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
list_in_6 = [i for i in range(0,71) if i%5==0]
print('list_in_6 = ', list_in_6)

#7)	Написать скрипт который из списка целых чисел выведет количество чётных чисел которые делятся на 5 без остатка.
#Вывести количество цифр в списке
evens_digit_5 = sorted([e for e in list_in_6 if e % 5 ==0])
print('evens_digit_5 =', evens_digit_5)
evens_count_5 = len(evens_digit_5)
print('evens_count_5 = ', evens_count_5)

#8)	Написать скрипт который создаст список целых рандомных чисел.
import random
randomlist = random.sample(range(0, 120), 71)
print('random_list = ',randomlist)

#9)	Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
x = number_list
split_list = [ x [i:i + 5] for i in range(0, 71, 5) ]
print('split_list =', split_list)

#10)Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
def aleksey_list_1(number_list):
    even_list = [i for i in range(0,71) if i%2==0]
    odd_list = [list(range(71))[1::2]]
    print('even_list= ', even_list)
    print('odd_list = ', odd_list)
aleksey_list_1(number_list)


#11)	Написать скрипт который сгенерирует список под названием five_stars из списков по 5 элементов целых чисел.
stars_1 = list(range(0, 20, 4))
stars_2 = list(range(20, 40, 4))
stars_3 = list(range(40, 60, 4))
stars_all = [stars_1] + [stars_2] + [stars_3]
print('stars_all = ', stars_all)


# #12)Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars
sum_all = [sum(stars_1 + stars_2 + stars_3)]
print('sum_all = ', sum_all)
five_stars = [sum(stars_1)]+[sum(stars_2)]+[sum(stars_3)]
print('five_stars = ', five_stars)

# 13)	Написать функцию которая на вход получает список stars_all, а вернёт 2 списка.
# В одном списке внутренние списки из stars_all сумма чисел которых >= 100,
# а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”

total_sum_list_1 = sum(stars_all[0][0:5])
total_sum_list_2 = sum(stars_all[1][0:5])
total_sum_list_3 = sum(stars_all[2][0:5])
total_list = total_sum_list_1 + total_sum_list_2 + total_sum_list_3

if total_list >= 100:
    print('True:', total_list)
else:
    print('No_list')

# 14)	Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок
# вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
my_real_year_salary = 3000
salary_1 = 10000
salary_2 = 20000
salary_3 = 30000
salary_4= 50000
salary_5 = 100000
my_age = ''
my_age = input('Enter yor age: ')

if my_age == 'string':
    print()
def aleksey(my_age):
    result_1 = int(salary_1 / my_real_year_salary)
    result_2 = int(salary_2 / my_real_year_salary)
    result_3 = int(salary_3 / my_real_year_salary)
    result_4 = int(salary_4 / my_real_year_salary)
    result_5 = int(salary_5 / my_real_year_salary)
    print('Кубышка в сумме 10 тыс. через = ', result_1, 'года')
    print('===========================================')
    print('Кубышка в сумме 20 тыс. через = ', result_2, 'лет')
    print('===========================================')
    print('Кубышка в сумме 30 тыс. через = ', result_3, 'лет')
    print('===========================================')
    print('Кубышка в сумме 50 тыс. через = ', result_4, 'лет')
    print('===========================================')
    print('Кубышка в сумме 100 тыс. через = ', result_5, 'года')
    print('===========================================')
aleksey(45)

# 15)	Написать функцию которая получив на вход стартовую ЗП Junior QA и количество
# лет стажа выведет в консоль прогресс роста ЗП по каждому году из введенного количества
# лет стажа. Внутри функция учитывает дорожную карту развития скилов QA и список, полезных
# для компании, активностей которые может делать QA. Free implementation of function body logic
start_salary_qa = 1000
stage_years = 1

def progress_qa(start_salary_qa,stage_years):
    upper_salary = int(start_salary_qa * stage_years)
    print('upper_salary from years = ', upper_salary)
    progress_qasalary = [upper_salary for upper_salary in range(2000, 10000, 1500)]
    print('progress_qasalary_every_year =', progress_qasalary)

progress_qa(1500, 4)


# 16)	Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
import names

users_name = [names.get_full_name() for i in range(0, 5)]
print('user_name =', users_name)

# 17)	Написать скрипт который сгенерирует уникальных id).
# К каждому имени надо прикрепить номер итерации цикла как порядковый номер.
import uuid
count = 0
for i in range(5):
    filename = [uuid.uuid4()]
    count += 1
    print('filename_',count, filename)

# 18) Написать скрипт, который сгенерирует список списков. Каждый элемент списка это список,
# в котором 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.
import randomtimestamp as rd
from datetime import date, timedelta
import calendar
import string

full_list = [ [], [] ]

firstJan = date.today().replace(day=1, month=1)
randomDay = firstJan + timedelta(days = random.randint(0, 365 if calendar.isleap(firstJan.year) else 364))

full_list[0] = [names.get_full_name() for i in range(0, 5)]
full_list[1] = [randomDay for i in range(0, 5)]
print('full_list = ', full_list)

# 19)	Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации
# Employees = [[user_name_1], [login], [password], [E_mail], [reg_date]]

# Генератор пароля (без итерации)
def generator_pw():
    pwd = string.ascii_letters + string.digits + string.punctuation
    return ["".join(random.choice(pwd) for x in range(random.randint(6, 12)))]*5
print('generator_pw = ', generator_pw())

Employees = [[], [], [], [], []]

Employees[0] = [names.get_full_name() for i in range(0, 4)]
Employees[1] = ['ivanov', 'petrov', 'sidorov', 'ivanova', 'petrova']
Employees[2] = [generator_pw()]
Employees[3] = ['email_1','email_2','email_3','email_4','email_5']
Employees[4] = [randomDay for i in range(0, 5)]
print('Employees_List:', Employees)

# 20)	Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно)
# family = [  [], [], [[], []] ]

family = [  [], [], [ [], [] ] ]

family[0] = [names.get_last_name() for i in range(0, 4)]
family[1] = [names.get_full_name() for i in range(0, 5)]
family[2][0] = [random.choice([True, False]) for i in range(0, 5)]
print('family =', family)

# 21)	Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)
# gender_list = [ [0], [1], [ [2], [3] ]]
gender_list = [ [], [], [ [], [] ] ]
gender_list[0] = [names.__author__ for i in range(0, 4)]
gender_list[1] = [names.get_last_name() for i in range(0, 4)]
gender_list[2][0] = [names.get_full_name(gender='male') for i in range(0, 4)]
gender_list[2][1] = [names.get_full_name(gender='female') for i in range(0, 4)]
print('gender_list' ,gender_list)


# 22)	Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5200$)
salary = [ [], [], [] ]
salary[0] = [names.__title__ for i in range(0, 5)]
salary[1] = [names.get_first_name() for i in range(0, 5)]
salary[2] = [i for i in range(300, 5300, 1060)]
print('salary = ', salary)

# 23)	Написать скрипт который создаст список имён работников из salary, у которых ЗП от 1500$ до 3000$

names_salary = salary[1]
salary_of = salary[2]

for i in salary_of:
    if 1500 <= i <= 3000:
        print('salary_of =', [i] + [salary[1][2]])


# 24)	Написать скрипт который создаст список имён мужчин из gender.

print('men_list_from_genger = ', gender_list[2][0])

# 25)	Написать скрипт который создаст список имён женщин из gender.

print('women_list_from_genger = ', gender_list[2][1])

# 26)	Написать скрипт который создаст список имён неженатых мужчин из family.
# 27)	Написать скрипт который создаст список имён незамужних женщин из family.

not_maried_men = family
not_maried_women = family

if not_maried_men:
    not_maried_men = [names.get_last_name() for i in range(0, 4)]
    print('not_maried_men_list = ', not_maried_men)
    if not_maried_women:
        not_maried_women = [names.get_full_name(gender='female') for i in range(0, 4)]
        print('not_maried_women_list= ', not_maried_women)

# 28)	Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. реализуйте как
# функцию.

for i in not_maried_men:
    for x in salary_of:
        if x >= 1500:
            list_names = [i] + [x]
print('list_names = ', list_names)
