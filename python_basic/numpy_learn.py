import numpy as np
import pandas as pd

# 1. Numpy - NumPy array yaratish va asosiy operatsiyalar
# Numpy massivlari (arrays) bilan ishlash
# Misol: 1 o'lchovli massiv yaratish
arr = np.array([1, 2, 3, 4, 5])
print("1. Numpy 1D Massiv:")
print(arr)
print("Massivning shakli:", arr.shape)  # Shakli (dimensiya) haqida ma'lumot

# 2. Numpy - 2 o'lchovli massiv yaratish
# Misol: 2 o'lchovli massiv (matritsa)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2. Numpy 2D Massiv (Matritsa):")
print(matrix)
print("Matritsaning shakli:", matrix.shape)

# 3. Numpy - Array elementlariga arifmetik amallar
# Misol: Massiv elementlarini qo'shish, ko'paytirish
arr2 = np.array([10, 20, 30, 40, 50])
sum_arr = arr + arr2  # Massivlar qo'shilishi
print("\n3. Massivlarni qo'shish:")
print(sum_arr)

# 4. Numpy - Array slicing (Kesish)
# Misol: Array dan qismini olish
sliced_arr = arr[1:4]  # 1-chi elementdan 4-chi elementgacha
print("\n4. Numpy Array kesish:")
print(sliced_arr)

# 5. Numpy - Elementlarni tartibga solish
# Misol: Arrayni tartibga solish
arr3 = np.array([5, 2, 8, 1, 4])
sorted_arr = np.sort(arr3)
print("\n5. Numpy Arrayni tartibga solish:")
print(sorted_arr)

# 6. Pandas - DataFrame yaratish
# Misol: DataFrame yaratish
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("\n6. Pandas DataFrame:")
print(df)

# 7. Pandas - DataFrame dan specific columnni olish
# Misol: DataFrame dan bitta ustunni olish
age_column = df['Age']
print("\n7. Pandas DataFrame ustunini olish:")
print(age_column)

# 8. Pandas - Ma'lumotlarni filtrlash
# Misol: DataFrame ni shartli filtr bilan tanlash
filtered_df = df[df['Age'] > 25]  # Yosh 25 dan katta bo'lganlarni tanlash
print("\n8. Pandas DataFrame filtrlash:")
print(filtered_df)

# 9. Pandas - Qator va ustunlarni tanlash
# Misol: DataFrame da maxsus qator va ustunni tanlash
specific_row = df.iloc[1]  # 1-chi qatorni olish (index 0-dan boshlanadi)
specific_column = df.iloc[:, 1]  # 1-chi ustunni olish
print("\n9. Pandas DataFrame dan maxsus qator va ustun:")
print("Maxsus qator:", specific_row)
print("Maxsus ustun:", specific_column)

# 10. Pandas - DataFrame ustunini qo'shish
# Misol: DataFrame ga yangi ustun qo'shish
df['Salary'] = [1000, 1500, 2000, 2500]
print("\n10. Pandas DataFrame ustunini qo'shish:")
print(df)

# 11. Pandas - DataFrame ni teskari tartibda saralash
# Misol: DataFrame ni teskari tartibda saralash
df_sorted = df.sort_values(by='Age', ascending=False)
print("\n11. Pandas DataFrame ni teskari tartibda saralash:")
print(df_sorted)

# 12. Numpy va Pandas birgalikda ishlash
# Misol: Pandas DataFramega NumPy array bilan ustun qo'shish
arr4 = np.array([5, 10, 15, 20])
df['Score'] = arr4  # Numpy arrayni pandas DataFramega qo'shish
print("\n12. Numpy va Pandas birgalikda ishlash:")
print(df)

# Bonus - Ma'lumotlarni CSV faylga saqlash va o'qish
# Misol: DataFrame ni CSV formatida saqlash va qayta o'qish
df.to_csv('students.csv', index=False)
read_df = pd.read_csv('students.csv')
print("\nBonus: CSV faylga saqlash va qayta o'qish:")
print(read_df)
