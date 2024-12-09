# 1. Klasslar va Obyektlarga Yo'naltirilgan Dasturlash (OOP)
#   Klasslar va obyektlar nima?
# 1.1. Klasslar - bu obyektlarni yaratish uchun shablon yoki matritsa sifatida ishlaydi.
# 1.2. Obyektlar esa bu klasslardan yaratilgan aniq nusxalar hisoblanadi.

class Car:
    # Klassning __init__ metodida atributlar aniqlanadi
    def __init__(self, make, model, year):
        self.make = make  # Obyektning markasi
        self.model = model  # Obyektning modeli
        self.year = year  # Obyektning ishlab chiqarilgan yili

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


# Obyekt yaratish
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Mustang", 2021)

# Obyektni ishlatish
print(car1.display_info())  # 2020 Toyota Corolla
print(car2.display_info())  # 2021 Ford Mustang


# Klass va obyektlar o'rtasidagi farq:
# Klass: Umumiy shablon, Obyekt: Klassdan yaratilgan aniq nusxalar


# 2. __init__ metodi va atributlar
# 2.1. __init__ metodi - bu konstruktor bo'lib, obyektnik atributlarini o'rnatish uchun ishlatiladi.

class Person:
    def __init__(self, name, age):
        self.name = name  # Obyektning ism atributi
        self.age = age  # Obyektning yosh atributi

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Obyekt yaratish
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.greet())  # Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # Hello, my name is Bob and I am 25 years old.


# 3. Methodlar va inkapsulyatsiya
# 3.1. Inkapsulyatsiya (Encapsulation) - Ma'lumotlarni himoya qilish va faqat kerakli metodlar orqali ma'lumotlarga kirish imkoniyatini yaratish.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Bank hisobining egasi
        self.__balance = balance  # Bank hisobining balans atributi (private)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance  # Balansni olish uchun metod


# Obyekt yaratish
account = BankAccount("Alice", 1000)
account.deposit(200)  # Deposited 200. New balance is 1200.
account.withdraw(500)  # Withdrew 500. New balance is 700.
print(account.get_balance())  # 700


# Inkapsulyatsiya orqali balansni to'g'ridan-to'g'ri o'zgartirish mumkin emas, faqat metodlar orqali


# 4. Vorislik va polimorfizm
# 4.1. Vorislik - Bir klassning xususiyatlarini boshqa bir klassga meros qilib olish.
# 4.2. Polimorfizm - Bir xil nomdagi metodlar turli klasslarda turlicha ishlashini ta'minlaydi.

# Vorislik misoli:
class Animal:
    def speak(self):
        return "Animal makes a sound"


class Dog(Animal):  # Dog klassi Animal klassidan vorislik oladi
    def speak(self):  # Polimorfizm
        return "Woof!"


class Cat(Animal):  # Cat klassi ham Animal klassidan vorislik oladi
    def speak(self):  # Polimorfizm
        return "Meow!"


# Obyektlar yaratish
dog = Dog()
cat = Cat()

# Polimorfizm: Har bir hayvon o'ziga xos ovoz chiqaradi
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!


# Polimorfizmni ko'rish: Agar `speak` metodini chaqirsa, har bir hayvon o'ziga mos ovozni chiqaradi


# 5. OOP da konstruktor va metodlar bilan ishlash
# 5.1. Konstruktor yordamida ma'lumotlarni o'rnatish
# 5.2. Metodlar yordamida obyektlar bilan ishlash

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name} now earns {self.salary}"


# Obyekt yaratish
employee = Employee("John", "Software Engineer", 70000)

# Methodlar yordamida obyektni o'zgartirish
print(employee.give_raise(5000))  # John now earns 75000


# 6. Kapsulyatsiya va inkapsulyatsiya yordamida atributlarga kirish
# 6.1. `@property` dekoratori yordamida atributlarga faqat o'qish imkoniyatini berish

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # private attribute

    @property
    def radius(self):
        return self.__radius  # Only reading the radius

    @property
    def area(self):
        return 3.14 * self.__radius ** 2  # Area calculation


# Obyekt yaratish
circle = Circle(5)
print(circle.radius)  # 5
print(circle.area)  # 78.5


# __radius atributi faqat o'qilishi mumkin, o'zgartirilishi mumkin emas


# 7. Klassdan obyekt yaratish va metod chaqirish
# 7.1. Klass metodlari va instans metodlarining farqi

class Calculator:
    @staticmethod  # Klass metodi
    def add(a, b):
        return a + b

    def subtract(self, a, b):  # Instans metod
        return a - b


# Klass metodidan foydalanish
print(Calculator.add(5, 3))  # 8

# Instans metodidan foydalanish
calc = Calculator()
print(calc.subtract(5, 3))  # 2


# 8. OOPda Multiple Inheritance (Ko'plab vorislik)
# 8.1. Bir nechta klasslardan vorislik olish

class Parent1:
    def speak(self):
        return "I am Parent1"


class Parent2:
    def walk(self):
        return "I am walking"


class Child(Parent1, Parent2):
    def run(self):
        return "I am running"


# Obyekt yaratish
child = Child()
print(child.speak())  # I am Parent1
print(child.walk())  # I am walking
print(child.run())  # I am running


# Multiple inheritance yordamida ikkita klassdan vorislik olish


# 9. OOP da operatorni overload qilish
# 9.1. Python da operatorlarni o'zgartirish

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Obyektlar yaratish
p1 = Point(1, 2)
p2 = Point(3, 4)

# Operatorni overload qilish orqali nuqtalarni qo'shish
p3 = p1 + p2
print(p3)  # Point(4, 6)


# Bu yerda `+` operatori `__add__` metodidan foydalaniladi


# 10. Klasslarda xatoliklarni boshqarish
# 10.1. Klass ichida xatoliklarni boshqarish va Exception larni tutish

class Divisor:
    def __init__(self, value):
        self.value = value

    def divide(self, divisor):
        try:
            result = self.value / divisor
            return result
        except ZeroDivisionError:
            return "Cannot divide by zero"


# Obyekt yaratish
div = Divisor(10)
print(div.divide(2))  # 5.0
print(div.divide(0))  # Cannot divide by zero

# Exception handling yordamida xatoliklarni boshqarish


# Farqlar va qaysi holatda foydalanish:
# 1. **Klasslar va obyektlar**: Klasslar umumiy shablon bo'lib, obyektlar shu klassga asoslangan real instansiyalardir.
# 2. **__init__ metodi**: Obyekt yaratishda avtomatik ravishda chaqiriladi va obyektning boshlang'ich holatini o'rnatadi.
# 3. **Inkapsulyatsiya**: Ma'lumotlarni yashirish va faqat kerakli metodlar orqali o'zgartirishni ta'minlaydi. Masalan, `__balance` atributining maxfiyligi.
# 4. **Vorislik**: Klasslardan xususiyat va metodlarni boshqa klasslarga o'tkazish imkonini beradi. Misol uchun, `Dog` va `Cat` klasslari `Animal` klassidan meros olishadi.
# 5. **Polimorfizm**: Bir xil metod nomi turli klasslarda ishlashi mumkin. Misol uchun, `speak` metodi turli hayvonlar uchun turlicha ishlaydi.
# 6. **Method Overriding**: Meros qilib olingan metodlarni o'zgartirish (override) orqali maxsus funksiyalarni yaratish mumkin.
# 7. **Abstrakt Klasslar**: Metodlarni ta'riflashni faqat shablon sifatida qoldirish va uni keyin real klasslarda amalga oshirish.
# 8. **Multiple Inheritance**: Bir nechta klasslardan xususiyatlar olish imkonini beradi.

# Har bir misolni real dunyo muammolarida ishlatish mumkin. Misol uchun, **inkapsulyatsiya** bank hisob raqamlarini boshqarishda, **vorislik** hayvonlar haqida ma'lumotlar bazasini yaratishda, **polimorfizm** turli xil transport vositalarini boshqarishda, va **method overriding** o'zgaruvchan tizimlarni yaratishda ishlatiladi.
