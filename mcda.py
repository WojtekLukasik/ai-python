from supply import *

allProducts = supply()

color = {'black': 16, 'gold': 10, 'purple': 12, 'brown': 7, 'blue': 12, 'white': 14, 'red': 13, 'orange': 11, 'yellow': 8, 'silver': 15}
shape = {'rectangle': 15, 'pack': 19, 'square': 9, 'jar': 7, 'egg': 12}
size = {'small': 7, 'medium': 16, 'big': 13}

def sizeValue(X):
    if X.size == 'small':
        return X.mass/5
    if X.size == 'medium':
        return X.mass/10
    if X.size == 'big':
        return X.mass/20
parameters = {
    'color': {'weights': 3, 'q': 1, 'p': 5},
    'shape': {'weights': 4, 'q': 1, 'p': 6},
    'mass': {'weights': 0.5, 'q': 2, 'p': 10},
    'size': {'weights': 1, 'q': 1, 'p': 8}

}
def getConcordance(gA, gB, q, p):
    if gB <= gA + q:
        return 1
    if gB <= gA + p:
        return (p - gB + gA) / (p - q)
    return 0

def getAllTypeConcordance(A, B):
    concordance = 0.0
    weight_sum = 0

    parameter = parameters['color']
    w, q, p = parameter['weights'], parameter['q'], parameter['p']
    concordance += getConcordance(color[A.color], color[B.color], q, p) * w
    weight_sum += w

    parameter = parameters['shape']
    w, q, p = parameter['weights'], parameter['q'], parameter['p']
    concordance += getConcordance(shape[A.shape], shape[B.shape], q, p) * w
    weight_sum += w

    parameter = parameters['mass']
    w, q, p = parameter['weights'], parameter['q'], parameter['p']
    concordance += getConcordance(sizeValue(A), sizeValue(B), q, p) * w
    weight_sum += w

    parameter = parameters['size']
    w, q, p = parameter['weights'], parameter['q'], parameter['p']
    concordance += getConcordance(size[A.size], size[B.size], q, p) * w
    weight_sum += w

    concordance /= weight_sum
    return concordance

def getConcordanceAllProducts():
    C = []

    for i in range(len(allProducts)):
        c = 0
        for j in range(len(allProducts)):
            if j==i:
                continue
            else:
                c += getAllTypeConcordance(allProducts[i], allProducts[j])
        c /= len(allProducts)-1
        C.append(c)
    return C

def choseProducts():
    number = 20
    C = getConcordanceAllProducts()
    products = []
    prev = -1
    while number > 0:
        max = -1
        if prev == -1:
            max = 0
        for j in range(len(allProducts)):
            if prev == -1:
                if C[max]<C[j]:
                    max = j
            elif max == -1:
                if C[prev]>C[j]:
                    max = j
            elif C[max] < C[j] and C[j] < C[prev]:
                max = j
        prev = max
        for j in range(len(allProducts)):
            if C[max] > 0.75:
                if C[max] == C[j]:
                    products.append(allProducts[j])
                    number -= 1
                if number == 0:
                    break
            else:
                number = 0
    return products

def selectedSupply():
    products = choseProducts()
    supply = []
    for i in range(len(products)):
        supply.append([products[i].color, products[i].shape, products[i].mass, products[i].size, '-'])
    supply.append(['-', '-', 0, '-', '-'])
    print(supply)
    return supply