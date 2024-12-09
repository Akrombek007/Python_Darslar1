# Mavzu: Imtihon va Mustaqil Ishlar
# Testlar va amaliy topshiriqlar. Kichik loyihalarni taqdim qilish.

import random
import json
from typing import List, Dict, Any


# 1. Test savollarini yaratish va tasodifiy tanlash
class Test:
    def __init__(self, name: str, questions: List[str]):
        self.name = name
        self.questions = questions

    def get_random_questions(self, num: int = 5) -> List[str]:
        """Testdan tasodifiy savollarni tanlash."""
        return random.sample(self.questions, num)


# Test misoli
questions = [
    "Python dasturlash tili nima?",
    "Foydalanuvchi kiritgan ma'lumotni qanday qabul qilasiz?",
    "Pythonni kim ishlab chiqqan?",
    "Pythonning eng yaxshi xususiyatlari nima?",
    "List va Tuple farqi nima?"
]

test = Test(name="Python Test", questions=questions)


# 2. Imtihon javoblarini saqlash
class ExamResult:
    def __init__(self, user_id: int, answers: Dict[int, str]):
        self.user_id = user_id
        self.answers = answers
        self.correct_answers = 0

    def evaluate(self, correct_answers: Dict[int, str]):
        """Javoblarni baholash."""
        self.correct_answers = sum(1 for qid, answer in self.answers.items() if correct_answers.get(qid) == answer)
        return self.correct_answers


# Imtihon uchun to'g'ri javoblar
correct_answers = {
    1: "Python",
    2: "input()",
    3: "Guido van Rossum",
    4: "Kengaytirilgan kutubxonalar",
    5: "List mutatsiyalanuvchi, Tuple esa o'zgarmas"
}


# 3. Test savollarini chiqarish va foydalanuvchidan javoblarni olish
def conduct_exam(test: Test, user_id: int):
    """Imtihon o'tkazish."""
    random_questions = test.get_random_questions()
    print(f"Test: {test.name}\n")

    answers = {}
    for i, question in enumerate(random_questions, 1):
        print(f"Savol {i}: {question}")
        answer = input("Javobni kiriting: ")
        answers[i] = answer

    result = ExamResult(user_id, answers)
    score = result.evaluate(correct_answers)
    print(f"\nImtihon yakuni: {score} ta to'g'ri javob")


# 4. Mustaqil ish uchun topshiriq yaratish
class Assignment:
    def __init__(self, title: str, description: str, max_points: int):
        self.title = title
        self.description = description
        self.max_points = max_points

    def submit(self, user_id: int, submission: str):
        """Mustaqil ishni topshirish."""
        print(f"Mustaqil ish: {self.title}")
        print(f"Ta'rif: {self.description}")
        print(f"Maxsus ball: {self.max_points}")
        print(f"Foydalanuvchi {user_id} topshiriqni quyidagi tarzda taqdim etdi:\n{submission}")


# Mustaqil ish
assignment = Assignment(
    title="Python dasturlash bo'yicha loyiha",
    description="Foydalanuvchi Python dasturlash tilida oddiy kalkulyator dasturini yaratishi kerak.",
    max_points=100
)


# 5. Mustaqil ishni baholash
def grade_assignment(submission: str, max_points: int) -> int:
    """Mustaqil ishni baholash."""
    if "def" in submission and "return" in submission:
        score = max_points
    else:
        score = max_points // 2
    return score


# 6. Imtihonlar va mustaqil ishlarni izlash
def search_tests(tests: List[Test], keyword: str) -> List[Test]:
    """Testlarni kalit so'z orqali qidirish."""
    return [test for test in tests if keyword.lower() in test.name.lower()]


# 7. Test natijalarini saqlash
def save_exam_result(user_id: int, score: int) -> None:
    """Test natijasini faylga saqlash."""
    result_data = {
        "user_id": user_id,
        "score": score,
        "timestamp": "2024-12-09"
    }
    with open("exam_results.json", "a") as file:
        json.dump(result_data, file)
        file.write("\n")


# 8. Foydalanuvchining test natijalarini ko'rish
def view_results(user_id: int) -> None:
    """Foydalanuvchining test natijalarini ko'rish."""
    try:
        with open("exam_results.json", "r") as file:
            results = file.readlines()
            for result in results:
                result_data = json.loads(result)
                if result_data["user_id"] == user_id:
                    print(f"Foydalanuvchi {user_id} natijasi: {result_data['score']} ball")
    except FileNotFoundError:
        print("Natijalar mavjud emas.")


# 9. Testni qayta topshirish
def retake_exam(test: Test, user_id: int):
    """Testni qayta topshirish."""
    if input("Testni qayta topshirasizmi? (ha/yo'q): ").lower() == "ha":
        conduct_exam(test, user_id)
    else:
        print("Testni qayta topshirmadi.")


# 10. Kichik loyiha yaratish (oddiy kalkulyator)
def simple_calculator():
    """Oddiy kalkulyator dasturi."""
    print("Kalkulyator: +, -, *, / amallaridan foydalaning.")
    num1 = float(input("Birinchi raqamni kiriting: "))
    operator = input("Amalni kiriting (+, -, *, /): ")
    num2 = float(input("Ikkinchi raqamni kiriting: "))

    if operator == "+":
        print(f"Natija: {num1 + num2}")
    elif operator == "-":
        print(f"Natija: {num1 - num2}")
    elif operator == "*":
        print(f"Natija: {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"Natija: {num1 / num2}")
        else:
            print("0 ga bo'lish mumkin emas.")
    else:
        print("Noto'g'ri amal.")


# 11. Mustaqil ish natijalarini saqlash
def save_assignment_result(user_id: int, score: int) -> None:
    """Mustaqil ish natijasini saqlash."""
    result_data = {
        "user_id": user_id,
        "score": score,
        "timestamp": "2024-12-09"
    }
    with open("assignment_results.json", "a") as file:
        json.dump(result_data, file)
        file.write("\n")


# 12. Loyiha tayyorlash va baholash
def project_submission(user_id: int, project_code: str):
    """Loyihani topshirish va baholash."""
    print(f"Loyiha foydalanuvchi {user_id} tomonidan topshirildi.")
    grade = grade_assignment(project_code, 100)
    print(f"Loyihangiz {grade} ball olgan.")


# **Asosiy dastur uchun misollar**

# Test o'tkazish
conduct_exam(test, 1)

# Mustaqil ish topshirish
assignment.submit(1, "Python kodini yozish")

# Mustaqil ishni baholash
score = grade_assignment("def add(a, b): return a + b", 100)
print(f"Mustaqil ish balli: {score}")

# Test natijasini saqlash
save_exam_result(1, 4)

# Test natijalarini ko'rish
view_results(1)

# Testni qayta topshirish
retake_exam(test, 1)

# Kalkulyator dasturi
simple_calculator()

# Loyiha topshirish
project_submission(1, "def add(a, b): return a + b")

# Mustaqil ish natijasini saqlash
save_assignment_result(1, 90)
