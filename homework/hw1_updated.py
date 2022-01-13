# 1.Создать переменную типа String

string_type = "I m string"

# 2.Создать переменную типа Integer

int_type = 23

# 3.Создать переменную типа Float

float_type = 23.23

# 4.Создать переменную типа Bytes

bytes_type = bytes(23)

# 5.Создать переменную типа List

lists_type = ["Boris", "Anna", "Sofia", "Vladislav", "Yaroslav", "Andrey"]

# 6.Создать переменную типа Tuple

tuple_type = ("IOS", "Android", "Windows")

# 7.Создать переменную типа Set

set_type = set(["banana", "apple", "banana", "apple", "tomato"])

# 8.Создать переменную типа Frozen set

frozenset_type = frozenset('zqw123qwdwqfqwgjjASADSD')

# 9.Создать переменную типа Dict

dict_type = {'firstName': "Vladislav", 'secondName': "Nikitin"}

# 10.Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

print(string_type, "=", type(string_type), "\n", int_type, "=", type(int_type), "\n", float_type, "=", type(float_type),
      "\n", bytes_type, "=", type(bytes_type), "\n", lists_type, "=", type(lists_type), "\n", tuple_type, "=",
      type(tuple_type),"\n",set_type,"=",type(set_type),"\n",frozenset_type,"=",type(frozenset_type),"\n",dict_type,"=",type(dict_type))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
name1 = "Vlad"
name2 = "Sonya"
result = name1+name2
print(result)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
str1 = "Stroka"
age = 25
print(str1,age)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс) строку и число нельзя складывать! можно преобразовать число в string, но тогда мы серовно складываем 2 стринга

str2 = "stroka2"
age = "10"
print(str2+age)