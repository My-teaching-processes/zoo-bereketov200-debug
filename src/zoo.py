"""Класс Zoo, демонстрирующий композицию и управление коллекцией."""

from typing import List, Optional
from src.animal import Animal


class Zoo:
    """
    Класс Zoo, управляющий коллекцией животных.
    """

    def __init__(self, name: str, location: str) -> None:
        """
        Инициализация зоопарка.
        
        Аргументы:
            name: Название зоопарка
            location: Локация зоопарка
        """
        self._name = name
        self._location = location
        self._animals: List[Animal] = []

    # Здесь можно добавить нужные методы для управления животными в зоопарке (нужно чтобы тесты проходили)