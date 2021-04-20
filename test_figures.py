# -*-coding: utf-8 -*-
"""Файл, содержащий  классы фигур, импортируется из пакета Figures
obj_triangle = Triangle(side_a, side_b, side_c) - объект "Треугольник"
        side_a, side_b, side_c - стороны треугольника
obj_rectangle = Rectangle(side_a, side_b) - объект "Прямоугольник"
        side_a, side_b - смежные стороны прямоугольника
obj_square = Square(side) - объект "Квадрат"
        side - сторона квадрата
obj_circle = Circle(radius) - объект "Круг" ("Окружность")
        radius - радиус окружности
Методы классов фигур:
figure.perimeter() - периметр (длина окружности) фигуры
figure.area() - площадь фигуры
figure.add_area(another_figure) - сумма площадей двух фигур (фигура должна быть экземпляром подкласса базового класса Figure())
"""

from Figures.figures import *
import pytest

triangle = Triangle(3,4,5)
rectangle = Rectangle(8,10)
square = Square(4)
circle = Circle(10)
rhombus = Rhombus(12,8)

# Блок тестов, проверяющих, является ли класс Figure родительским для проверяемого класса
def test_triangleIsInstance():
    assert isinstance(triangle, Figure),"Класс 'Figure' не является базовым"
def test_rectangleIsInstance():
    assert isinstance(rectangle, Figure),"Класс 'Figure' не является базовым"
def test_squareIsInstance():
    assert isinstance(square, Figure),"Класс 'Figure' не является базовым"
def test_circleIsInstance():
    assert isinstance(circle, Figure),"Класс 'Figure' не является базовым"
def test_rhombusIsInstance():
    assert isinstance(rhombus, Figure),"Класс 'Figure' не является базовым"

def test_triangles_area_counts():
#    triangle = T(3,4,5)
    assert triangle.area() !=0,"Площадь треугольника не может быть равной нулю"
    assert triangle.area() == 6,"Ошибка в вычислении площади"


def test_triangles_perimeter_counts():
#    triangle = T(3,4,5)
    assert triangle.perimeter() !=0,"Периметр треугольника не может быть равен нулю"
    assert triangle.perimeter() == 12,"Ошибка в вычислении преиметра"

#@pytest.mark.skip
def test_is_triangle_exists():
    wrongTriangle = Triangle(3,4,9)


def test_rectangles_area_counts():
    rectangle = Rectangle(8,10)
    assert rectangle.area() !=0,"Площадь прямоугольника не может быть равной нулю"
    assert rectangle.area() == 80,"Ошибка в вычислении площади"


def test_rectangles_perimeter_counts():
    rectangle = Rectangle(8,10)
    assert rectangle.perimeter() !=0,"Периметр прямоугольника не может быть равен нулю"
    assert rectangle.perimeter() == 36,"Ошибка в вычислении преиметра"

def test_square_area_counts():
    square = Square(6)
    assert square.area() !=0,"Площадь квадрата не может быть равной нулю"
    assert square.area() == 36,"Ошибка в вычислении площади"


def test_square_perimeter_counts():
    square = Square(6)
    assert square.perimeter() !=0,"Периметр квадрата не может быть равен нулю"
    assert square.perimeter() == 24,"Ошибка в вычислении преиметра"


def test_circle_area_counts():
    circle = Circle(10)
    assert circle.area() !=0,"Площадь круга не может быть равной нулю"
    assert circle.area() == 314,"Ошибка в вычислении площади"


def test_circumference_counts():
    circle = Circle(10)
    assert circle.perimeter() !=0,"Длина окружности не может быть равна нулю"
    assert circle.perimeter() == 2*3.14*10,"Ошибка в вычислении длины окружности" 
