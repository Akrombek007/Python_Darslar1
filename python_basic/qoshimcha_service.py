# 1. **Iteratorlar**:
# Iteratorlar obyektlarining elementlariga ketma-ket kirish uchun ishlatiladi.
# Iteratorlar "iter()" va "next()" metodlarini ishlatadi.

# Namuna 1: Oddiy iterator yaratish
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Iteratorni tugatish
        self.current += 1
        return self.current - 1


# Foydalanish
iterator = MyIterator(0, 5)
for value in iterator:
    print(value)

# Namuna 2: Iteratorning "next()" metodidan foydalanish
my_iterator = iter([1, 2, 3, 4])
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2

# Namuna 3: Iteratorni "for" sikli bilan ishlatish
for num in range(5):
    print(num)


# 2. **Generatorlar**:
# Generatorlar iteratorlar kabi ishlaydi, lekin ularning afzalligi - ularni yaratish osonroq va xotira samarali.
# "yield" kalit so'zi generatorni yaratishda ishlatiladi.

# Namuna 4: Oddiy generator
def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)


# Namuna 5: Fibonacci sonlar generatori
def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a
        n -= 1


for num in fibonacci(5):
    print(num)  # 0 1 1 2 3

# Namuna 6: Generatorda tasodifiy sonlar
import random


def random_numbers(count):
    for _ in range(count):
        yield random.randint(1, 100)


for num in random_numbers(5):
    print(num)


# 3. **Dekoratorlar**:
# Dekoratorlar funksiya yoki metodlarning xulqini o'zgartirish uchun ishlatiladi. Ular boshqa funksiya yoki metodga argument sifatida beriladi.

# Namuna 7: Oddiy dekorator
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# Namuna 8: Funksiya bilan argumentlar qabul qiluvchi dekorator
def decorator_with_args(func):
    def wrapper(arg):
        print("Argument received:", arg)
        return func(arg)

    return wrapper


@decorator_with_args
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")

# Namuna 9: Dekoratorlar yordamida vaqtni o'lchash
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time} seconds.")
        return result

    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)


slow_function()


# Namuna 10: Dekorator yordamida xatolikni qayta ishlash
def error_handling_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred: {e}")

    return wrapper


@error_handling_decorator
def divide(a, b):
    return a / b


print(divide(10, 2))
print(divide(10, 0))  # ZeroDivisionError


# 4. **Kontekst Menejerlari (with operatori)**:
# `with` operatori yordamida resurslarni boshqarish va xatoliklardan saqlanish mumkin.
# Kontekst menejerlari yordamida resurslar (masalan, fayl) osonlik bilan boshqariladi va ularni ishlatganingizdan so'ng tozalanadi.

# Namuna 11: Oddiy kontekst menejeri
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"Exception: {exc_value}")
        return True  # True bo'lsa, xato tutiladi


# Foydalanish
with MyContextManager() as cm:
    print("Inside the context")
    raise ValueError("Something went wrong!")  # Exceptionni tutish

# Namuna 12: Fayl bilan ishlash
with open('example.txt', 'w') as file:
    file.write("Hello, this is a test file.")

# Namuna 13: Faylni o'qish va xatoliklarni boshqarish
try:
    with open('non_existent_file.txt', 'r') as file:
        data = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")


# Namuna 14: Resurslarni boshqarish
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to the database")
        self.connection = "DB Connection"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing the database connection")
        self.connection = None
        if exc_type:
            print(f"Exception: {exc_value}")


with DatabaseConnection() as db:
    print(db)

# Namuna 15: Timer kontekst menejeri
from time import time


class Timer:
    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time()
        print(f"Execution time: {self.end - self.start} seconds")


with Timer():
    sum([i for i in range(1000000)])

# Namuna 16: `open()` yordamida faylga yozish va o'qish
with open('example.txt', 'w') as f:
    f.write("This is a test file for context manager demo.")

with open('example.txt', 'r') as f:
    print(f.read())

# Namuna 17: `with` va `lock` obyektlaridan foydalanish
from threading import Lock

lock = Lock()


def critical_section():
    with lock:
        print("In critical section")


critical_section()


# Namuna 18: Resurslarni boshqarish (matritsa)
class Matrix:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        print("Entering matrix context")
        return self.data

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting matrix context")


with Matrix([[1, 2], [3, 4]]) as matrix:
    print("Matrix:", matrix)
