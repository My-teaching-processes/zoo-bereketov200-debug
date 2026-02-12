"""Основное приложение, демонстрирующее принципы OOP."""

from src.animals import Dog, Cat, Bird
from src.zoo import Zoo


def main() -> None:
    """Зарустить основное приложение."""
    print("=" * 60)
    print("Каплас в систему управления OOP Zoo Management!")
    print("=" * 60)

    # Создание зоопарка
    zoo = Zoo("Парк Sunshine", "Центральный город")
    print(f"\nСоздано: {zoo}\n")

    # Создание различных животных
    print("--- Создание Животных ---")
    dog = Dog("Rex", 5, "Golden Retriever")
    print(dog)

    cat = Cat("Whiskers", 3, "Orange Tabby")
    print(cat)

    bird1 = Bird("Tweety", 2, "Canary")
    print(bird1)

    bird2 = Bird("Flightless", 10, "Penguin", can_fly=False)
    print(bird2)

    # Добавление животных в зоопарк
    print("\n--- Добавление Животных в Парк ---")
    for animal in [dog, cat, bird1, bird2]:
        zoo.add_animal(animal)

    # Отображение всех животных
    zoo.display_animals()

    # Животные, издающие звуки
    print("\n--- Животные звуки ---")
    for sound in zoo.get_all_sounds():
        print(sound)

    # Накормление всех животных
    zoo.feed_all()

    # Обучение собаки
    print("\n--- Обучение собаки ---")
    dog.teach_trick("Sit")
    dog.teach_trick("Stay")
    print(dog.perform_trick("Sit"))
    print(dog.perform_trick("Dance"))

    # активность кота
    print("\n--- Активности кота ---")
    print(cat.scratch("sofa"))
    cat.sleep(2)

    # Полет птицы
    print("\n--- Полет птицы ---")
    print(bird1.fly(100))
    print(bird1.land())
    print(bird2.fly(50))  # Пингвин не может летать

    # Физическая нагружка всех животных
    zoo.exercise_all(20)

    # Отображение обновленной информации
    zoo.display_animals()

    # Статистика
    print("\n--- Статистика Парка ---")
    print(f"Всего животных: {zoo.get_animal_count()}")
    print(f"Собаки: {zoo.get_species_count('Dog')}")
    print(f"Коты: {zoo.get_species_count('Cat')}")
    print(f"Птицы: {zoo.get_species_count('Bird')}")

    # Поиск определенного животного
    print("\n--- Поиск Животных ---")
    found = zoo.find_animal_by_name("Whiskers")
    if found:
        print(f"Найдено: {found.get_info()}")

    print("\n" + "=" * 60)
    print("Спасибо за посещение Парка OOP!")
    print("=" * 60)


if __name__ == "__main__":
    main()
