import random
import time


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0
        self.skill = None

    def create_hero(name, race, prof):
        hp = 0
        damage = 0
        name = name
        if race == race_list[0]:
            hp += 200
            damage += 60
        elif race == race_list[1]:
            hp += 200
            damage += 60
        elif race == race_list[2]:
            hp += 200
            damage += 60
        elif race == race_list[3]:
            hp += 200
            damage += 60
        else:
            print("Такой расы нет")
            quit()
        if prof == prof_list[0]:
            hp += 10
            damage -= 20
        elif prof == prof_list[1]:
            hp += 30
            damage -= 40
        elif prof == prof_list[2]:
            hp += 100
            damage += 20
        elif prof == prof_list[3]:
            hp += 230
            damage += 90
        else:
            print("такой профессии нет")
            quit()
        return Player(name, hp, damage)

    def levelup(self, max_exp):
        self.exp -= max_exp
        self.lvl += 1
        self.damage += self.lvl * 5
        self.hp += self.lvl * 10
        print(f"{self.name}, поздравляю с повышением уровня! Уровень:{self.lvl}")


    def ability(self):
        if self.skill == "Замораживание":
            print("Вы заморозили монстра! Теперь он не"
                  "атакует тебя")
            enemy.damage = 0
        elif self.skill == "Отравление":
            print("Вы отравили монстра в этой схватке,"
                  "-10 здоровья у врага!")
            enemy.hp -= 10

        elif self.skill == "Лечение":
            print("Твоё оружие вылечило тебя. + 10 здоровья")
            self.hp += 10

    def attack(self, victim):
        max_exp = self.lvl * 100
        rnd_attack = random.randint(1, 5)
        if rnd_attack == 1:
            print("Вы наносите двойной урон!")
            victim.hp -= self.damage * 2
        elif rnd_attack == 2 or rnd_attack == 3 or rnd_attack == 4:
            victim.hp -= self.damage
        elif rnd_attack == 5:
            print("Вы промазали")
        if victim.hp <= 0:
            print(f"Монстр по имени {victim.name} повержен! вы получили 20 опыта ")
            thing = random.randint(0, 1)
            if thing == 0:
                weapon = self.create_weapon()
                print(f"вам выпало {weapon[1]} оружие: {weapon[0]}")
            elif thing == 1:
                print("Вам не выпало оружие")
            self.exp += 20
            if self.exp >= max_exp:
                self.levelup(max_exp)
            thing_1 = random.randint(0, 1)
            if thing_1 == 0:
                armor = self.create_armor()
                print(f"Вам выпала {armor[1]} броня: {armor[0]}")
            elif thing_1 == 1:
                print("Вам не выпала броня")
            self.skill = random.choice(powers_list)
            print(f"Теперь вы одарены способностью: {self.skill}")

            return False
        elif victim.hp > 0:
            if self.skill != None:
                self.ability()
            print(f'У монстра по имени {victim.name} осталось {victim.hp} здоровья')
            return True

    def create_weapon(self):
        wpn = weapon_list[random.randint(0, 5)]
        wpn_rare = random.choice(list(weapon_dict.keys()))
        if wpn == weapon_list[0]:
            self.damage += 10 * wpn_rare
        elif wpn == weapon_list[1]:
            self.damage += 8 * wpn_rare
        elif wpn == weapon_list[2]:
            self.damage += 15 * wpn_rare
        elif wpn == weapon_list[3]:
            self.damage += 20 * wpn_rare
        elif wpn == weapon_list[4]:
            self.damage += 60 * wpn_rare
        elif wpn == weapon_list[5]:
            self.damage += 40 * wpn_rare
        return [wpn, weapon_dict[wpn_rare]]

    def create_armor(self):

        armor_rare = armor_list[random.randint(0, 2)]
        armor_rare_1 = random.choice(list(armor_dict.keys()))
        if armor_rare == armor_list[0]:
            self.hp += 60 * armor_rare_1
        elif armor_rare == armor_list[1]:
            self.hp += 50 * armor_rare_1
        elif armor_rare == armor_list[2]:
            self.hp += 100 * armor_rare_1
        return [armor_rare, armor_dict[armor_rare_1]]




class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def create_enemy():
        rnd_name = random.choice(enemy_name)
        rnd_hp = random.randint(200, 250)
        rnd_damage = random.randint(30, 60)
        return Enemy(rnd_name, rnd_hp, rnd_damage)

    def attack(self, victim):
        rnd_attack = random.randint(1, 5)
        if rnd_attack == 1:
            print("Монстр наносит двойной урон!")
            victim.hp -= self.damage * 2
        elif rnd_attack == 2 or rnd_attack == 3 or rnd_attack == 4:
            victim.hp -= self.damage
        elif rnd_attack == 5:
            print("Монстр промазал")
        if victim.hp <= 0:
            print(f"Монстр победил,ты повержен!")
            quit()
        elif victim.hp > 0:
            print(f'У героя {victim.name} осталось {victim.hp} здоровья')


def fight_choice():
    answer = input(f"Ты готов сразиться с монстром по имени {enemy.name}? (Да/Нет)").capitalize()
    if answer == "Да":
        result = player.attack(enemy)
        if result == True:
            enemy.attack(player)
            fight_choice()
    elif answer == "Нет":
        rnd_choice = random.randint(1, 3)
        if rnd_choice == 1 or rnd_choice == 2:
            print("Вы сбежали от монстра")
        elif rnd_choice == 3:
            print("Побег не удался, монстр наносит урон!")
            enemy.attack(player)
            fight_choice()
    else:
        print("Такого варианта нет")
        fight_choice()


my_name = input("Введите ваше имя: ").capitalize()
race_list = ["человек", "пират", "эльф", "вампир"]
prof_list = ["шахтёр", "фермер", "торговец", "защитник"]
enemy_name = ["Таракан", "Дремера", "Снорк", "Скромник", "Житель Изнанки", "Вендиго"]
weapon_list = ["Меч", "Лук", "Боевая Лопата", "Автомат", "Расщепитель Частиц", "MICRO-HID"]
weapon_dict = {1: "Обычное", 2: "Редкое", 3: "Эпическое"}
armor_list = ["Барьер", "Щит", "Тяжёлая Броня"]
armor_dict = {1: "Обычное", 2: "Редкое", 3: "Эпическое"}
powers_list = ["Отравление", "Замораживание", "Лечение"]
race = input(f"За какую расу будете играть? {race_list}: ").lower()
prof = input(f"За какую профессию будете играть? {prof_list}: ").lower()
player = Player.create_hero(my_name, race, prof)

while True:
    event = random.randint(1, 3)
    time.sleep(1)
    if event == 1:
        print("Тебе никто не встретился")
    elif event == 2:
        enemy = Enemy.create_enemy()
        print(f"Тебе встретился монстр по имени {enemy.name}, у него {enemy.hp} хп, {enemy.damage} дамага ")
        print(f"{player.name}, {player.hp} хп, {player.damage} дамаг, {player.lvl} лвл, {player.exp} опыта ")
        fight_choice()
    elif event == 3:
        player.hp += 30
        print(f"Ты нашёл зелье здоровья, твоё хп {player.hp} ")
