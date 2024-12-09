# istisnolarni qayta ishlash.py

# 1. Umumiy try-except bloklari

# 1.1. ZeroDivisionError: nolga bo'lish
def divide_by_zero():
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        print(f"Xatolik yuz berdi: {e}")


# 1.2. ValueError: noto'g'ri ma'lumot turi
def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        print(f"Xatolik yuz berdi: {e}")


# 2. Istisnolarni qayta ishlash va resurslarni tozalash uchun 'finally' bloki
def file_operations():
    try:
        file = open("example.txt", "r")
        data = file.read()
        print(data)
    except FileNotFoundError as e:
        print(f"Fayl topilmadi: {e}")
    finally:
        try:
            file.close()
        except NameError:
            pass
        print("Resurslar tozalandi!")


# 3. Maxsus istisnolarni yaratish
class CustomError(Exception):
    """Maxsus xato sinfi"""
    pass


def raise_custom_error():
    try:
        raise CustomError("Bu maxsus xato!")
    except CustomError as e:
        print(f"Maxsus xato: {e}")


# 4. Multiple except bloklari
def multiple_exceptions(value):
    try:
        if value == "zero":
            return 10 / 0
        elif value == "string":
            return int("not a number")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")


# 5. Try except bloklarida else bo'limi
def check_value(value):
    try:
        return int(value)
    except ValueError as e:
        print(f"ValueError: {e}")
    else:
        print(f"Success: {value} an integer.")


# 6. Custom exception handling in a specific situation (value out of range)
class OutOfRangeError(Exception):
    """Maxsus xato: qiymat oralig'ida emas"""
    pass


def check_range(value):
    if value < 0 or value > 100:
        raise OutOfRangeError("Qiymat 0 dan 100 gacha bo'lishi kerak!")
    else:
        print(f"Qiymat: {value} yaroqli.")


# 7. Istisnolarni qayta ishlashda logging dan foydalanish
import logging

logging.basicConfig(level=logging.INFO)


def log_exception():
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        logging.error(f"Xatolik yuz berdi: {e}")
        print("Xatolikni qayd ettik.")


# 8. Exception chaining (Istisnolarni zanjirlash)
def chain_exceptions():
    try:
        try:
            return 10 / 0
        except ZeroDivisionError as e:
            raise ValueError("Qiymat noto'g'ri bo'ldi.") from e
    except ValueError as e:
        print(f"Xato zanjiri: {e}")


# 9. Try-except-da o'zgaruvchi bo'yicha tekshirish
def check_for_type(value):
    try:
        if not isinstance(value, int):
            raise TypeError("Foydalanuvchi integer kiritishi kerak.")
        return value * 2
    except TypeError as e:
        print(f"Xatolik: {e}")


# 10. Istisnolarni qayta ishlashda xatoliklarni yig'ish
def collect_exceptions(value):
    errors = []
    try:
        if value == "zero":
            10 / 0
    except ZeroDivisionError as e:
        errors.append(f"ZeroDivisionError: {e}")

    try:
        if value == "string":
            int("not a number")
    except ValueError as e:
        errors.append(f"ValueError: {e}")

    if errors:
        for error in errors:
            print(error)


# Quyidagi misollarni bajarish:
if __name__ == "__main__":
    print("1. Umumiy Try-Except Bloklari:")
    divide_by_zero()  # ZeroDivisionError
    convert_to_int("abc")  # ValueError

    print("\n2. Resurslarni tozalash (finally):")
    file_operations()

    print("\n3. Maxsus Xato (Custom Error):")
    raise_custom_error()

    print("\n4. Bir nechta except bloklari:")
    multiple_exceptions("zero")  # ZeroDivisionError
    multiple_exceptions("string")  # ValueError

    print("\n5. Else bo'limi:")
    check_value("123")  # Success
    check_value("abc")  # ValueError

    print("\n6. Maxsus diapazon tekshiruvi:")
    check_range(150)  # OutOfRangeError

    print("\n7. Logging bilan istisnolarni qayd etish:")
    log_exception()

    print("\n8. Istisnolarni zanjirlash:")
    chain_exceptions()

    print("\n9. O'zgaruvchi turini tekshirish:")
    check_for_type("hello")  # TypeError
    check_for_type(10)  # No error

    print("\n10. Xatoliklarni yig'ish:")
    collect_exceptions("zero")
    collect_exceptions("string")
