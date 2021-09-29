import random


class Enemy:
    def __init__(self):
        enemy_types = ["Dragon", "Skeleton", "Cyclops", "Wolf", "Golem", "Goblin", "Elf", "witch", "rabbit(Bubs bunny)",
                       "Orc", "Troll", "Tiger", "Ogre", "Minotaur", "griffin"]
        self.name = random.choice(enemy_types)
        self.health = random.randrange(50, 100, 10)

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def set_health(self, newHealth):
        self.health = newHealth

    def attack(self):
        return random.randint(5, 20)

