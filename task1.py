# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

n = int(input("Введите число N: "))
if n < 1:
    print("Число должно быть больше нуля")
elif n == 1:
    fibonacciNums  = [0]
else:
    fibonacciNums  = [0, 1]
    fib1 = 0
    fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fibonacciNums.append(fib2)

if n > 0:
    my_file = open("FibonacciNumbers.txt", "w+")
    my_file.write(str(fibonacciNums))
    my_file.close()