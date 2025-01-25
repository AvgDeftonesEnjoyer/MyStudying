check = int(input("Choose homework: 1, 2, 3, 4: "))

if check == 1:
    """Напишите программу, которая выводит все числа от 1 до 100."""
    for i in range(101):
        print(i)
elif check == 2:
    """Создайте таблицу умножения для числа, введенного пользователем"""
    num = int(input("Enter the num: "))
    for i in range(11):
        print(f"{num} x {i} = {num * i}")
elif check == 3:
    """Напишите программу, которая выводит все четные числа от 1 до 50."""
    for i in range(51):
        if i % 2 == 0:
            if i == 0:
                continue
            print(i)
elif check == 4:
    """Реализуйте обратный отсчет от 10 до 1 с выводом: Пуск!"""
    a = 10
    while a > 0:
        print(a)
        a -= 1
    print("Пуск!")