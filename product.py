from coder import create_image
from assigning import assigning


class Product:

    def __init__(self, color, shape, mass, size):
        self.color = color
        self.shape = shape
        self.mass = mass
        self.size = size


class FinalProduct:

    def __init__(self, color, shape, mass, size, name):
        self.color = color
        self.shape = shape
        self.mass = mass
        self.size = size
        self.name = name

        if size == 'small':
            self.price = 2.99

        if size == 'medium':
            self.price = 3.99

        if size == 'big':
            self.price = 4.99

        self.img = create_image(self)

    def shelf(self, shelfs):
        print(self.img)
        return assigning(self.img, shelfs);
