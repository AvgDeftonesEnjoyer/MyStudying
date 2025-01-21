check = int(input("Choose homework 1, 2, 3: "))

if check == 1: #Напиши програму, яка ділить два числа. Додай обробку помилки ділення на нуль.
    a = int(input("Enter the first num: "))
    b = int(input("Enter the second num: "))

    try:
        result = a / b
        print(f"Here is result {result:.2f}")
    except ZeroDivisionError:
        print("You can divide on zero")
if check == 2: #Реалізуй програму, яка зчитує число з файлу. Якщо файл відсутній, програма повинна створити його та записати туди число за замовчуванням.
    try:
        with open("Exceptions/text.txt", 'r') as file:
            for line in file:
                print(line, end = '')
    except FileNotFoundError:
        print("File is not found, try again !")
if check == 3: #Створи програму, яка запитує у користувача число і виводить його квадрат. Оброби випадок, коли користувач вводить текст замість числа.
    x = True
    while x: 
        try:
            a = int(input("Enter the num: "))
            print(f"Here in {a} in ^2 - {a**2}")
            x = False 
        except ValueError:
            print("Enter the num!")