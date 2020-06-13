import os

from codes_recognizer.rocognizer import recognizer


def assigning(product_code_path, shelfs):
    c = None
    code = recognizer(product_code_path)
    print(code)
    product_color = str(code[0]) + str(code[1])
    print(product_color)
    for shelf in shelfs:
        if shelf.color == product_color:
            shelf.add_product(code)
            c = shelf.get_field()

    print("Product", product_code_path, "is on", c)
    return c
