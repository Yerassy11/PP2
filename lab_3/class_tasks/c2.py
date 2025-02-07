class Shape:
    def __init__(self):
        self.length = 0

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

# Пример использования:
square = Square(4)
print(square.area())
