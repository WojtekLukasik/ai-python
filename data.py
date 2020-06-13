from sweets import Sweets


def create_data_sweets():
    allProducts = []

    sweet = Sweets('Mars', 'czekoladowy', 'baton', 'sredni', 2.49)
    allProducts.append(sweet)
    sweet = Sweets('Mars', 'czekoladowy', 'czekolada', 'duzy', 4.99)
    allProducts.append(sweet)
    sweet = Sweets('Mars', 'czekoladowy', 'czekolada', 'ogromny', 11.26)
    allProducts.append(sweet)
    sweet = Sweets('M&M', 'czekoladowy', 'czekolada', 'duzy', 3.99)
    allProducts.append(sweet)
    sweet = Sweets('M&M', 'czekoladowy', 'baton', 'sredni', 2.89)
    allProducts.append(sweet)
    sweet = Sweets('Nestle', 'bananowy', 'landrynka', 'maly', 0.39)
    allProducts.append(sweet)
    sweet = Sweets('Nestle', 'truskawkowy', 'landrynka', 'maly', 0.39)
    allProducts.append(sweet)
    sweet = Sweets('Nestle', 'cola', 'landrynka', 'maly', 0.49)
    allProducts.append(sweet)
    sweet = Sweets('Wedel', 'czekoladowy', 'baton', 'sredni', 1.99)
    allProducts.append(sweet)
    sweet = Sweets('Maoam', 'truskawkowy', 'guma', 'maly', 0.25)
    allProducts.append(sweet)

    return allProducts


learning_data = [
    # kolor, kształt, waga, rozmiar, nazwa
    ['black', 'rectangle', 51, 'small', 'Mars'],
    ['gold', 'pack', 100, 'big', 'Haribo'],
    ['purple', 'rectangle', 100, 'big', 'Milka-czekolada'],
    ['brown', 'pack', 45, 'small', 'M&M'],
    ['blue', 'rectangle', 50, 'medium', 'Bounty'],
    ['blue', 'square', 40, 'small', 'Knoppers'],
    ['blue', 'rectangle', 35, 'small', 'Milky-way'],
    ['gold', 'rectangle', 40, 'medium', 'Twix'],
    ['gold', 'rectangle', 50, 'medium', 'Prince-polo'],
    ['brown', 'rectangle', 55, 'medium', 'Snickers'],
    ['brown', 'rectangle', 45, 'medium', 'Lion'],
    ['white', 'rectangle', 40, 'medium', 'Kinder-bueno'],
    ['red', 'rectangle', 50, 'medium', 'Kit-kat'],
    ['blue', 'rectangle', 115, 'big', 'Wedel-czekolada'],
    ['white', 'rectangle', 15, 'small', 'Krowka'],
    ['red', 'pack', 70, 'medium', 'Skittles'],
    ['orange', 'rectangle', 45, 'medium', 'Reeses'],
    ['blue', 'rectangle', 55, 'medium', 'Oreo'],
    ['gold', 'rectangle', 120, 'big', 'Ferrero-rocher'],
    ['white', 'rectangle', 120, 'big', 'Rafaello'],
    ['white', 'jar', 600, 'big', 'Nutella'],
    ['white', 'rectangle', 25, 'small', 'Duplo'],
    ['brown', 'jar', 500, 'big', 'GoOn'],
    ['brown', 'jar', 470, 'big', 'Active Orzechowe'],
    ['red', 'jar', 250, 'medium', 'Strawberry-Jam'],
    ['black', 'jar', 250, 'medium', 'Blackberry-Jam'],
    ['orange', 'jar', 250, 'medium', 'Peach-Jam'],
    ['brown', 'rectangle', 140, 'big', 'Jezyki-classic'],
    ['blue', 'rectangle', 140, 'big', 'Jezyki-kokos'],
    ['white', 'rectangle', 100, 'big', 'Kinder-Chocolate'],
    ['yellow', 'rectangle', 300, 'big', 'belVita'],
    ['blue', 'rectangle', 380, 'big', 'Wedel-Ptasie-Mleczko'],
    ['purple', 'rectangle', 330, 'big', 'Milka-Alpejskie-Mleczko'],
    ['blue', 'rectangle', 294, 'big', 'Delicje'],
    ['silver', 'pack', 280, 'big', 'Wawel-Michalki'],
    ['red', 'rectangle', 50, 'medium', 'Krakuski-Petit-Beurre'],
    ['white', 'egg', 20, 'small', 'Kinder-Niespodzianka'],
    ['brown', 'rectangle', 180, 'big', 'Familijne-Wafle'],
    ['red', 'rectangle', 235, 'big', 'dr-Gerard-PryncyPalki'],
    ['white', 'rectangle', 25, 'medium', 'Nestle-Cini-Minis-Batonik'],
    ['black', 'pack', 70, 'big', 'Korsarz-Draze'],
    ['white', 'rectangle', 50, 'medium', 'Goralki'],
    ['white', 'rectangle', 24, 'medium', 'Kinder-Country'],
    ['red', 'rectangle', 46, 'medium', '3Bit'],
    ['yellow', 'rectangle', 25, 'medium', 'Nestle-Nesquik-Batonik'],
    ['yellow', 'rectangle', 47, 'medium', 'Wedel-WW'],
    ['brown', 'rectangle', 30, 'medium', 'Lubisie'],
    ['purple', 'rectangle', 22, 'small', 'Maoam'],
    ['brown', 'rectangle', 294, 'medium', 'Grzeski'],
    ['white', 'rectangle', 250, 'big', 'merci'],
]


def create_data_dict():
    products_as_dict = []

    sweet = Sweets('Mars', 'czekoladowy', 'baton', 'sredni', 2.49)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('Mars', 'czekoladowy', 'czekolada', 'duzy', 4.99)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('Mars', 'czekoladowy', 'czekolada', 'ogromny', 11.26)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('M&M', 'czekoladowy', 'czekolada', 'duzy', 3.99)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('M&M', 'czekoladowy', 'baton', 'sredni', 2.89)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('Nestle', 'bananowy', 'landrynka', 'maly', 0.39)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('Nestle', 'truskawkowy', 'landrynka', 'maly', 0.39)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('Nestle', 'cola', 'landrynka', 'maly', 0.49)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('Wedel', 'czekoladowy', 'baton', 'sredni', 1.99)
    products_as_dict.append(vars(sweet))
    sweet = Sweets('Maoam', 'truskawkowy', 'guma', 'maly', 0.25)
    products_as_dict.append(vars(sweet))

    return products_as_dict
