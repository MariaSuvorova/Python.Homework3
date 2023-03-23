'''Требуется найти в массиве A[1..N] самый близкий по величине 
элемент к заданному числу X. Пользователь в первой строке вводит 
натуральное число N – количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5 '''
from math import *
n = int(input("Введите размер массива:  "))
numbers = list(input("Введите массив:  ").split())
x = int(input("Что ищем?  "))

dif = abs(int(numbers[0])- x)
fnumber = int(numbers[0])
for i in range(n):
    numbers[i] = int(numbers[i])
    dif_temp = abs(numbers[i] - x)
    if  dif_temp < dif:
        dif = dif_temp
print(f"Самое близкое к {x} число: ", end="")

for i in range(n):    
    if abs(numbers[i] - x) == dif:
        print(numbers[i], end="  ")