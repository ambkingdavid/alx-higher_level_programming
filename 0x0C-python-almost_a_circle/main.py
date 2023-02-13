#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(50, 220), Rectangle(50, 220, 100)]
    """ Rectangle(20, 25, 11, 80)]"""
    list_squares = [Square(50, 50, 85)]
    """ Square(15, 70, 50), Square(80, 30, 70)]"""

    Base.draw(list_rectangles, list_squares)
