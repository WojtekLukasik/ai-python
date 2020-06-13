import pygame
from settings import Settings
from field import Field
from shelf import Shelf

settings = Settings()


def create_board(screen):
    board = []

    shelfs = [
        (50, 50), (150, 50), (450, 50), (550, 50), (850, 50), (950, 50),
        (250, 250), (350, 250), (650, 250), (750, 250),
        (50, 450), (150, 450), (450, 450), (550, 450), (850, 450), (950, 450),
        (250, 650), (350, 650), (650, 650), (750, 650)
    ]

    for y in range(settings.y_fields):
        row = []
        for x in range(settings.x_fields):
            field = Field(screen, x, y, 50 + x * 100, 50 + y * 100, False, False, 1)
            for shelf in shelfs:
                if field.center_x == shelf[0] and field.center_y == shelf[1]:
                    field.is_shelf = True
                    field.image = pygame.image.load('img/shelf.png')

            row.append(field)
        board.append(row)
    for row in board:
        for field in row:
            field.add_neighbors(board)

    for row in board:
        for field in row:
            if field.x > 0 and board[field.y][field.x - 1].is_shelf:
                field.cost_of_travel += 1
            if field.x < 9 and board[field.y][field.x + 1].is_shelf:
                field.cost_of_travel += 1
            if field.y > 0 and board[field.y - 1][field.x].is_shelf:
                field.cost_of_travel += 1
            if field.y < 9 and board[field.y + 1][field.x].is_shelf:
                field.cost_of_travel += 1

    return board


def draw_board(board):
    for row in board:
        for field in row:
            field.blitme()


def get_shelfs(board):
    field_shelfs = []
    shelfs = []
    for row in board:
        for field in row:
            if field.isShelf():
                field_shelfs.append(field)

    shelf = Shelf(field_shelfs[0], "01")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[1], "01")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[2], "02")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[3], "02")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[4], "03")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[5], "03")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[6], "04")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[7], "04")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[8], "05")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[9], "05")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[10], "06")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[11], "06")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[12], "07")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[13], "07")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[14], "08")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[15], "08")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[16], "09")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[17], "09")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[18], "10")
    shelfs.append(shelf)

    shelf = Shelf(field_shelfs[19], "10")
    shelfs.append(shelf)

    return shelfs

