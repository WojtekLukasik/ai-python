from product import Product
import random


def create_data_products():
    allProducts = []

    product = Product('black', 'rectangle', 51, 'small')
    allProducts.append(product)
    product = Product('gold', 'pack', 100, 'big')
    allProducts.append(product)
    product = Product('purple', 'rectangle', 100, 'big')
    allProducts.append(product)
    product = Product('brown', 'pack', 45, 'small')
    allProducts.append(product)
    product = Product('blue', 'rectangle', 50, 'medium')
    allProducts.append(product)
    product = Product('blue', 'square', 40, 'small')
    allProducts.append(product)
    product = Product('blue', 'rectangle', 35, 'small')
    allProducts.append(product)
    product = Product('gold', 'rectangle', 40, 'medium')
    allProducts.append(product)
    product = Product('gold', 'rectangle', 50, 'medium')
    allProducts.append(product)
    product = Product('brown', 'rectangle', 55, 'medium')
    allProducts.append(product)
    product = Product('brown', 'rectangle', 45, 'medium')
    allProducts.append(product)
    product = Product('white', 'rectangle', 40, 'medium')
    allProducts.append(product)
    product = Product('red', 'rectangle', 50, 'medium')
    allProducts.append(product)
    product = Product('blue', 'rectangle', 115, 'big')
    allProducts.append(product)
    product = Product('white', 'rectangle', 15, 'small')
    allProducts.append(product)
    product = Product('red', 'pack', 70, 'medium')
    allProducts.append(product)
    product = Product('orange', 'rectangle', 45, 'medium')
    allProducts.append(product)
    product = Product('blue', 'rectangle', 55, 'medium')
    allProducts.append(product)
    product = Product('gold', 'rectangle', 120, 'big')
    allProducts.append(product)
    product = Product('white', 'rectangle', 120, 'big')
    allProducts.append(product)
    product = Product('white', 'jar', 600, 'big')
    allProducts.append(product)
    product = Product('white', 'rectangle', 25, 'small')
    allProducts.append(product)
    product = Product('brown', 'jar', 500, 'big')
    allProducts.append(product)
    product = Product('brown', 'jar', 470, 'big')
    allProducts.append(product)
    product = Product('red', 'jar', 250, 'medium')
    allProducts.append(product)
    product = Product('black', 'jar', 250, 'medium')
    allProducts.append(product)
    product = Product('orange', 'jar', 250, 'medium')
    allProducts.append(product)
    product = Product('brown', 'rectangle', 140, 'big')
    allProducts.append(product)
    product = Product('blue', 'rectangle', 140, 'big')
    allProducts.append(product)
    product = Product('white', 'rectangle', 100, 'big')
    allProducts.append(product)
    product = Product('yellow', 'rectangle', 300, 'big')
    allProducts.append(product)
    product = Product('blue', 'rectangle', 380, 'big')
    allProducts.append(product)
    product = Product('purple', 'rectangle', 330, 'big')
    allProducts.append(product)
    product = Product('blue', 'rectangle', 294, 'big')
    allProducts.append(product)
    product = Product('silver', 'pack', 280, 'big')
    allProducts.append(product)
    product = Product('red', 'rectangle', 50, 'medium')
    allProducts.append(product)
    product = Product('white', 'egg', 20, 'small')
    allProducts.append(product)
    product = Product('brown', 'rectangle', 180, 'big')
    allProducts.append(product)
    product = Product('red', 'rectangle', 235, 'big')
    allProducts.append(product)
    product = Product('white', 'rectangle', 25, 'medium')
    allProducts.append(product)
    product = Product('black', 'pack', 70, 'big')
    allProducts.append(product)
    product = Product('white', 'rectangle', 50, 'medium')
    allProducts.append(product)
    product = Product('white', 'rectangle', 24, 'medium')
    allProducts.append(product)
    product = Product('red', 'rectangle', 46, 'medium')
    allProducts.append(product)
    product = Product('yellow', 'rectangle', 25, 'medium')
    allProducts.append(product)
    product = Product('yellow', 'rectangle', 47, 'medium')
    allProducts.append(product)
    product = Product('brown', 'rectangle', 30, 'medium')
    allProducts.append(product)
    product = Product('purple', 'rectangle', 22, 'small')
    allProducts.append(product)
    product = Product('brown', 'rectangle', 294, 'medium')
    allProducts.append(product)
    product = Product('white', 'rectangle', 250, 'big')
    allProducts.append(product)

    return allProducts

def supply():
    allProducts = create_data_products()
    R = []
    supply = []
    while len(R)<20:
        rand = random.randint(0, 49)
        if R.count(rand) == 0:
            R.append(rand)
            supply.append(allProducts[rand])
    return supply
