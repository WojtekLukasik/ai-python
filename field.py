import pygame
from shelf import Shelf



class Field:

    def __init__(self, screen, x, y, center_x, center_y, is_shelf, is_occupied_by_agent, cost_of_travel):
        # Jakieś podstawowe rzeczy
        self.screen = screen
        self.x = x
        self.y = y
        self.center_x = center_x
        self.center_y = center_y
        self.is_shelf = is_shelf
        self.is_occupied_by_agent = is_occupied_by_agent
        self.cost_of_travel = cost_of_travel
        self.neighbors = []
        self.shelves = []

        # Te parametry są potrzebne do algorytmu A*
        self.g = 0
        self.h = 0
        self.f = 0
        self.previous = None

        # Przedmiot, który podnosi agent
        self.item = []
        self.is_empty = True

        # Te rzeczy są potrzebne do wyświetlenia pola
        self.image = pygame.image.load('img/Field.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = (center_x, center_y)

    # Metoda do wyświetlania pola na ekranie
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def add_neighbors(self, board):
        if self.x > 0 and board[self.y][self.x - 1].is_shelf == False:
            self.neighbors.append(board[self.y][self.x - 1])
        if self.x < 9 and board[self.y][self.x + 1].is_shelf == False:
            self.neighbors.append(board[self.y][self.x + 1])
        if self.y > 0 and board[self.y - 1][self.x].is_shelf == False:
            self.neighbors.append(board[self.y - 1][self.x])
        if self.y < 9 and board[self.y + 1][self.x].is_shelf == False:
            self.neighbors.append(board[self.y + 1][self.x])

    def addShelf(self):
        shelf = Shelf(len(self.shelves) + 1)
        self.shelves.append(shelf)

    def isShelf(self):
        return self.is_shelf