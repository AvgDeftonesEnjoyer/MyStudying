check = int(input("Choose homework: 1, 2, 3, 4, 5 : "))

if check == 1 : #списки
    check1 = int(input("Choose homework: 1, 2 : "))
    if check1 == 1:
        #Створи список чисел від 1 до 10. Видали всі парні числа та виведи залишок.
        user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i = 0
        while i < len(user_list):
            if user_list[i] % 2 == 0:
                user_list.pop(i)
            else:
                i += 1
        print(user_list)
    elif check1 == 2:
        #Реалізуй програму, яка приймає список слів і друкує довжину кожного слова.
        user_list = ["hello world", "USA", "apple", "rust", "im learning python"]
        i = 0
        while i < len(user_list):
            print(f"Length of '{user_list[i]}' is {len(user_list[i])}")
            i += 1

elif check == 2: #Кортежи
    #Створи кортеж із 5 елементів. Виведи другий і четвертий елементи.
    data = (1, 2, 3, 4, 5)
    print(data[2] , data[4])
        
elif check == 3 : #Словари
    products_list = {"apple": 98, "orange": 45, "pineaplle": 20, "grape": 98, "banana": 57}
    
    keys = list(products_list.keys())
    values = list(products_list.values())

    index_of_product = values.index(min(values)) # індекс мін значення

    product_name = keys[index_of_product]

    print(f"The {product_name} has a lowest price - {min(values)}")

elif check == 4: #Множини
    list_A = {1, 2, 3, 4}
    list_B = {5, 2, 7, 8, 1}
    
    print(f"The interstections of list A and list B are : {list_A.intersection(list_B)}")

elif check == 5: # рядки
    string = input("Enter the string: ")
    if string == string[::-1]: 
        print(f"The word {string} is palindrom")
    else:
        print(f"The word {string} is not palindrom")
