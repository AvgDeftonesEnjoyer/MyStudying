check = int(input("Choose Homework: 1, 2, 3: "))

if check == 1:  #Створи клас "Автомобіль" з атрибутами марка, модель, рік випуску. Додай метод для виведення цієї інформації.
    class Car : 
        def __init__(self, Make, Model, Release_Date):
            self.Make = Make
            self.Model = Model
            self.Release_Date = Release_Date

        def get_info(self):
            print("Make:", self.Make, "Model:", self.Model, "Release date is -", self.Release_Date)

    car1 = Car('Toyota', 'Corrola', 1975)
    car1.get_info()   
elif check == 2: #Реалізуй клас "Тварина" з методом звук(), який перевизначається у дочірніх класах: "Кіт" (звук "мяу") та "Собака" (звук "гав").               
    class Animal:
        def get_sound(self):
            return "This animal makes a sound"
        
    class Dog(Animal):
        def get_sound(self):
            return "Gav!"
        
    class Cat(Animal):
        def get_sound(self):
            return 'Mew'    
        
    dog = Dog()
    cat = Cat()

    print("Dog: ", dog.get_sound)
    print("Cat: ", cat.get_sound)
elif check == 3: #Створи клас "Банк" з методом додати гроші і зняти гроші. Додай обмеження, щоб не можна було зняти більше, ніж є на рахунку.
    class Bank:
        def __init__(self, initial_balance = 0):
            self.balance = initial_balance

        def add_money(self,amount):
            if amount > 0:
                self.balance += amount
                return f"Your new balance is {self.balance}"
            else:
                return "You can add a negative amount"
            
        def take_money(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                return f'You took {amount} from your balance. Your new balance is {self.balance}'
            else:
                return 'Not enough money on your balance'
            
        def get_balance(self):
            return f'Your current balance is {self.balance}'
        
    my_account = Bank(1000)

    print(my_account.get_balance())  # Перевірка балансу
    print(my_account.add_money(500))  # Додати 500
    print(my_account.take_money(300))  # Зняти 300
    print(my_account.take_money(1500))  # Спроба зняти більше, ніж є
else:
    print("Invalid choice. Please select 1, 2, or 3.")

            
    