from rectangle import Rectangle, Square, Circle
# создаем два лпрямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# считаем площадь прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())
# деллаем квадраты
square_1 = Square(5)
square_2 = Square(10)
# считаем площадь квадратов
print(square_1.get_area_square(),
      square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())
# circle
circle_1 = Circle(5)
circle_2 = Circle(10)
# PR2
print(circle_1.get_area_circle(),
      circle_2.get_area_circle())