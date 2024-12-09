# Dekoratorlar haqida to'liq qo'llanma va misollar

# 1. Oddiy Dekorator
def simple_decorator(func):
    """Oddiy dekorator - funksiya argument sifatida oladi va uni qayta ishlaydi"""

    def wrapper():
        print("Dekorator ishga tushdi!")
        func()
        print("Dekorator ishini tugatdi.")

    return wrapper


@simple_decorator
def say_hello():
    """Salom beruvchi funksiya"""
    print("Salom!")


# say_hello() ni chaqirganimizda quyidagicha natija bo'ladi:
# Dekorator ishga tushdi!
# Salom!
# Dekorator ishini tugatdi.
print("\n1. Oddiy dekorator misoli:")
say_hello()


# 2. Dekoratorga parametr uzatish
def repeat_decorator(times):
    """Dekorator, funksiyani berilgan marta qayta ishlash uchun"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_decorator(3)  # Funksiyani 3 marta chaqirish uchun
def greet(name):
    print(f"Salom, {name}!")


# greet() chaqirilganda, "Salom, John!" 3 marta chiqariladi
print("\n2. Parametrli dekorator misoli:")
greet("John")


# 3. Funksiya qiymatini o'zgartirish
def double_return(func):
    """Funksiyaning natijasini ikki marta qaytarish uchun dekorator"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


@double_return
def add(a, b):
    """Ikki sonni qo'shish"""
    return a + b


# add(3, 5) ning natijasi 16 bo'ladi (8 qaytariladi, chunki natija ikki marta qaytariladi)
print("\n3. Funksiya natijasini ikki marta qaytarish:")
print(add(3, 5))


# 4. Dekorator yordamida xatoliklarni tutish
def error_handling_decorator(func):
    """Funksiya chaqirilganda xatoliklarni tutish uchun dekorator"""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")

    return wrapper


@error_handling_decorator
def divide(a, b):
    """Ikki sonni bo'lish"""
    return a / b


# 10 / 0 ga bo'lishni sinab ko'ramiz, xatolik yuz beradi
print("\n4. Xatolikni tutish dekoratori misoli:")
divide(10, 0)

# 5. Dekorator yordamida vaqtni o'lchash
import time


def timer_decorator(func):
    """Funksiyaning bajarilish vaqtini o'lchash uchun dekorator"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funksiya bajarilishi {end_time - start_time:.4f} soniya davom etdi.")
        return result

    return wrapper


@timer_decorator
def long_running_task():
    """Bir necha soniya davom etadigan vazifa"""
    time.sleep(2)


# long_running_task() chaqirilganda vaqt o'lchovi amalga oshiriladi
print("\n5. Vaqt o'lchash dekoratori misoli:")
long_running_task()


# 6. Dekorator yordamida chiquvchi qiymatni o'zgartirish
def square_decorator(func):
    """Funksiyaning chiqishini kvadrat qilish uchun dekorator"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2

    return wrapper


@square_decorator
def get_number():
    """Oddiy sonni qaytarish"""
    return 5


# get_number() 5 ni qaytaradi, lekin dekorator yordamida 25 qaytadi
print("\n6. Chiquvchi qiymatni o'zgartirish:")
print(get_number())


# 7. Dekoratorni sinovdan o'tkazish va xatoliklarni qayta ishlash
def try_again_decorator(retries):
    """Dekorator, xatolik yuz berishi mumkin bo'lgan funksiyani qayta bajarish"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Xatolik: {e}. Qayta urinib ko'ring...")
                    attempt += 1
            print("Maxsus xatoliklar yuz berdi, urinishlar tugadi.")

        return wrapper

    return decorator


@try_again_decorator(3)
def unstable_function():
    """Ikkita sinov uchun xatolik beradigan funksiya"""
    if random.choice([True, False]):
        raise ValueError("Tasodifiy xatolik!")
    return "Hammasi yaxshi!"


# Unstable function ishlaganda xatoliklarni qayta sinab ko'radi
print("\n7. Xatolikni qayta sinab ko'rish dekoratori misoli:")
print(unstable_function())

# 8. Kesh bilan ishlash dekoratori
from functools import lru_cache


@lru_cache(maxsize=128)
def expensive_function(n):
    """Katta hisoblash vaqti talab etadigan funksiya"""
    time.sleep(2)  # hisoblashing vaqtini simulyatsiya qilish
    return n * n


# Birinchi chaqiruvda keshga saqlanadi, ikkinchisida esa keshdan olinadi
print("\n8. Kesh bilan ishlash dekoratori misoli:")
print(expensive_function(10))  # Hisoblash birinchi marta
print(expensive_function(10))  # Keshdan olinadi


# 9. Dekorator yordamida ma'lumotlarni formatlash
def upper_case_decorator(func):
    """Funksiya natijasini katta harfda qaytarish uchun dekorator"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@upper_case_decorator
def greet_user(name):
    """Foydalanuvchiga salom beruvchi funksiya"""
    return f"Salom, {name}!"


# greet_user() salomni katta harflar bilan qaytaradi
print("\n9. Ma'lumotlarni formatlash dekoratori misoli:")
print(greet_user("Ali"))


# 10. Dekorator yordamida obyektga metod qo'shish
def add_method_decorator(cls):
    """Klassga yangi metod qo'shish uchun dekorator"""

    def new_method(self):
        return "Yangi metod qo'shildi!"

    setattr(cls, 'new_method', new_method)
    return cls


@add_method_decorator
class MyClass:
    """Oddiy sinf"""

    def hello(self):
        return "Salom!"


# MyClass instansiyasiga yangi metod qo'shiladi
print("\n10. Obyektga metod qo'shish dekoratori misoli:")
obj = MyClass()
print(obj.new_method())  # Yangi metod ishlatiladi
