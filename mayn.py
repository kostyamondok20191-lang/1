import time
from questions import QUIZ_DATA

print("ЛАСКАВО ПРОСИМО ДО ІНТЕЛЕКТ-КВІЗУ")
print("Перед вами 10 питань. Натискайте А, Б, В або Г для відповіді.")
print("Починаємо через 2 години")
time.sleep(1)

total_score = 0
score = 0
total_questions = len(QUIZ_DATA)
for index, item in enumerate(QUIZ_DATA):
    print(f"\n Питання №{index + 1}: {item.get("question")}")
    for option in item["options"]:
        print(f"  {option}")
    user_answer = input("\nВаша відповідь (А, Б, В, Г): ").strip().upper()
    if user_answer == item.get("answer"):
        print(" Правильно! + ", item.get("skore"), " бал")
        score += item.get("skore")
        total_score += item.get("skore")

    else:
        print(f" Неправильно. Правильна відповідь: {item.get("answer")}")
        total_score += item.get("skore")

    time.sleep(2)

print("РЕЗУЛЬТАТИ ТЕСТУВАННЯ")
print(f"• Балів: {score} з {total_score}")

success_rate = (score / total_score) * 100
print (success_rate)