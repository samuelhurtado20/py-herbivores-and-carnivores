class Animal:
    Alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.Alive.append(self)

    def hide(self) -> None:
        self.hidden = not self.hidden

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @staticmethod
    def alive() -> list[str]:
        return [repr(animal) for animal in Animal.Alive]


class Herbivore(Animal):
    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        super().__init__(name, health, hidden)

    def be_eaten(self, amount: int) -> None:
        if not self.hidden:
            self.health -= amount
        if self.health <= 0:
            Animal.Alive.remove(self)


class Carnivore(Animal):
    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        super().__init__(name, health, hidden)

    def bite(self, herbivore: Herbivore) -> None:
        if not self.hidden and not herbivore.hidden:
            herbivore.be_eaten(50)
