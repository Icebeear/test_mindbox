from math import sqrt, pi, isclose 

# базовый класс фигур 
class Shape:
    def calculate_area(self):
        raise NotImplementedError(
            "В дочернем классе должен быть переопределен метод calculate_area"
        )

# класс для работы с кругом 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

# класс для работы с триугольником
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if not (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            
            raise ValueError("У треугольника сумма двух любых сторон должна быть больше третьей")
        
    # вычисление площади с помощью формулы герона
    def calculate_area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    # является ли треугольник прямоугольным
    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

# класс для вычисления площади ромба (для примерс добавлянием)
class Rhombus(Shape):
    def __init__(self, side, heigth):
        self.side = side 
        self.heigth = heigth

    def calculate_area(self):
        return self.side * self.heigth

def calculate_area(*args, **kwargs):
    figures = {
        1: Circle,
        2: Rhombus,
        3: Triangle,
    }

    if len(args) > 3:
        raise NotImplementedError (
            "Метод для расчета площади этой фигуры не реализован"
        )
    
    else:
        shape = figures[len(args)]
        return shape(*args).calculate_area()



if __name__ == '__main__':
    pass