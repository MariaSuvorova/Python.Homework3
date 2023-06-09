"""Требуется вычислить, сколько раз встречается некоторое число X 
в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках 
записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1 """
#  решение через цикл
# n = int(input("Введите размер массива:  "))
# numbers = list(input("Введите массив:  ").split())
# x = int(input("Что ищем?  "))
# counter = 0
# for i in range(n):
#     numbers[i] = int(numbers[i])
#     if numbers[i] == x:
#         counter += 1

# print(f"Число {x} встречается {counter} раз")

# решение через методы
n = int(input("Введите размер массива:  "))
numbers = list(input("Введите массив:  ").split())
x = input("Что ищем?  ")
counter = numbers.count(x)
print(f"Число {x} встречается {counter} раз")
