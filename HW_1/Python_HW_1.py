# создать переменную типа 'string' строка
name = 'Aleksey'
print('Name:', name)

# создать переменную типа 'int' целочисловое значение
salary = 1000
print('Salary:', salary)

# создать переменную типа 'float' число с плавающей запятой
temperature = 36.6
print(float, 'Temperature:', temperature)

# создать переменную типа 'bytes'
b_bytes = bytes(10)
print(b_bytes)

#создать переменную типа 'list' несколько элементов в одной переменной
numbers = [123, 345, 'Ivan', 'Vadim', '123']
numbers_list = list(numbers)
print('List:', numbers)

#создать переменную типа Tuple (Кортеж), используется для хранения нескольких элементов в одной переменной
users_list = ["Tom", "Bob", "Kate", 45, 36.66]
users_tuple = tuple(users_list)
print(users_tuple)

#создать переменную типа Set (неповторяемое множество)
thisset = {'apple', 'banana', 'orange', 'grape', 'apple', 'banana', 'apricot'}
print(thisset)
print(len(thisset))
thisset = set(('apple', 'banana', 'orange', 'grape', 'apple', 'banana', 'apricot'))
print(thisset)

#создать переменную типа FrozenSet, вид множеста, которое не может быть изменено
users = frozenset({"Tom", "Bob", "Alice"})
print(users)

#создать переменную типа Dict
mydict = {
  "brand": "Wolksvagen",
  "model": "Passat",
  "year": 2010
}

#вывести на консоль все вышеперечисленные переменные с добавлением типа данных
print(type(name))
print(type(salary))
print(type(temperature))
print(type(bytes))
print(type(numbers))
print(type(users_tuple))
print(type(thisset))
print(type(users))
print(type(mydict))

#создать 2 переменные String, создать переменную, в которой сканкатенируете эти переменные. Вывести в консоль
a = "Tom_Hanks"
b = "Julia_Roberts"
print(a + b)

#вывести в одну строку переменные типа String и Integer используя запятую
a = 'Ivanov'
b = 'Petrov'
age_Ivanov = 25
age_Petrov = 35
print(a, age_Ivanov, b, age_Petrov)

# вывести в одну строку переменные типа Str и Int, используя знак +
a = 'Olya(21) +'
b = 'Vasya(22)'
c = '= love'
print(a + b + c)