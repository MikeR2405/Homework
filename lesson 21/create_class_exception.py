class SquareException:
    pass
class ValueError(SquareException):
    pass
class NonPositiveException(ValueError):
    pass
class Square:
    def __init__(self,a):
        if self.a <= 0:
            raise NonPositiveException('Неправильно указанна сторона квадрата')


