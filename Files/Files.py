try:
    check = int(input("Choose homework: 1, 2, 3: "))
except ValueError:
    print("Please enter a valid number!")
    exit()

if check == 1:  # Завдання 1: Читання файлу
        with open('Files/data.txt', 'r') as file:
            for line in file:
                print(line, end='')

elif check == 2:  # Завдання 2: Додавання тексту до файлу
        text = input("Enter text to add to data.txt: ")
        with open('Files/data.txt', 'a') as file:
            file.write(text + '\n')
        with open('Files/data.txt', 'r') as file:
            print(file.read())


elif check == 3:  # Завдання 3: Сума чисел з файлу
        total = 0
        with open("Files/numbers.txt", 'r') as file:
            
            for line in file:
                    total += int(line)

        print(f"Total sum: {total}")
    
else:
    print("Invalid choice. Please select 1, 2, or 3.")
