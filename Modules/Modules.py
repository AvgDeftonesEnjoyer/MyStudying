check = int(input("Choose homework : 1, 2, 3: "))

if check == 1: #Використовуй модуль math, щоб обчислити площу кола за заданим радіусом.
    import math

    r = float(input("Enter the radius of circle: "))

    print(f"The square of circle with radius {r} - {math.pi * math.pow(r, 2)}")
elif check == 2: #Реалізуй програму, яка використовує модуль random для генерації 10 випадкових чисел і знаходить середнє з них.

    import random
    import statistics

    nums = random.sample(range(1, 100), 10)

    print(f'Generated nums are - {nums}')

    median_values = statistics.median(nums)

    print(f"The average num is - {median_values}")

elif check == 3: #Створи власний модуль, який містить функцію для обчислення факторіалу числа.
    import myModule

    num = int(input("Enter the num: "))
    myModule.factorial(num)