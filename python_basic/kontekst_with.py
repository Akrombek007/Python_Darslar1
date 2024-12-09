# context_manager_examples.py

# 1. Asosiy Kontekst Menejeri

# Kontekst menejeri - bu resurslarni boshqarish uchun ishlatiladigan konstruktsiya
# Bu resursni olish va uni ishlatib bo'lgach, tozalashni avtomatik ravishda amalga oshiradi.

# Misol: Faylni o'qish uchun context manager
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)


# Bu yerda 'open' context manageri faylni ochadi va 'with' blokidan chiqilganda fayl avtomatik tarzda yopiladi.
# 'with' operatori bilan ishlash faylni o'qib bo'lgach resursni tozalashni osonlashtiradi.

# 2. Kendi Kontekst Menejeri Yaratish

# Biz o'zimizga moslashtirilgan kontekst menejerini yaratishimiz mumkin.
# Buning uchun __enter__ va __exit__ metodlarini o'z ichiga olgan sinf yaratishimiz kerak.

class MyContextManager:
    def __enter__(self):
        print("Resurs ochildi.")
        return self  # Bu yerda biz o'zimiz ishlatmoqchi bo'lgan obyektni qaytarishimiz mumkin

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resurs yopildi.")
        if exc_type:
            print(f"Xatolik yuz berdi: {exc_value}")
        return True  # Agar 'True' qaytarsak, xato ishlov berilmaydi (xatolikni yutish)


# Kontekst menejeri ishlatilgan holat
with MyContextManager() as cm:
    print("Resurs bilan ishlayapman.")

# 3. Faylni Yopishda Xatoliklarni Boshqarish

# Kontekst menejeri yordamida faylni o'qish va xatoliklarni boshqarish
try:
    with open('missing_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Fayl topilmadi!")


# 4. Kontekst Menejeri bilan Ma'lumotlar Bazasiga ulanish

# Bu yerda kontekst menejerini ma'lumotlar bazasiga ulanish uchun ishlatamiz.
class DatabaseConnection:
    def __enter__(self):
        print("Ma'lumotlar bazasiga ulanish...")
        # Bu yerda ulanish kodlarini yozish mumkin
        self.connection = "Database Connection"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("Ma'lumotlar bazasidan uzilish...")
        # Bu yerda uzilish kodlarini yozish mumkin
        self.connection = None


with DatabaseConnection() as db:
    print(f"Ulangan: {db}")

# 5. Kontekst Menejeri bilan Faylga Yozish

# Kontekst menejeri yordamida faylga ma'lumot yozish
with open('output.txt', 'w') as file:
    file.write("Bu yangi yozilgan ma'lumot.")


# 6. Resursni Avtomatik Tozalash

# Agar resursni ishlatganingizdan so'ng tozalashni unutsangiz, context manager buni avtomatik bajaradi.
class ResourceHandler:
    def __enter__(self):
        print("Resursni olib, foydalanish uchun ochyapman.")
        self.resource = "Some Resource"
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resursni tozalayapman.")
        self.resource = None


# Context menejeri resursni boshqaradi va avtomatik ravishda tozalashni ta'minlaydi
with ResourceHandler() as resource:
    print(f"Resurs bilan ishlash: {resource}")


# 7. Xatoliklarni Boshqarish

# Xatolikni boshqarish va unga tegishli javob berish
class ErrorHandlingManager:
    def __enter__(self):
        print("Xatolikni boshqarish boshlandi.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Xatolik yuz berdi: {exc_value}")
            return True  # Bu yerda xatolikni yutamiz
        print("Xatolik yo'q, yakunlanmoqda.")
        return False  # Xatolikni qaytarmaslik uchun False


# Context menejeri yordamida xatolikni boshqarish
with ErrorHandlingManager():
    print("Xatolik yuz berishi mumkin.")
    raise ValueError("Bu xatolik!")


# 8. O'zgaruvchilarni Tozalash

# O'zgaruvchilarni tozalash va ularni to'g'ri boshqarish
class VariableCleaner:
    def __enter__(self):
        print("O'zgaruvchilarni tozalash boshlanmoqda.")
        self.variable = "Some data"
        return self.variable

    def __exit__(self, exc_type, exc_value, traceback):
        print("O'zgaruvchilarni tozalash yakunlandi.")
        self.variable = None  # O'zgaruvchi tozalanadi


with VariableCleaner() as variable:
    print(f"O'zgaruvchi ishlatilmoqda: {variable}")


# 9. Tarmoq Ulanishlarini Boshqarish

# Tarmoq ulanishlarini boshqarishda ham kontekt menejerlari juda foydali.
class NetworkConnection:
    def __enter__(self):
        print("Tarmoqga ulanish...")
        self.connection = "Network Connection"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("Tarmoqdan uzilish...")
        self.connection = None


# Tarmoq ulanishi bilan ishlash
with NetworkConnection() as network:
    print(f"Tarmoq ulanishi: {network}")


# 10. Hujjatni Biriktirish va Yuborish

# Fayllarni biriktirish va yuborish uchun kontekst menejeridan foydalanish
class DocumentHandler:
    def __enter__(self):
        print("Hujjatni ochish...")
        self.document = "Document Content"
        return self.document

    def __exit__(self, exc_type, exc_value, traceback):
        print("Hujjatni yopish...")
        self.document = None


with DocumentHandler() as doc:
    print(f"Hujjat bilan ishlash: {doc}")


# 11. Funksiyalarni Tozalash

# Kontekst menejeri yordamida funksiyani boshqarish
class FunctionCleaner:
    def __enter__(self):
        print("Funksiya ishga tushdi.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Funksiya yakunlandi.")


with FunctionCleaner():
    print("Funksiya ishlamoqda.")

# 12. Faylni Yozishni Sinovdan O'tkazish

# Faylga ma'lumot yozish va sinovdan o'tkazish
with open('test.txt', 'w') as file:
    file.write("Sinov fayli uchun ma'lumot.")

print("Faylga yozish yakunlandi.")
