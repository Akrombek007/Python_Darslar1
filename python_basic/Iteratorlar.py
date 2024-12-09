# 11. Kengaytirilgan Mavzular: Iteratorlar va Generatorlar

# 1. **Iteratorlar haqida tushuncha**
# Iteratorlar Python-da biror kolleksiya ustida bitta elementni ketma-ket qaytarishga imkon beruvchi obyektlardir.
# Iteratorlar ikkita asosiy metodga ega:
# - __iter__(): Bu metod iteratordan birinchi elementni qaytaradi va iteratsiya qilish imkoniyatini yaratadi.
# - __next__(): Har safar chaqirilganda keyingi elementni qaytaradi.

# Quyidagi misolda iteratorni yaratish ko'rsatilgan.

class MyIterator:
    def __init__(self, start, end):
        self.current = start  # Boshlanish qiymati
        self.end = end  # Tugash qiymati

    # __iter__ metodini yozish kerak
    def __iter__(self):
        return self  # Iteratorni o'zi qaytadi

    # __next__ metodini yozish kerak
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Agar tugash qiymatiga yetilsa, StopIteration xatosi chiqariladi
        self.current += 1
        return self.current - 1  # Hozirgi qiymatni qaytarish

# Iteratorni yaratish va foydalanish
iterator = MyIterator(0, 5)
for value in iterator:
    print(value)

# Natija:
# 0
# 1
# 2
# 3
# 4

# 2. **Generatorlar haqida tushuncha**
# Generatorlar esa iteratorlarni yaratishning qulayroq va samaraliroq usuli bo'lib, ular `yield` operatorini ishlatadi.
# Generatorlar iteratsiya qilish jarayonini yengillashtiradi va xotirada katta hajmdagi ma'lumotlarni saqlashni talab qilmaydi.

# Quyidagi misolda generatordan foydalanish ko'rsatilgan.

def my_generator(start, end):
    current = start
    while current < end:
        yield current  # yield operatori generatorni keyingi qiymatni qaytarishga o'tkazadi
        current += 1

# Generatorni yaratish va foydalanish
gen = my_generator(0, 5)
for value in gen:
    print(value)

# Natija:
# 0
# 1
# 2
# 3
# 4

# 3. **Iterator va generatorning farqlari**
# - Iteratorlar klasslarni yaratishni talab qiladi, ya'ni `__iter__` va `__next__` metodlarini yozish kerak.
# - Generatorlar esa oson va qisqa kod yozishni talab qiladi, faqat `yield` operatori yordamida generator yaratish mumkin.

# 4. **Yangi generator yaratish**
# Yangi generator yaratishda `yield` operatori yordamida yangi qiymatlarni qaytarish mumkin.

def even_numbers(n):
    """N sonigacha bo'lgan juft sonlarni qaytaruvchi generator"""
    for i in range(n):
        if i % 2 == 0:
            yield i

# Generatorni yaratish va undan foydalanish
for num in even_numbers(10):
    print(num)

# Natija:
# 0
# 2
# 4
# 6
# 8

# 5. **`yield` operatori haqida tushuncha**
# `yield` operatori generatorni `return` kabi ishlatadi, lekin har safar chaqirilganda keyingi qiymatni qaytaradi va ichki holatni saqlaydi.

def count_up_to(max):
    count = 0
    while count < max:
        yield count
        count += 1

# Generatorni yaratish
counter = count_up_to(3)
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
# print(next(counter))  # StopIteration xatosi chiqariladi

# 6. **Birinchi generatorni ishlatish va qaytarish**
# Generatorlar faqatgina bir marta ishlatiladi. Ularni yana qayta ishlatib bo'lmaydi, ammo yangi generator yaratish mumkin.

gen = (x * x for x in range(5))  # List comprehension bilan generator
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
print(next(gen))  # 16

# 7. **Generator bilan fayldan ma'lumotlarni o'qish**
# Generatorlarni faylni o'qish jarayonida samarali ishlatish mumkin.

def read_large_file(file_path):
    """Katta fayldan ma'lumotlarni o'qish uchun generator"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Generatorni yaratish va undan foydalanish
file_gen = read_large_file('large_file.txt')  # Fayl nomini to'g'ri kiriting
for line in file_gen:
    print(line.strip())

# 8. **`itertools` moduli yordamida iteratorlar**
# `itertools` moduli iteratorlarni yaratish uchun juda foydalidir.

import itertools

# Aksiyalikni topish
numbers = [1, 2, 3]
iterator = itertools.count(start=0, step=1)  # Infinite iterator
print(next(iterator))  # 0
print(next(iterator))  # 1
print(next(iterator))  # 2

# 9. **`zip` yordamida bir nechta iteratsiyalarni birlashtirish**
# Bir nechta iteratorlarni birlashtirish uchun `zip` yordamida foydalanish mumkin.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Natija:
# Alice: 85
# Bob: 90
# Charlie: 92

# 10. **`enumerate` yordamida ro'yxatdagi indekslar bilan ishlash**
# `enumerate` yordamida ro'yxatdagi elementlarning indekslarini olish mumkin.

names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

# Natija:
# 0: Alice
# 1: Bob
# 2: Charlie

# 11. **Generatorning xotira samaradorligi**
# Generatorlar katta ma'lumotlarni xotirada saqlash zarurati yo'q, bu esa ularni samarali qiladi.

def big_range(n):
    """Katta diapazondagi sonlarni generator yordamida yaratish"""
    for i in range(n):
        yield i

# 1000000 ta elementni generator yordamida yaratish
gen = big_range(1000000)
print(next(gen))  # 0
print(next(gen))  # 1

# 12. **Generatorni `send` va `throw` metodlari bilan ishlatish**
# Generatorga tashqi qiymatlarni yuborish yoki xatolik yuborish mumkin.

def counter():
    count = 0
    while True:
        value = yield count
        if value is not None:
            count = value
        else:
            count += 1

# Generatorni ishga tushirish
gen = counter()
print(next(gen))  # 0
print(next(gen))  # 1
print(gen.send(5))  # 5
print(next(gen))  # 6
