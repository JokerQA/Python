import random

# 1.Написать скрипт который в создаст список целых чисел

lists = []

for item in range(70):
    lists.append(random.randint(0, 100))

print('lists_numbers = ', lists)

# 2.Написать скрипт который в создаст список целых чётных чисел.

lists_even = []

for item in range(70):
    even_count = random.randint(0, 1000)
    if even_count % 2 == 0:
        lists_even.append(even_count)

print('even_number = ', lists_even)

# 3.Написать скрипт который в создаст список целых нечётных чисел

lists_odd = []

for item in range(70):
    odd_count = random.randint(0, 1000)
    if not odd_count % 2 == 0:
        lists_odd.append(odd_count)

print('odd_number = ', lists_odd)
