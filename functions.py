import sys
import pygame

from settings import Settings
from agent import Agent
from board import draw_board


def check_events(agent, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                agent.turn_right()
            elif event.key == pygame.K_LEFT:
                agent.turn_left()
            elif event.key == pygame.K_UP:
                agent.move_forward(board)
            elif event.key == pygame.K_SPACE:
                a_star(board[0][0], board[5][5])


def update_screen(board, screen, agent):
    draw_board(board)
    agent.blitme()

    pygame.display.flip()


def get_distance(field, goal_field):
    d = abs(field.x - goal_field.x) + abs(field.y - goal_field.y)
    return d


def a_star(start_field, goal_field, board):
    closed_set = []
    open_set = []
    path = []

    open_set.append(start_field)
    # start_field.image = pygame.image.load('img/green.png')

    while len(open_set) > 0:
        winner = 0

        for i in range(len(open_set)):
            if open_set[i].f < open_set[winner].f:
                winner = i

        current = open_set[winner]

        if current == goal_field:
            temp = current
            path.append(current)

            while temp.previous is not None:
                path.append(temp.previous)
                temp = temp.previous

            for field in path:
                field.image = pygame.image.load('img/path.png')

            for row in board:
                for field in row:
                    field.g = 0
                    field.h = 0
                    field.f = 0
                    field.previous = None

            return path

        open_set.remove(current)
        closed_set.append(current)
        # current.image = pygame.image.load('img/red.png')
        neighbors = current.neighbors

        for neighbor in neighbors:
            if neighbor not in closed_set:
                temp_g = current.g + neighbor.cost_of_travel

                if neighbor in open_set:
                    if temp_g < neighbor.g:
                        neighbor.g = temp_g
                else:
                    neighbor.g = temp_g
                    open_set.append(neighbor)
                    # neighbor.image = pygame.image.load('img/green.png')

                neighbor.h = get_distance(neighbor, goal_field)
                neighbor.f = neighbor.g + neighbor.h

                neighbor.previous = current


def check_turn(agent, next_field):
    if agent.y == next_field.y and next_field.x == agent.x + 1 and agent.turn == "Right":
        return True
    elif agent.y == next_field.y and next_field.x == agent.x - 1 and agent.turn == "Left":
        return True
    elif agent.x == next_field.x and next_field.y == agent.y + 1 and agent.turn == "Down":
        return True
    elif agent.x == next_field.x and next_field.y == agent.y - 1 and agent.turn == "Up":
        return True
    else:
        return False


def change_turn(agent, next_field):
    if agent.y == next_field.y and next_field.x == agent.x + 1 and agent.turn == "Up":
        agent.turn_right()
    elif agent.y == next_field.y and next_field.x == agent.x + 1 and agent.turn == "Down":
        agent.turn_left()
    elif agent.y == next_field.y and next_field.x == agent.x + 1 and agent.turn == "Left":
        agent.turn_left()
    elif agent.y == next_field.y and next_field.x == agent.x - 1 and agent.turn == "Up":
        agent.turn_left()
    elif agent.y == next_field.y and next_field.x == agent.x - 1 and agent.turn == "Down":
        agent.turn_right()
    elif agent.y == next_field.y and next_field.x == agent.x - 1 and agent.turn == "Right":
        agent.turn_right()
    elif agent.x == next_field.x and next_field.y == agent.y + 1 and agent.turn == "Right":
        agent.turn_right()
    elif agent.x == next_field.x and next_field.y == agent.y + 1 and agent.turn == "Left":
        agent.turn_left()
    elif agent.x == next_field.x and next_field.y == agent.y + 1 and agent.turn == "Up":
        agent.turn_left()
    elif agent.x == next_field.x and next_field.y == agent.y - 1 and agent.turn == "Right":
        agent.turn_left()
    elif agent.x == next_field.x and next_field.y == agent.y - 1 and agent.turn == "Left":
        agent.turn_right()
    elif agent.x == next_field.x and next_field.y == agent.y - 1 and agent.turn == "Down":
        agent.turn_right()


# def execute_step(agent, next_step, board, path):
#     if check_turn(agent, next_step):
#         agent.move_forward(board)
#         if len(path) != 0:
#             next_step = path.pop()
#         else:
#             next_step = None
#             for row in board:
#                 for field in row:
#                     if not field.is_shelf:
#                         field.image = pygame.image.load('img/Field.png')
#     else:
#         change_turn(agent, next_step)
