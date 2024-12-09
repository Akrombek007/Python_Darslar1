# lambda.py

# 1. Lambda funksiyasi asoslari
# Lambda funksiyasi - bu qisqacha yozilgan, nomlanmagan funksiya.
# Lambda funksiyasi o'zida bir nechta ifodalardan faqat bitta ifodani o'z ichiga oladi.
# Lambda funksiyasi quyidagi formatda ishlaydi:
# lambda x: x + 1 - bu yerda x - kirish argumenti va x + 1 - bu funksiyaning bajariladigan aksi.

print("1. Lambda funktsiyasi asoslari:")
add_one = lambda x: x + 1  # x ga 1 qo'shadi
print(add_one(5))  # Natija: 6

# 2. Lambda funksiyasi yordamida ikki sonni qo'shish
# Lambda funksiyasi ikki sonni qo'shish uchun ham ishlatilishi mumkin.
print("\n2. Lambda funktsiyasi yordamida ikki sonni qo'shish:")
add_two_numbers = lambda x, y: x + y  # Ikki sonni qo'shish
print(add_two_numbers(3, 4))  # Natija: 7

# 3. Lambda va map funksiyasi
# map() funksiyasi yordamida lambda funksiyasi ro'yxatdagi har bir elementga qo'llanadi.
# map() lambda funksiyasining har bir elementga o'zgartirishlar kiritishini amalga oshiradi.
print("\n3. Lambda va map funksiyasi:")
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Ro'yxatdagi har bir sonni kvadratga oshirish
print(squared_numbers)  # Natija: [1, 4, 9, 16, 25]

# 4. Lambda va filter funksiyasi
# filter() funksiyasi lambda yordamida ro'yxatdagi ma'lum bir shartga javob beruvchi elementlarni tanlab olish uchun ishlatiladi.
print("\n4. Lambda va filter funksiyasi:")
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Faqat juft sonlarni olish
print(even_numbers)  # Natija: [2, 4]

# 5. Lambda va reduce funksiyasi
# reduce() funksiyasi lambda yordamida ro'yxatdagi barcha elementlar ustida to'plama operatsiyasini bajaradi.
from functools import reduce

print("\n5. Lambda va reduce funksiyasi:")
sum_of_numbers = reduce(lambda x, y: x + y, numbers)  # Ro'yxatdagi barcha sonlarni qo'shish
print(sum_of_numbers)  # Natija: 15

# 6. Lambda bilan max va min funksiyalari
# max() va min() funksiyalari lambda yordamida ro'yxatdagi eng katta yoki eng kichik elementlarni topadi.
print("\n6. Lambda bilan max va min funksiyalari:")
max_number = max(numbers, key=lambda x: x)  # Ro'yxatdagi eng katta sonni topish
min_number = min(numbers, key=lambda x: x)  # Ro'yxatdagi eng kichik sonni topish
print(f"Max: {max_number}, Min: {min_number}")  # Natija: Max: 5, Min: 1

# 7. Lambda funksiyasini key argumenti bilan ishlatish
# key argumenti bilan lambda funksiyasi, masalan, ro'yxatni tartiblashda ishlatiladi.
print("\n7. Lambda funksiyasini key argumenti bilan ishlatish:")
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))  # So'zlarni uzunlikka qarab tartiblash
print(sorted_words)  # Natija: ['date', 'apple', 'banana', 'cherry']

# 8. Lambda va shartli ifoda (ternary operator)
# Lambda funksiyasi shartli ifoda bilan ham ishlatiladi. Bu usul oddiy if else konstruktsiyasini qisqartiradi.
print("\n8. Lambda va shartli ifoda:")
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(10))  # Natija: Even
print(is_even(7))  # Natija: Odd

# 9. Lambda bilan list comprehension
# Lambda funksiyasi list comprehension yordamida ro'yxatlarni tezda yaratishda ishlatilishi mumkin.
print("\n9. Lambda bilan list comprehension:")
doubled_numbers = [lambda x: x * 2 for x in numbers]  # Ro'yxatdagi har bir sonni ikki baravarga oshirish
doubled_numbers_result = [f(1) for f in doubled_numbers]  # Har bir lambda funksiyasini chaqirish
print(doubled_numbers_result)  # Natija: [2, 4, 6, 8, 10]

# 10. Lambda va dictionaries
# Lambda funksiyasi dictionaries (lug'atlar) bilan ishlashda ham foydalidir, masalan, qiymatlar bo'yicha saralashda.
print("\n10. Lambda va dictionaries:")
d = {"a": 3, "b": 1, "c": 2}
sorted_dict = sorted(d.items(), key=lambda x: x[1])  # Dictionary elementlarini qiymatga qarab tartiblash
print(sorted_dict)  # Natija: [('b', 1), ('c', 2), ('a', 3)]

# 11. Lambda va multiple arguments
# Lambda funksiyasi bir nechta argument bilan ishlashi mumkin, bu esa uni murakkabroq operatsiyalar uchun qulay qiladi.
print("\n11. Lambda va multiple arguments:")
multiply = lambda x, y, z: x * y * z  # Uchta argumentni ko'paytirish
print(multiply(2, 3, 4))  # Natija: 24

# 12. Lambda va funktsiyalarni qaytarish
# Lambda funksiyalari boshqa funksiyalar tomonidan qaytarilishi mumkin.
print("\n12. Lambda va funktsiyalarni qaytarish:")


def make_multiplier(n):
    return lambda x: x * n


multiply_by_3 = make_multiplier(3)  # 3 ga ko'paytiruvchi funksiya yaratish
print(multiply_by_3(5))  # Natija: 15
