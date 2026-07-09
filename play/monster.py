import random
class Monster:
    def __init__(self, name, hp, damage, agility):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.agility = agility
            
    def attack(self, other):
        crit = random.choice([1, 1, 1, 1.5, 2])
        final_damage = int(self.damage * crit)

        def monster_agility(final_damage):
            chaice = random.randint(1, 100)
            if chaice <= self.agility:
                final_damage = 0
                hp = other.hp
                hp -= final_damage
                other.hp = hp
                print(f"{other.name} ухилився.")
                
            else:
                hp = other.hp
                hp -= final_damage
                other.hp = hp
                print ("lol")
                if crit > 1:
                    print(f"критичний удар! {self.name} розлютився!")
                print(f"{self.name} завдає{final_damage} шкоди для{other.name}.")

        monster_agility(final_damage)

    def is_alive(self):
        return self.hp > 0

class Golem(Monster):
    def __init__(self, name, hp, damage, shield, agility):
        super().__init__(name, hp, damage, agility)
        self.shield = shield

        
    def attack(self, other):
        print(f"{self.name} замах")
        super().attack(other)

class dragon(Monster):
    def __init__(self, name, hp, damage, agility):
        super().__init__(name, hp, damage, agility)

    def attack(self, other):
        print(f"{self.name} плює вогнем")
        super().attack(other)

    def ragnarok(self):
        heal_amount = 20
        self.hp += heal_amount
        print(f"{self.name} поглинає вогонь і відновлює{heal_amount} HP!")