import random
class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, other):
        crit = random.choice([1, 1, 1, 1.5, 2])
        final_damage = int(self.damage * crit)

        other.hp -= final_damage
        if crit > 1:
            print(f"критичний удар! {self.name} розлютився!")
        print("{self.name}завдає{final_damage}шкоди для{other.name}.")
    def is_alvive(self):
        return self.hp > 0

class Golem(Monster):
    def __init__(self, name, hp, damage, shield):
        super().__init__(name, hp, damage)
        self.shield = shield

    def attack(self, other):
        print("{self.name}замах")
        super().attack(other)

class dragon(Monster):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
    def attack(self, other):
        print("{self.name}плює вогнем")
        super().attack(other)

    def ragnarok(self):
        heal_amount = 20
        self.hp += heal_amount
        print(f"{self.name}поглинає вогонь і відновлює{heal_amount}РЗ!")