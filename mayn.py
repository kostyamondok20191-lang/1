import random
import time
from questions import QUIZ_DATA

questions_pool = QUIZ_DATA[:]

print("ЛАСКАВО ПРОСИМО ДО ІНТЕЛЕКТ-КВІЗУ")
print("Перед вами 10 питань. Натискайте А, Б, В або Г для відповіді.")
hours, minutes, second = map(int, input("Введіть час: год, хв, с (через пробіл.)").split())
final_time = (hours * 3600 + minutes * 60 + second)
time.sleep(hours * 3600 + minutes * 60 + second)

total_score = 0
score = 0

while len(questions_pool) > 0:
    random_index = random.randint(0, len(questions_pool) - 1)
    item = questions_pool.pop(random_index)
    print(f"\n Питання: {item.get('question') or item.get('qestion')}")
    for option in item["options"]:
        print(f"  {option}")
    user_answer = input("\nВаша відповідь (А, Б, В, Г): ").strip().upper()
    correct_answer = item.get("answer") or item.get("ansver")
    if user_answer == correct_answer:
        print(" Правильно! + ", item.get("skore"), " бал")
        score += item.get("skore")
    else:
        print(f" Неправильно. Правильна відповідь: {correct_answer}")
    total_score += item.get("skore")
    time.sleep(1)

print(f"\nРЕЗУЛЬТАТ: {score} з {total_score} балів.")
print(score / total_score * 100)