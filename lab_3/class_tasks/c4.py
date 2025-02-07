class Shape:
    def __init__(self):
        pass  # Базовый класс ничего не делает по умолчанию

    def area(self):
        return 0  # По умолчанию площадь равна 0


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  # Вызываем конструктор базового класса
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Формула площади прямоугольника: длина * ширина

# Пример использования:
rectangle = Rectangle(7, 4)
print(rectangle.area())
