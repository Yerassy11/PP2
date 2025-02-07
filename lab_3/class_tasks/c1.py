class MyClass:
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())
        
# Пример использования:
obj = MyClass()
obj.getString()
obj.printString()
