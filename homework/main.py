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

# 11.Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.

string_type_1 = 'firstStroke'
string_type_2 = 'secondStroke23'
string_type_3 = string_type_1 + string_type_2
print(string_type_3)

# 12.Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.

int_type1 = 345
int_type2 = 50
int_type3 = int_type1+int_type2
print(int_type3)

# 13. Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.

int_type_decide = int_type1/int_type2
print(int_type_decide)

# 14. Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.

int_type_multiplication = int_type1*int_type2
print(int_type_multiplication)

# 15. Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.

int_type_without = int_type1 // int_type2;
print(int_type_without)

# 16. Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль

int_type_mod = int_type1 % int_type2;

print(int_type_mod)

# 17.(7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.

print((7+12)**3+(7*4)-44/2**4)