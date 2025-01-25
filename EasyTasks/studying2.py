check = int(input("Choose homework: 1, 2, 3: "))

if check == 1 :
    """Напишите программу, которая запрашивает у пользователя число и проверяет

    Если оно больше нуля, вывести: "Число положительное".
    Если меньше нуля, вывести: "Число отрицательное".
    Если равно нулю, вывести: "Число равно нулю"."""
    num = int(input("Enter the num: "))
    if num > 0 :
        print(f"{num} is > 0")
    elif num < 0:
        print(f"{num} is < 0")
    elif num == 0 :
        print(f"{num} is = 0") 

elif check == 2:
    """Создайте программу, которая проверяет, является ли введенное пользователем число четным или нечетным."""
    num = int(input("Enter the value of num: "))
    if num % 2 == 0:
        print(f"{num} is even")
    elif num % 2 != 0 :
        print(f"{num} is odd")

elif check == 3:
    """Напишите программу, которая принимает три числа и выводит наибольшее из них."""
    my_list = []
    for i in range(3):
        num = int(input("Enter the num: "))
        my_list.append(num)
    print(f"{max(my_list)} is the biggest num in the list")



