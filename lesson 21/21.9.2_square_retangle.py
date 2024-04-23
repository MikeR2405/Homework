class Retangle:
    def __init__(self,width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y =y
    def __str__(self):
        return f'Retangle : {self.x}, {self.y}, {self.width}, {self.height}.'

    def getArea(self):
        return self.width * self.height

rect_1 = Retangle(50,100, 5, 10)
print(rect_1)
print(rect_1.getArea())