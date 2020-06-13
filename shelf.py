import pygame


class Shelf:

    def __init__(self, field, color):
        self.field = field
        self.color = color
        self.level1 = []
        self.level2 = []
        self.level3 = []


    def add_product(self, product):
        if product[7] == 1:
            self.level1.append(product)
        elif product[7] == 2:
            self.level2.append(product)
        else:
            self.level3.append(product)

    def get_field(self):
        return self.field

    def get_color(self):
        return self.color
