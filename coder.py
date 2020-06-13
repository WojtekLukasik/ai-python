from PIL import Image, ImageDraw, ImageFont
# img = Image.new('RGB', (504, 112), color='white')
# d = ImageDraw.Draw(img)
# fnt = ImageFont.truetype('D:\Studia\Projects\AL-2020\img\codes\\arial_bold.ttf', 75)
# d.text((30, 30), "10010101249", font=fnt, fill=(0, 0, 0))
# img.save('img/codes/test.png')


def code_mass(mass):
    if mass < 100:
        return '0' + str(mass)
    else:
        return str(mass)


def code_price(price):
    return str(int(price * 100))


def code_size(size):
    if size == 'small':
        return '1'
    elif size == 'medium':
        return '2'
    else:
        return '3'


def code_color(color):
    if color == 'black':
        return '01'
    if color == 'gold':
        return '02'
    if color == 'purple':
        return '03'
    if color == 'brown':
        return '04'
    if color == 'blue':
        return '05'
    if color == 'white':
        return '06'
    if color == 'red':
        return '07'
    if color == 'orange':
        return '08'
    if color == 'yellow':
        return '09'
    if color == 'silver':
        return '10'


def code_shape(shape):
    if shape == 'rectangle':
        return '01'
    if shape == 'pack':
        return '02'
    if shape == 'square':
        return '03'
    if shape == 'jar':
        return '04'
    if shape == 'egg':
        return '05'


def create_image(product):
    string = code_color(product.color) + code_shape(product.shape) + code_mass(product.mass) + \
             code_size(product.size) + code_price(product.price)
    print(string)
    img = Image.new('RGB', (560, 112), color='white')
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('img\codes\\arial_bold.ttf', 75)
    d.text((28, 28), string, font=fnt, fill=(0, 0, 0))
    path = 'img/codes/' + product.name + '.png'
    img.save(path)
    return path

