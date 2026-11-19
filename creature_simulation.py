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
class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.altitude = 0

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks from above!")
        target.hp -= self.attack_power

        if target.hp < 0:
            target.hp = 0

        print(f"{target.name} HP: {target.hp}")   

class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.altitude = 0

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks from above!")
        target.hp -= self.attack_power

        if target.hp < 0:
            target.hp = 0

        print(f"{target.name} HP: {target.hp}")


        
class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.depth = 0

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks underwater!")
        target.hp -= self.attack_power

        if target.hp < 0:
            target.hp = 0

        print(f"{target.name} HP: {target.hp}")
class FireCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.fire_level = 0

    def emit_fire(self, new_fire_level):
        self.fire_level = max(0, min(100, new_fire_level))
        print(f"{self.name} fire level: {self.fire_level}")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        damage = self.attack_power + self.fire_level // 10

        print(f"{self.name} uses fire attack!")
        target.hp -= damage

        if target.hp < 0:
            target.hp = 0

        print(f"{target.name} HP: {target.hp}")


if __name__ == "__main__":
    goblin = Creature("Goblin", 30, 5)
    dragon = Creature("Dragon", 100, 15)
    hawk = FlyingCreature("Hawk", 50, 10)
    dummy = Creature("Dummy", 40, 0)
    hawk.fly_to(100)
    hawk.attack(dummy)
    fish = SwimmingCreature("Shark", 70, 12)
    dummy = Creature("Dummy", 40, 0)
    dragon = FireCreature("Fire Dragon", 100, 15)
    dummy = Creature("Dummy", 100, 0)
    dragon.emit_fire(80)
    dragon.attack(dummy)

    fish.dive_to(30)
    fish.attack(dummy)
    dragon.attack(goblin)

    print(f"Goblin HP: {goblin.hp}")
    print(f"Goblin alive: {goblin.is_alive()}")
