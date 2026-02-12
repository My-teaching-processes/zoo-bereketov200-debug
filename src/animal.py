"""Базовый класс Animal, демонстрирующий наследование и абстракцию."""

from abc import ABC, abstractmethod
from typing import Optional


class Animal(ABC):
    """
    Абстрактный базовый класс для всех животных.
    
    Этот класс демонстрирует:
    - Инкапсуляцию (приватные атрибуты со свойствами)
    - Наследование (базовый класс для подклассов)
    - Абстракцию (абстрактные методы)
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Инициализация животного.
        
        Аргументы:
            name: Имя животного
            age: Возраст животного в годах
            species: Вид животного
        """
        self._name = name
        self._age = age
        self._species = species
        self._energy = 100  # Уровень энергии от 0-100

    @property
    def name(self) -> str:
        """Получить имя животного."""
        return self._name

    @property
    def age(self) -> int:
        """Получить возраст животного."""
        return self._age

    @property
    def species(self) -> str:
        """Получить вид животного."""
        return self._species

    @property
    def energy(self) -> int:
        """Получить уровень энергии животного."""
        return self._energy

    @abstractmethod
    def make_sound(self) -> str:
        """
        Вернуть звук, который издает животное.
        
        Это абстрактный метод, который должен быть реализован подклассами.
        """
        pass

    @abstractmethod
    def eat(self, food: str) -> None:
        """
        Накормить животное.
        
        Аргументы:
            food: Тип пищи для животного
        """
        pass

    def sleep(self, hours: int) -> None:
        """
        Уложить животное спать.
        
        Аргументы:
            hours: Количество часов сна
        """
        energy_gain = min(hours * 10, 100 - self._energy)
        self._energy += energy_gain
        print(f"{self._name} спал {hours} час(ов) и получил {energy_gain} энергии.")

    def exercise(self, minutes: int) -> None:
        """
        Физическая нагрузка для животного.
        
        Аргументы:
            minutes: Продолжительность упражнения в минутах
        """
        energy_loss = min(minutes // 5, self._energy)
        self._energy -= energy_loss
        print(f"{self._name} занимался {minutes} минут и потерял {energy_loss} энергии.")

    def get_info(self) -> str:
        """Получить подробную информацию о животном."""
        return (f"Имя: {self._name}, Вид: {self._species}, "
                f"Возраст: {self._age} лет, Энергия: {self._energy}/100")

    def __str__(self) -> str:
        """Вернуть строковое представление животного."""
        return f"{self._name} - {self._species}"

    def __repr__(self) -> str:
        """Вернуть детальное строковое представление."""
        return f"{self.__class__.__name__}(name='{self._name}', age={self._age})"
