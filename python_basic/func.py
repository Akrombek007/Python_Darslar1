# 6. Funksiyalar - To'liq Qo'llanma va Namuna Kodlar

# 1. Nima uchun funksiyalar kerak?
# Misol: Funksiyalar kodni qayta-qayta yozish o'rniga, uni takroriy ishlatishga yordam beradi.

def greeting(name):
    """Foydalanuvchini salomlash."""
    return f"Salom, {name}!"


# Funksiyani qayta-qayta chaqirish
print(greeting("Akrom"))
print(greeting("Zarina"))


# Tushuntirish: Bu yondashuv bilan salomlashni har safar yozish shart emas.
# Katta loyihalarda takroriy koddan qochish va tuzilmani toza saqlash uchun kerak.

# 2. Funksiyalarni yaratish va chaqirish
# Misol: Funksiya yaratiladi va chaqiriladi.

def add(a, b):
    """Ikki sonni qo'shish."""
    return a + b


result = add(10, 5)
print(f"10 + 5 = {result}")


# Tushuntirish: Funksiyalarni parametrlar bilan dinamik foydalanish imkoniyati mavjud.
# Bu misolda sonlarni qo'shish oson va moslashuvchan.

# 3. Funksiya ichida boshqa funksiyadan foydalanish
def multiply_and_add(a, b, c):
    """Ikki sonni ko'paytirish va keyin uchinchi sonni qo'shish."""

    def multiply(x, y):
        return x * y

    product = multiply(a, b)
    return product + c


print(multiply_and_add(2, 3, 5))  # Natija: 11


# Tushuntirish: Funksiya ichida funksiya yaratib, murakkab logikani boshqarish osonlashadi.

# 4. Parametrlar bilan ishlash
# Misol: Default qiymatlar bilan parametrlar

def greet_with_language(name, language="uz"):
    """Tilga qarab salomlash."""
    greetings = {
        "uz": "Salom",
        "en": "Hello",
        "ru": "Привет"
    }
    return f"{greetings.get(language, 'Salom')}, {name}!"


print(greet_with_language("Akrom"))
print(greet_with_language("John", language="en"))


# Tushuntirish: Default qiymatlar funksiyani dinamik qiladi va foydalanuvchidan kamroq ma'lumot talab qiladi.

# 5. Qaytish qiymatlari
# Misol: Funksiya bir nechta qiymatni qaytarishi

def calculate(a, b):
    """Qo'shish va ayirish natijalarini qaytaradi."""
    return a + b, a - b


add_result, sub_result = calculate(7, 3)
print(f"Qo'shish: {add_result}, Ayirish: {sub_result}")

# Tushuntirish: Funksiyalar birdan ortiq qiymatni qaytarib, murakkab hisob-kitoblarni bir joyda boshqarish imkonini beradi.

# 6. Lambda funksiyalar
# Misol: Lambda yordamida oddiy hisob-kitob

double = lambda x: x * 2
print(double(4))  # Natija: 8

# Tushuntirish: Lambda funksiya qisqa va vaqtinchalik hisob-kitoblar uchun ishlatiladi.

# 7. Lambda va `filter` bilan ishlash
numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Natija: [2, 4, 6]


# Tushuntirish: Lambda funksiyalarni `filter` va `map` kabi funksiyalar bilan qo'shib ishlatish samarali.

# 8. Kengaytirilgan holat: Funksiya ichida lambda
def create_multiplier(n):
    """Multiplikator funksiyasini yaratadi."""
    return lambda x: x * n


times_three = create_multiplier(3)
print(times_three(5))  # Natija: 15


# Tushuntirish: Lambda funksiyalarni boshqa funksiyalar ichida yaratib, ulardan moslashuvchan foydalanish mumkin.

# 9. Rekursiv funksiyalar
# Misol: Faktorialni hisoblash

def factorial(n):
    """Rekursiya yordamida faktorialni hisoblash."""
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # Natija: 120


# Tushuntirish: Rekursiv funksiyalar murakkab algoritmlarni sodda ko'rinishda yozishga yordam beradi.

# 10. Qo‘shimcha: Funksiyadan funksiya qaytarish
def make_power_function(n):
    """Darajaga oshiruvchi funksiya yaratadi."""

    def power(x):
        return x ** n

    return power


square = make_power_function(2)
cube = make_power_function(3)
print(square(4))  # Natija: 16
print(cube(2))  # Natija: 8


# Tushuntirish: Funksiyadan boshqa funksiya qaytarish murakkab matematik operatsiyalarni boshqarish imkonini beradi.

# 11. Holat: Ko'p variantli parametrlar
def print_args(*args, **kwargs):
    """Har qanday parametrlarni qabul qiluvchi funksiya."""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")


print_args(1, 2, 3, name="Akrom", age=25)

# Tushuntirish: Ko‘p sonli va turli xil parametrlar bilan ishlashda foydalaniladi.
