class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

        if target.hp < 0:
            target.hp = 0

    def is_alive(self):
        return self.hp > 0


if __name__ == "__main__":
    goblin = Creature("Goblin", 30, 5)
    dragon = Creature("Dragon", 100, 15)

    dragon.attack(goblin)

    print(f"Goblin HP: {goblin.hp}")
    print(f"Goblin alive: {goblin.is_alive()}")