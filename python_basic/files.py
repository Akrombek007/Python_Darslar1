import csv
import json


# 1. Fayl ochish va yopish
def open_close_example():
    # Fayl ochish va yopishning asosiy usuli
    file = open('example.txt', 'w')  # Yozish rejimi
    file.write("Hello, World!")
    file.close()

    # Ochiq qolgan fayllar xotira muammolariga olib kelishi mumkin.
    # Shuning uchun 'with' kontekst menejeridan foydalanamiz.
    with open('example.txt', 'r') as file:
        content = file.read()
        print("Fayldan o'qildi:", content)


# 2. Faylga yozish (write) va o'qish (read)
def write_read_example():
    # Faylga yozish
    with open('example.txt', 'w') as file:
        file.write("Python'da fayllar bilan ishlashni o'rganamiz.\n")
        file.write("Bu juda foydali mavzu.\n")

    # Faylni o'qish
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print("O'qilgan qatorda:", line.strip())


# 3. Faylga yozishni davom ettirish (append)
def append_example():
    with open('example.txt', 'a') as file:
        file.write("Qo'shimcha ma'lumotlar yozilmoqda.\n")


# 4. CSV fayllar bilan ishlash
def csv_example():
    # CSV faylga yozish
    data = [["Name", "Age", "Country"],
            ["Alice", 30, "USA"],
            ["Bob", 25, "UK"],
            ["Charlie", 35, "Canada"]]
    with open('example.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    # CSV faylni o'qish
    with open('example.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("CSV Qator:", row)


# 5. JSON fayllar bilan ishlash
def json_example():
    # JSON ma'lumotni yozish
    data = {"name": "Alice", "age": 30, "country": "USA"}
    with open('example.json', 'w') as jsonfile:
        json.dump(data, jsonfile)

    # JSON faylni o'qish
    with open('example.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        print("JSON ma'lumot:", data)


# 6. Fayllarni o'chirish
import os


def delete_file_example():
    if os.path.exists('example.txt'):
        os.remove('example.txt')
        print("'example.txt' o'chirildi.")
    else:
        print("'example.txt' mavjud emas.")


# 7. Faylni o'qishda xatoliklarni boshqarish
def error_handling_example():
    try:
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("Fayl topilmadi. Iltimos, fayl nomini tekshiring.")
    except Exception as e:
        print("Xato yuz berdi:", str(e))


# 8. Binariy fayllar bilan ishlash
def binary_file_example():
    # Binariy faylga yozish
    with open('example.bin', 'wb') as binary_file:
        binary_file.write(b'This is binary data.')

    # Binariy faylni o'qish
    with open('example.bin', 'rb') as binary_file:
        data = binary_file.read()
        print("Binariy ma'lumot:", data)


# Har bir funksiyani chaqirish
if __name__ == "__main__":
    print("1. Fayl ochish va yopish:")
    open_close_example()

    print("\n2. Faylga yozish va o'qish:")
    write_read_example()

    print("\n3. Faylga davomiy yozish:")
    append_example()

    print("\n4. CSV fayllar bilan ishlash:")
    csv_example()

    print("\n5. JSON fayllar bilan ishlash:")
    json_example()

    print("\n6. Fayllarni o'chirish:")
    delete_file_example()

    print("\n7. Xatoliklarni boshqarish:")
    error_handling_example()

    print("\n8. Binariy fayllar bilan ishlash:")
    binary_file_example()
