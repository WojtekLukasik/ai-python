import pygame


class Agent:

    def __init__(self, screen, position_x, position_y, turn):
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y
        self.turn = turn
        self.x = (self.position_x - 50) // 100
        self.y = (self.position_y - 50) // 100

        self.image = pygame.image.load('img/' + turn + '.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.item = None
        self.is_busy = False

        self.rect.center = (position_x, position_y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def turn_left(self):
        if self.turn == "Up":
            self.turn = "Left"
        elif self.turn == "Left":
            self.turn = "Down"
        elif self.turn == "Down":
            self.turn = "Right"
        elif self.turn == "Right":
            self.turn = "Up"
        self.image = pygame.image.load('img/' + self.turn + '.png')

    def turn_right(self):
        if self.turn == "Up":
            self.turn = "Right"
        elif self.turn == "Left":
            self.turn = "Up"
        elif self.turn == "Down":
            self.turn = "Left"
        elif self.turn == "Right":
            self.turn = "Down"
        self.image = pygame.image.load('img/' + self.turn + '.png')

    def move_forward(self, board):
        if self.turn == "Up" and self.position_y > 50 and board[(self.position_y - 100) // 100][self.position_x // 100]. \
                is_shelf == False:
            self.position_y -= 100
            self.y -= 1
        elif self.turn == "Left" and self.position_x > 50 and board[self.position_y // 100][(self.position_x - 100) // 100].\
                is_shelf == False:
            self.position_x -= 100
            self.x -= 1
        elif self.turn == "Down" and self.position_y < 950 and board[(self.position_y + 100) // 100][self.position_x // 100]. \
                is_shelf == False:
            self.position_y += 100
            self.y += 1
        elif self.turn == "Right" and self.position_x < 950 and board[self.position_y // 100][(self.position_x + 100) // 100].\
                is_shelf == False:
            self.position_x += 100
            self.x += 1
        self.rect.center = (self.position_x, self.position_y)

