# operators_examples.py

# 1. Arifmetik Operatorlar: +, -, *, /, //, %, **
# ===============================================

# 1.1 Qo‘shish (+)
# Qo‘shish uchun ishlatiladi, oddiy matematik amallarni bajarishda muhim.
a = 5
b = 3
print(f"Qo'shish: {a} + {b} = {a + b}")  # Natija: 8

# 1.2 Ayirish (-)
# Biror qiymatni boshqasidan ayirish uchun ishlatiladi.
print(f"Ayirish: {a} - {b} = {a - b}")  # Natija: 2

# 1.3 Ko‘paytirish (*)
# Qiymatlarni ko‘paytiradi.
print(f"Ko'paytirish: {a} * {b} = {a * b}")  # Natija: 15

# 1.4 Bo‘lish (/)
# Natija doim float turida qaytadi.
print(f"Bo'lish: {a} / {b} = {a / b}")  # Natija: 1.666...

# 1.5 Butun sonli bo‘lish (//)
# Faqat butun qismni qaytaradi.
print(f"Butun sonli bo'lish: {a} // {b} = {a // b}")  # Natija: 1

# 1.6 Qoldiq (%)
# Bo‘lishdan qolgan qoldiqni hisoblaydi.
print(f"Qoldiq: {a} % {b} = {a % b}")  # Natija: 2

# 1.7 Darajaga ko‘tarish (**)
# Biror sonni darajaga ko‘taradi.
print(f"Darajaga ko'tarish: {a} ** {b} = {a ** b}")  # Natija: 125

# Qo‘llanilish joyi: Matematik hisob-kitoblar, algoritmlar, statistik analiz.

# 2. Solishtirish Operatorlari: ==, !=, <, >, <=, >=
# =================================================

# 2.1 Tengmi (==)
# Qiymatlarning tengligini tekshiradi.
print(f"Tengmi: {a} == {b} ? {a == b}")  # Natija: False

# 2.2 Teng emasmi (!=)
# Qiymatlar teng emasligini tekshiradi.
print(f"Teng emasmi: {a} != {b} ? {a != b}")  # Natija: True

# 2.3 Kichikmi (<)
# Bir qiymat boshqasidan kichikligini tekshiradi.
print(f"Kichikmi: {a} < {b} ? {a < b}")  # Natija: False

# 2.4 Katta (<)
# Bir qiymat boshqasidan kattaligini tekshiradi.
print(f"Katta: {a} > {b} ? {a > b}")  # Natija: True

# 2.5 Kichik yoki tengmi (<=)
# Qiymat kichik yoki tengligini tekshiradi.
print(f"Kichik yoki tengmi: {a} <= {b} ? {a <= b}")  # Natija: False

# 2.6 Katta yoki tengmi (>=)
# Qiymat katta yoki tengligini tekshiradi.
print(f"Katta yoki tengmi: {a} >= {b} ? {a >= b}")  # Natija: True

# Qo‘llanilish joyi: Shartli amallar, qaror qabul qilish.

# 3. Mantiqiy Operatorlar: and, or, not
# ====================================

x = True
y = False

# 3.1 Mantiqiy "va" (and)
# Ikkala qiymat ham True bo‘lsa, natija True qaytaradi.
print(f"AND operatori: {x} and {y} = {x and y}")  # Natija: False

# 3.2 Mantiqiy "yoki" (or)
# Hech bo‘lmaganda bittasi True bo‘lsa, True qaytaradi.
print(f"OR operatori: {x} or {y} = {x or y}")  # Natija: True

# 3.3 Mantiqiy "emas" (not)
# Qiymatni teskari qiladi (True -> False, False -> True).
print(f"NOT operatori: not {x} = {not x}")  # Natija: False

# Qo‘llanilish joyi: Shartlarni murakkablashtirish va tekshirish.

# Amaliy holatlar:
# -----------------------------------

# 1. Odd yoki juft son aniqlash (% operatori)
number = 7
if number % 2 == 0:
    print(f"{number} juft son.")
else:
    print(f"{number} toq son.")

# 2. Solishtirish operatorlari bilan qiymat qatorida bo‘lishini tekshirish
value = 25
if 10 <= value <= 50:
    print("Qiymat ruxsat etilgan diapazonda.")
else:
    print("Qiymat diapazondan tashqarida.")

# 3. Mantiqiy operatorlar va foydalanuvchi kirishi
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Kirish muvaffaqiyatli!")
else:
    print("Login yoki parol noto'g'ri.")

# 4. Mantiqiy kombinatsiyalar
is_raining = True
have_umbrella = False
if is_raining and not have_umbrella:
    print("Uyda qoling yoki soyabon oling!")
else:
    print("Yomg'irdan himoyalanish kerak emas.")

# Har bir operator va shart bir-biridan farq qiladi:
# - **Arifmetik operatorlar** matematik amallar uchun ishlatiladi.
# - **Solishtirish operatorlari** shartlarni tekshirishda ishlatiladi.
# - **Mantiqiy operatorlar** bir nechta shartlarni birlashtirish yoki qayta ishlashda ishlatiladi.
