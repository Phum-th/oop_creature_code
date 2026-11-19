# Creature Battle Project (OOP + Git Branching Practice)

This project is designed to help me learn **object-oriented programming** in Python — especially **inheritance** — while also practicing key **Git concepts** like branching, merging, conflict resolution, and version history.

I will begin with a base class (`Creature`) and create additional subclasses on separate Git branches to simulate a real development workflow.

---

## Learning Objectives

### Python / OOP
- Understand and implement **classes**
- Use **inheritance** to extend behaviors
- Override and extend methods (e.g., `attack()`)
- Practice writing simple test code in `main`

### Git / Version Control
- Create and switch branches
- Merge branches into `main`
- Resolve merge conflicts
- View commit history (`git log --graph --all`)

---

## Project Structure

```text
oop_creature_code/
│
├── creature_simulation.py
└── README.md
```

## Classes

### 1. Creature
The base class with:
- name
- hp
- attack_power
- attack()
- is_alive()

### 2. FlyingCreature
Inherits from Creature.
- altitude
- fly_to()
- Overrides attack() for aerial attacks.

### 3. SwimmingCreature
Inherits from Creature.
- depth
- dive_to()
- Overrides attack() for underwater attacks.

### 4. FireCreature
Inherits from Creature.
- fire_level
- emit_fire()
- Overrides attack() to add fire damage.

---

## How to Run the Program

1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python creature_simulation.py
```

The program will run the test cases for all four creature classes and display their attack messages and HP values.

## Git Branches

The project uses the following branches:

- `main` – Base Creature class and final merged project.
- `flying_creature` – FlyingCreature implementation.
- `swimming_creature` – SwimmingCreature implementation.
- `fire_creature` – FireCreature implementation.

## What I Learned

Through this project, I practiced Python inheritance, method overriding, and using `super()` to reuse the parent class constructor. I also learned how to create Git branches, merge different features, resolve merge conflicts, and track changes using Git history.