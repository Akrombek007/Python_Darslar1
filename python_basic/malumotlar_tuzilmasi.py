# Ma'lumot Tuzilmalari Qo'llanmasi

# === 1. Listlar (list): yaratish, o'zgartirish, element qo'shish va o'chirish ===
# Listlar - ketma-ket tartiblangan va o'zgaruvchan ma'lumotlar tuzilmasi.
# Foydalanish holati: Ma'lumotlar tartibini saqlash va ularga indeks orqali murojaat qilish kerak bo'lganda.

# Misol 1: List yaratish
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Misol 2: Listga element qo'shish
my_list.append(6)
print("After Append:", my_list)

# Misol 3: Listga o'rtaga element qo'shish
my_list.insert(2, 10)  # 2-indeksga 10 ni qo'shish
print("After Insert:", my_list)

# Misol 4: Listdan element o'chirish
my_list.remove(10)  # Qiymat asosida o'chirish
print("After Remove:", my_list)

# Misol 5: Indeks asosida o'chirish
deleted = my_list.pop(3)  # 3-indeksdagi elementni olib tashlash
print("After Pop:", my_list, "| Deleted Element:", deleted)

# Misol 6: Listni qayta tartibga solish
my_list.sort(reverse=True)  # Kamayish tartibida
print("Sorted List:", my_list)

# Misol 7: Elementlarni sanash
count = my_list.count(2)
print("Count of 2:", count)

# Misol 8: Listni tozalash
my_list.clear()
print("Cleared List:", my_list)

# === 2. Tuple (tuple): o'zgarmas ro'yxatlar ===
# Tuple - o'zgarmas va tartibli ma'lumotlar tuzilmasi.
# Foydalanish holati: O'zgarmas va tartibni saqlaydigan ma'lumotlar kerak bo'lganda.

# Misol 1: Tuple yaratish
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Misol 2: Tuple elementlariga kirish
print("First Element:", my_tuple[0])

# Misol 3: Tupleni birlashtirish
new_tuple = my_tuple + (6, 7, 8)
print("Merged Tuple:", new_tuple)

# Misol 4: Tupleni qayta yaratish
my_tuple = (10,) + my_tuple[1:]
print("Modified Tuple:", my_tuple)

# Misol 5: Tuple ichida tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested_tuple)

# Misol 6: Tupleda elementlarni sanash
count = my_tuple.count(2)
print("Count of 2 in Tuple:", count)

# Misol 7: Tuple uzunligini olish
print("Length of Tuple:", len(my_tuple))

# Misol 8: Tupledan o'zgarmas ma'lumotlar bilan ishlash
coordinates = (40.7128, 74.0060)  # New York koordinatalari
print("Coordinates:", coordinates)

# === 3. Lug'atlar (dict): kalit-qiymat juftliklari bilan ishlash ===
# Lug'atlar - kalit-qiymat asosida ma'lumotlarni saqlash uchun.
# Foydalanish holati: Indeks emas, balki kalit asosida murojaat qilish kerak bo'lganda.

# Misol 1: Lug'at yaratish
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", my_dict)

# Misol 2: Lug'atga yangi juftlik qo'shish
my_dict["job"] = "Engineer"
print("After Adding Key-Value:", my_dict)

# Misol 3: Lug'atdagi qiymatni yangilash
my_dict["age"] = 26
print("After Updating Value:", my_dict)

# Misol 4: Lug'atdan qiymatni olish
age = my_dict.get("age")
print("Age:", age)

# Misol 5: Kalitni o'chirish
del my_dict["city"]
print("After Deleting Key:", my_dict)

# Misol 6: Barcha kalitlarni olish
keys = list(my_dict.keys())
print("Keys:", keys)

# Misol 7: Barcha qiymatlarni olish
values = list(my_dict.values())
print("Values:", values)

# Misol 8: Kalit-qiymat juftliklarini ko'rish
items = list(my_dict.items())
print("Items:", items)

# === 4. To'plamlar (set): noyob elementlar ===
# To'plamlar - tartibsiz va takrorlanuvchi bo'lmagan elementlarni saqlash uchun.
# Foydalanish holati: Noyob elementlarni topish yoki to'plam operatsiyalari kerak bo'lganda.

# Misol 1: To'plam yaratish
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Misol 2: To'plamga element qo'shish
my_set.add(6)
print("After Adding Element:", my_set)

# Misol 3: To'plamdan element o'chirish
my_set.discard(3)
print("After Discarding Element:", my_set)

# Misol 4: Birlashtirish (Union)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print("Union:", union_set)

# Misol 5: Kesish (Intersection)
intersection_set = set_a & set_b
print("Intersection:", intersection_set)

# Misol 6: Farq (Difference)
difference_set = set_a - set_b
print("Difference:", difference_set)

# Misol 7: Simmetrik farq (Symmetric Difference)
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference:", symmetric_difference_set)

# Misol 8: Takrorlanuvchi elementlarni olib tashlash
repeated_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(repeated_list)
print("Unique Elements:", unique_elements)
