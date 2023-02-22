#
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии. >

number = int(input('Введите число: '))
degree = int(input('Видите степень числа: '))

def sumnumber(number, degree):
    summa = 1
    for i in range(1, degree + 1):
        summa *= number
    return summa

print(sumnumber(number, degree))
