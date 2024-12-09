# 1. Oddiy Kalkulyator
# Ushbu misolda oddiy kalkulyator dasturni yaratish orqali foydalanuvchidan ikkita sonni kiritishni va ularni qo'shish, ayirish, ko'paytirish va bo'lish operatsiyalarini bajarishni so'raymiz.

def calculator():
    print("Oddiy Kalkulyator:")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")

    choice = input("Tanlang (1/2/3/4): ")

    num1 = float(input("Birinchi sonni kiriting: "))
    num2 = float(input("Ikkinchi sonni kiriting: "))

    if choice == '1':
        print(f"Natija: {num1 + num2}")
    elif choice == '2':
        print(f"Natija: {num1 - num2}")
    elif choice == '3':
        print(f"Natija: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Natija: {num1 / num2}")
        else:
            print("Xatolik: Nolga bo'lish mumkin emas.")
    else:
        print("Noto'g'ri tanlov!")


# 2. Kontaktlar Bazasini Yaratish
# Bu misolda foydalanuvchidan ism, telefon raqamini kiritish va ularni saqlashni so'raymiz. Kontaktlar bazasini yaratish.

contacts = []


def add_contact():
    name = input("Ismingizni kiriting: ")
    phone = input("Telefon raqamingizni kiriting: ")
    contacts.append({"name": name, "phone": phone})
    print(f"Kontakt qo'shildi: {name} - {phone}")


def show_contacts():
    if contacts:
        print("Barcha kontaktlar:")
        for contact in contacts:
            print(f"{contact['name']} - {contact['phone']}")
    else:
        print("Kontaktlar ro'yxati bo'sh.")


def contact_manager():
    while True:
        print("\n1. Kontakt qo'shish")
        print("2. Kontaktlarni ko'rish")
        print("3. Chiqish")

        choice = input("Tanlovni kiriting (1/2/3): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            break
        else:
            print("Noto'g'ri tanlov!")


# 3. Foydalanuvchi Kirish Tizimi
# Foydalanuvchi login tizimi yaratish. Foydalanuvchi ismi va parolini kiritish, ularni tasdiqlash.

users = {
    "admin": "password123",
    "user": "pass456"
}


def user_login():
    username = input("Foydalanuvchi nomini kiriting: ")
    password = input("Parolni kiriting: ")

    if username in users and users[username] == password:
        print(f"Xush kelibsiz, {username}!")
    else:
        print("Noto'g'ri foydalanuvchi nomi yoki parol!")


# 4. Vaqtni Hisoblash
# Ushbu misol orqali foydalanuvchidan boshlanish va tugash vaqtlarini kiritib, vaqtni hisoblashni amalga oshiramiz.

from datetime import datetime


def calculate_time():
    start_time = input("Boshlanish vaqtini kiriting (HH:MM:SS formatida): ")
    end_time = input("Tugash vaqtini kiriting (HH:MM:SS formatida): ")

    start_time = datetime.strptime(start_time, "%H:%M:%S")
    end_time = datetime.strptime(end_time, "%H:%M:%S")

    time_diff = end_time - start_time
    print(f"Vaqt farqi: {time_diff}")


# 5. To'lov Hisobi (Invoice Generator)
# Bu misolda foydalanuvchidan mahsulot nomi va narxini kiritib, hisob-kitob yaratamiz.

def generate_invoice():
    items = []
    total_price = 0

    while True:
        item_name = input("Mahsulot nomini kiriting (yoki 'chiqish' deb yozing): ")
        if item_name.lower() == 'chiqish':
            break
        item_price = float(input(f"{item_name} ning narxini kiriting: "))
        items.append((item_name, item_price))
        total_price += item_price

    print("\nHisob-kitob:")
    for item in items:
        print(f"{item[0]}: {item[1]} so'm")
    print(f"Jami to'lov: {total_price} so'm")


# 6. Kalendar yaratish
# Bu misolda foydalanuvchi kiritgan yil va oy bo'yicha o'sha oy uchun kalendarni yaratamiz.

import calendar


def generate_calendar():
    year = int(input("Yilni kiriting: "))
    month = int(input("Oy raqamini kiriting (1-12): "))

    print(calendar.month(year, month))


# 7. Tasodifiy Parol Generator
# Bu misolda tasodifiy parol yaratish uchun alifbo va raqamlardan foydalangan holda parol yaratamiz.

import random
import string


def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Yaratilgan parol: {password}")


# 8. CSV Faylga Ma'lumotlarni Saqlash
# Bu misolda foydalanuvchidan ma'lumotlarni kiritib, ularni CSV formatida saqlaymiz.

import csv


def save_to_csv():
    data = []
    while True:
        name = input("Ismingizni kiriting (chiqish uchun 'stop' deb yozing): ")
        if name.lower() == 'stop':
            break
        age = input(f"{name} ning yoshini kiriting: ")
        data.append([name, age])

    with open("data.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Ism", "Yosh"])
        writer.writerows(data)
    print("Ma'lumotlar CSV faylga saqlandi.")


# 9. Foydalanuvchi Hisobini Yangilash
# Bu misolda foydalanuvchi malumotlarini (ism va email) yangilash imkonini beramiz.

user_info = {
    "user1": {"name": "John", "email": "john@example.com"},
    "user2": {"name": "Alice", "email": "alice@example.com"}
}


def update_user_info():
    username = input("Foydalanuvchi nomini kiriting: ")
    if username in user_info:
        name = input("Ismni yangilang: ")
        email = input("Email manzilini yangilang: ")
        user_info[username]["name"] = name
        user_info[username]["email"] = email
        print(f"{username} malumotlari yangilandi.")
    else:
        print(f"{username} topilmadi.")


# 10. Faylni O'qish va Yozish
# Bu misolda fayldan ma'lumotlarni o'qish va unga yozish imkoniyatini yaratamiz.

def read_and_write_file():
    filename = input("Fayl nomini kiriting: ")

    with open(filename, 'w') as file:
        file.write("Bu test fayli.\n")
        file.write("Foydalanuvchi ma'lumotlari saqlanadi.")

    print(f"{filename} faylga ma'lumot yozildi.")

    with open(filename, 'r') as file:
        content = file.read()
        print(f"Fayldan o'qilgan ma'lumot: \n{content}")


# 11. To'lov Hisobi (Bill Generation)
# Foydalanuvchi buyurtmasini hisoblash, soliq qo'shish va umumiy to'lovni chiqarish.

def generate_bill():
    items = []
    total = 0
    while True:
        item = input("Mahsulot nomini kiriting (yoki 'stop' deb yozing): ")
        if item.lower() == 'stop':
            break
        price = float(input(f"{item} narxini kiriting: "))
        items.append((item, price))
        total += price

    tax = total * 0.15
    total_with_tax = total + tax
    print("\nBill:")
    for item, price in items:
        print(f"{item}: {price} so'm")
    print(f"Jami soliq: {tax} so'm")
    print(f"Umumiy to'lov: {total_with_tax} so'm")


# 12. Sodda Ma'lumotlar Bazasini Yaratish
# Ma'lumotlar bazasini yaratish, saqlash va o'qish.

import sqlite3


def create_database():
    conn = sqlite3.connect('simple_db.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)''')
    c.execute("INSERT INTO users (name, age) VALUES ('John', 30)")
    conn.commit()
    conn.close()


def read_database():
    conn = sqlite3.connect('simple_db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()


if __name__ == "__main__":
    # Barcha funksiyalarni faollashtiruvchi qismlar
    while True:
        print("\n1. Kalkulyator")
        print("2. Kontaktlar Bazasini Yaratish")
        print("3. Foydalanuvchi Kirish Tizimi")
        print("4. Vaqtni Hisoblash")
        print("5. To'lov Hisobi")
        print("6. Kalendar Yaratish")
        print("7. Parol Generator")
        print("8. CSV Faylga Ma'lumotlarni Saqlash")
        print("9. Foydalanuvchi Hisobini Yangilash")
        print("10. Faylni O'qish va Yozish")
        print("11. To'lov Hisobi (Bill Generation)")
        print("12. Ma'lumotlar Bazasini Yaratish")

        choice = input("Tanlovni kiriting (1-12): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            contact_manager()
        elif choice == '3':
            user_login()
        elif choice == '4':
            calculate_time()
        elif choice == '5':
            generate_invoice()
        elif choice == '6':
            generate_calendar()
        elif choice == '7':
            generate_password()
        elif choice == '8':
            save_to_csv()
        elif choice == '9':
            update_user_info()
        elif choice == '10':
            read_and_write_file()
        elif choice == '11':
            generate_bill()
        elif choice == '12':
            create_database()
            read_database()
        else:
            print("Noto'g'ri tanlov!")
        cont = input("Yana davom ettirasizmi? (ha/yo'q): ")
        if cont.lower() != 'ha':
            break
