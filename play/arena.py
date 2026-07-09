import time
import random

def start_tournament(monster1, monster2):
    print(f"ЛАСКАВО ПРОСИМО НА ВЕЛИКУ АРЕНУ!")
    print(f"Сьогодні б'ються: {monster1.name} проти {monster2.name}!")

    time.sleep(2)

    round_num = 1

    while monster1.is_alive() and monster2.is_alive():
        print(f" РАУНД {round_num} ")
        print(f"[{monster1.name}: {monster1.hp} HP] vs [{monster2.name}: {monster2.hp} HP]")
        print("-" * 30)
        
        time.sleep(1)  

        attacker, defender = random.sample([monster1, monster2], 2)
        if hasattr(attacker, 'ragnarok') and random.random() < 0.3:
                attacker.ragnarok()
        else:
                attacker.attack(defender)
    print("")

    round_num += 1
    time.sleep(1.5)

    if monster1.is_alive():
        print(f"ПЕРЕМОЖЕЦЬ: {monster1.name}!")
    else:
        print(f"ПЕРЕМОЖЕЦЬ: {monster2.name}!")