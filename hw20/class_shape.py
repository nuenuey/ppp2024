from matplotlib.patches import Rectangle
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, h, v): #가로 h, 세로 v
        self.h = h
        self.v = v

    def area(self):#면적
        return self.h * self.v
    def perimeter(self):#둘레
        return (self.h + self.v)*2


class Triangle(Shape):
    def __init__(self, h, v):
        self.h = h
        self.v = v
    def area(self):#면적
        return self.h * self.v/2

    def perimeter(self):#둘레
        return self.h*3

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):#면적
        return self.r * self.r * math.pi

    def perimeter(self):#둘레
        return self.r*2*math.pi





class RegularHexagon(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):#면적
        return 3*3**1/2* self.r**2

    def perimeter(self):#둘레
        return self.r*6





def main():
    shapes =[]
    shapes.append(Rectangle(5,3)) #가로,세로인 사각형
    shapes.append(Triangle(5,2))
    shapes.append(Circle(3))
    shapes.append(RegularHexagon(3))

    if shape == "삼각형":
        a=float(input("a의 길이 :"))


     #도형의 둘레와 면적
    for shape in shapes:
        print(shape)
        print(f"면적 : {shape.area():.2f}") #면적 계산
        print(f"둘레 : {shape.perimeter():.2f}") #둘레

if __name__ == "__main__":
    main()