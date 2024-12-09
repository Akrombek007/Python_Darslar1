# 1. Math kutubxonasi bilan ishlash (Matematik amallar)
import math

# 1.1. Kvadrat ildizni hisoblash
print("1.1 Kvadrat ildiz: ", math.sqrt(16))  # 4.0

# 1.2. Pi soni
print("1.2 Pi soni: ", math.pi)  # 3.141592653589793

# 1.3. Faktoriyel
print("1.3 Faktoriyel: ", math.factorial(5))  # 120

# 1.4. Trigonometriya funksiyalari
print("1.4 Sinus: ", math.sin(math.pi / 2))  # 1.0
print("1.4 Kosinus: ", math.cos(0))  # 1.0
print("1.4 Tangens: ", math.tan(math.pi / 4))  # 1.0

# 1.5. Yondoshuvlar (round)
print("1.5 Yondoshish (round): ", round(3.14159, 2))  # 3.14

# 1.6. Logarifm
print("1.6 Logarifm (ln): ", math.log(10))  # 2.302585092994046

# 2. Datetime kutubxonasi bilan ishlash (Vaqt va sana bilan ishlash)
from datetime import datetime, timedelta

# 2.1. Hozirgi sanani olish
print("2.1 Hozirgi sana: ", datetime.now())

# 2.2. Sana formatlash
now = datetime.now()
print("2.2 Sana formatlash: ", now.strftime("%Y-%m-%d %H:%M:%S"))

# 2.3. Sana orasidagi farq (timedelta)
today = datetime.now()
yesterday = today - timedelta(days=1)
print("2.3 Sana farqi: ", today - yesterday)

# 2.4. Sana va vaqtni qo'shish
future_date = today + timedelta(weeks=1)
print("2.4 1 hafta keyingi sana: ", future_date)

# 2.5. Sana va vaqtni taqqoslash
print("2.5 Sana taqqoslash: ", today > yesterday)  # True

# 3. OS kutubxonasi bilan ishlash (Fayllar tizimi va operatsion tizim funksiyalari)
import os

# 3.1. Joriy ishchi katalogni olish
print("3.1 Joriy ishchi katalog: ", os.getcwd())  # Katalogning nomi

# 3.2. Fayl mavjudligini tekshirish
print("3.2 Fayl mavjudligi: ", os.path.exists("example.txt"))  # False (agar fayl bo'lmasa)

# 3.3. Fayl nomini olish
print("3.3 Fayl nomini olish: ", os.path.basename("/path/to/file.txt"))  # file.txt

# 3.4. Katalogni yaratish
os.mkdir("new_directory")  # "new_directory" nomli katalogni yaratadi
print("3.4 Katalog yaratildi!")

# 3.5. Faylni o'chirish
os.remove("example.txt")  # Faylni o'chirish
print("3.5 Fayl o'chirildi!")

# 4. Random kutubxonasi bilan ishlash (Tasodifiy sonlar)
import random

# 4.1. Tasodifiy butun son olish
print("4.1 Tasodifiy butun son (1 dan 10 gacha): ", random.randint(1, 10))  # Masalan, 7

# 4.2. Tasodifiy haqiqiy son olish
print("4.2 Tasodifiy haqiqiy son (0 dan 1 gacha): ", random.random())  # Masalan, 0.37454

# 4.3. Ro'yxatdan tasodifiy element tanlash
items = ["apple", "banana", "cherry", "date"]
print("4.3 Tasodifiy element: ", random.choice(items))  # Masalan, 'banana'

# 4.4. Ro'yxatni tasodifiy tartibda joylashtirish
random.shuffle(items)
print("4.4 Tasodifiy tartiblangan ro'yxat: ", items)

# 4.5. Tasodifiy namunani tanlash
print("4.5 Tasodifiy namunalar (3 ta): ", random.sample(items, 3))  # 3 ta tasodifiy element

# 4.6. Tasodifiy sonlarning yig'indisini hisoblash
print("4.6 Tasodifiy sonlarning yig'indisi: ",
      sum(random.sample(range(1, 101), 5)))  # 5 ta tasodifiy sonning yig'indisi

# 5. Xatoliklarni loglash va qidirish
import logging

# 5.1. Xatolikni loglash
logging.basicConfig(level=logging.INFO)
logging.info("Bu xabar informatsiya")
logging.error("Bu xatolik xabari")

# 6. Fayl bilan ishlash
# 6.1. Faylga yozish
with open("example.txt", "w") as file:
    file.write("Salom, dunyo!")

# 6.2. Fayldan o'qish
with open("example.txt", "r") as file:
    print("6.2 Fayldan o'qish: ", file.read())

# 7. Fayl tizimida o'zgarishlar
# 7.1. Faylni ko'chirish
os.rename("example.txt", "new_example.txt")  # Fayl nomini o'zgartiradi

# 7.2. Faylni ko'chirish
import shutil

shutil.copy("new_example.txt", "copy_example.txt")  # Faylni nusxalash

# 7.3. Faylni o'chirish
os.remove("new_example.txt")  # Faylni o'chirish

# 8. Math va Random bilan ishlash
# 8.1. Sinus va tasodifiy qiymatlarning hisoblanishi
print("8.1 Sinus bilan tasodifiy sonning yondoshuvi: ", math.sin(random.random() * math.pi))

# 8.2. Tasodifiy tanlangan sonni tanlash va uning yondoshuvini topish
print("8.2 Tasodifiy butun son va uning kvadrat ildizi: ", random.randint(1, 100), math.sqrt(random.randint(1, 100)))

# 9. Vaqt va sanani manipulyatsiya qilish
# 9.1. Hozirgi sanani olish va uni qo'shish
new_date = datetime.now() + timedelta(days=5)
print("9.1 Hozirgi sana va 5 kun keyingi sana: ", datetime.now(), new_date)

# 10. Katalogda faylni izlash
# 10.1. Fayl nomini izlash
directory = os.getcwd()
files = os.listdir(directory)
print("10.1 Katalogdagi fayllar: ", files)
