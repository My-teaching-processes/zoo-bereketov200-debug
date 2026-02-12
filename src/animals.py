"""Конкретные реализации животных, демонстрирующие наследование и полиморфизм."""

from typing import Optional
from src.animal import Animal


class Dog(Animal):
    """
    Класс собаки, демонстрирующий конкретную реализацию базового класса Animal.
    
    Этот класс демонстрирует:
    - Наследование от абстрактного базового класса
    - Реализацию абстрактных методов
    - Полиморфизм
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализация собаки.
        
        Аргументы:
            name: Имя собаки
            age: Возраст собаки
            breed: Порода собаки
        """
        super().__init__(name, age, "Dog")
        self._breed = breed
        self._tricks: list[str] = []

    @property
    def breed(self) -> str:
        """Получить породу собаки."""
        return self._breed

    def make_sound(self) -> str:
        """Вернуть звук, который издает собака."""
        return f"{self._name} says: Woof! Woof!"

    def eat(self, food: str) -> None:
        """Накормить собаку."""
        if self._energy < 100:
            self._energy = min(100, self._energy + 20)
            print(f"{self._name} съел {food} и очень энергична!")
        else:
            print(f"{self._name} сейчас не голодна.")

    def teach_trick(self, trick: str) -> None:
        """
        Научить собаку новому трюку.
        
        Аргументы:
            trick: Название трюка
        """
        if trick not in self._tricks:
            self._tricks.append(trick)
            print(f"{self._name} научился новому трюку: {trick}!")

    def perform_trick(self, trick: str) -> Optional[str]:
        """
        Выполнить изученный трюк.
        
        Аргументы:
            trick: Трюк для выполнения
            
        Возвращает:
            Описание выполнения трюка
        """
        if self._energy < 10:
            return f"{self._name} is too tired to perform tricks."
        elif trick in self._tricks:
            self._energy -= 10
            return f"{self._name} performed the trick: {trick}!"
        else:
            return f"{self._name} hasn't learned the {trick} trick yet."

    def get_info(self) -> str:
        """Получить подробную информацию о собаке."""
        base_info = super().get_info()
        tricks_info = f", Трюки: {', '.join(self._tricks) if self._tricks else 'Нет'}"
        return f"{base_info}, Порода: {self._breed}{tricks_info}"


class Cat(Animal):
    """Класс кота, демонстрирующий другую конкретную реализацию Animal."""

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Инициализация кота.
        
        Аргументы:
            name: Имя кота
            age: Возраст кота
            color: Окраска/пыстэрн кота
        """
        super().__init__(name, age, "Cat")
        self._color = color
        self._mood = "neutral"

    @property
    def color(self) -> str:
        """Получить окраску кота."""
        return self._color

    @property
    def mood(self) -> str:
        """Получить унастроение кота."""
        return self._mood

    def make_sound(self) -> str:
        """Вернуть звук, который издает кот."""
        return f"{self._name} says: Meow!"

    def eat(self, food: str) -> None:
        """Накормить кота."""
        if self._energy < 100:
            self._energy = min(100, self._energy + 15)
            self._mood = "happy"
            print(f"{self._name} съел {food} и теперь очень рад!")
        else:
            print(f"{self._name} сейчас не интересуются в еде.")

    def scratch(self, target: str = "furniture") -> str:
        """
        Кот царапает что-нибудь.
        
        Аргументы:
            target: Объект, который царапает кот
            
        Возвращает:
            Описание акции царапания
        """
        self._mood = "playful"
        return f"{self._name} царапает {target}!"

    def get_info(self) -> str:
        """Получить подробную информацию о коте."""
        base_info = super().get_info()
        return f"{base_info}, Окраска: {self._color}, Унастроение: {self._mood}"


class Bird(Animal):
    """Класс птицы, демонстрирующий еще одну конкретную реализацию Animal."""

    def __init__(self, name: str, age: int, species: str, can_fly: bool = True) -> None:
        """
        Инициализация птицы.
        
        Аргументы:
            name: Имя птицы
            age: Возраст птицы
            species: Вид птицы
            can_fly: Может ли птица летать
        """
        super().__init__(name, age, species)
        self._can_fly = can_fly
        self._altitude = 0

    @property
    def can_fly(self) -> bool:
        """Проверить, может ли птица летать."""
        return self._can_fly

    @property
    def altitude(self) -> int:
        """Получить текущую высоту птицы."""
        return self._altitude

    def make_sound(self) -> str:
        """Вернуть звук, который издает птица."""
        return f"{self._name} says: Tweet! Tweet!"

    def eat(self, food: str) -> None:
        """Накормить птицу."""
        if self._energy < 100:
            self._energy = min(100, self._energy + 10)
            print(f"{self._name} съел {food} и чувствует себя энергичным!")
        else:
            print(f"{self._name} имеет достаточно энергии.")

    def fly(self, altitude: int) -> Optional[str]:
        """
        Дать птице летать на определенной высоте.
        
        Аргументы:
            altitude: Целевая высота в метрах
            
        Возвращает:
            Описание полета или ничего, если не вы могли летать
        """
        if not self._can_fly:
            return f"{self._name} cannot fly."
        elif self._energy < 20:
            return f"{self._name} is too tired to fly."
        else:
            self._altitude = altitude
            self._energy -= 20
            return f"{self._name} flew to {altitude} meters altitude!"

    def land(self) -> str:
        """На землю птице."""
        self._altitude = 0
        return f"{self._name} has landed!"

    def get_info(self) -> str:
        """Получить подробную информацию о птице."""
        base_info = super().get_info()
        fly_status = "Да" if self._can_fly else "Нет"
        return f"{base_info}, Может летать: {fly_status}, Высота: {self._altitude}м"
