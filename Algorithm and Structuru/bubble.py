check = int(input("Choose homework : 1, 2, 3: "))

if check == 1 : #Реалізуй алгоритм сортування бульбашкою для списку чисел.
    n = 6
    mas = [ 5, 7, 4, 3, 8, 2]
    count = 0

    for run in range(n - 1):
        for i in range(n - 1 - run):
            if mas[i] > mas[i+1]:
                count += 1
                mas[i], mas[i+1] = mas[i+1], mas[i]

    print(*mas)
    print(count)
    
elif check == 2 : #Напиши програму, яка реалізує лінійний пошук заданого числа у списку.
    mas = [2, 4, 15, 657, 980, 5, 15, 67, 89, 45, 59, 69, 23, 56, 76, 80, 123, 225]
    num = int(input("Enter the u want to find : "))
    found = False

    for i in mas:
        if i == num:
            print(f"Num if found! Here is it's index - {mas.index(num)}")
            found = True
            break
    if not found:
        print("Num is not found !")

elif check == 3: # Створи простий стек з використанням списку. Реалізуй методи push, pop, peek.
    stack = [2, 4, 15, 657, 980, 5, 15, 67, 89, 45, 59, 69, 23, 56, 76, 80, 123, 225]

    num1 = int(input("Enter num to append : "))
    stack.append(num1)
    print(stack)

    print(stack.pop())

    print(stack[-1])