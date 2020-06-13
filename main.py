import pygame
import functions
import sys
import time
import decision_tree
import data

from agent import Agent
from settings import Settings
from board import create_board, draw_board, get_shelfs
from random import randint, choice
from mcda import selectedSupply
from product import FinalProduct
from coder import create_image


# Inicjalizacja programu i utworzenie obiektu ekrany
def run():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Inteligentny wózek widłowy")
    # agent = Agent(screen, 550, 450, "Down")
    agent = Agent(screen, 950, 950, "Left")
    board = create_board(screen)
    shelfs = get_shelfs(board)
    my_tree = decision_tree.build_tree(data.learning_data)
    products_from_supply = []
    supply_depot = board[9][0]

    dest_field = None
    path = []
    next_step = None
    # Rozpoczęcie głównej pętli programu
    while True:
        # functions.check_events(agent, board)
        # functions.update_screen(board, screen, agent)
        #
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
                elif event.key == pygame.K_DOWN:
                    agent.item = None
                    agent.is_busy = False
                elif event.key == pygame.K_SPACE:
                    products_from_supply = selectedSupply()

                    # print("Wybrano: " + board[9][0].item[-1])
                    # field = board[9][0]
                    # if not field.is_shelf:
                    #     path = functions.a_star(board[agent.y][agent.x], field, board)
                    #     path.pop(len(path) - 1)
                    #     next_step = path.pop(len(path) - 1)

        if len(products_from_supply) != 0 and supply_depot.is_empty is True and agent.is_busy is False:
            supply_depot.item = products_from_supply.pop(0)
            print(supply_depot.item)
            path = functions.a_star(board[agent.y][agent.x], supply_depot, board)
            path.pop(len(path) - 1)
            next_step = path.pop(len(path) - 1)
            agent.is_busy = True

        if board[agent.y][agent.x].item and agent.item is None:
            prediction = decision_tree.print_leaf(decision_tree.classify(board[agent.y][agent.x].item, my_tree))
            print("Agent uważa, że przedmiot to: " + prediction[0])
            new_product = FinalProduct(supply_depot.item[0], supply_depot.item[1], supply_depot.item[2],
                                       supply_depot.item[3], prediction[0])
            print(new_product)

            '''
            Wyznacza patha do polki na ktora ma polozyc  produkt. 
            '''
            # list [x, y]
            dest_shelf = new_product.shelf(shelfs)
            path = functions.a_star(board[agent.y][agent.x], dest_shelf.get_field(), board)

            ''''''
            agent.item = new_product
            path.pop(len(path) - 1)
            next_step = path.pop(len(path) - 1)
            agent.is_busy = True

        if board[agent.y][agent.x] == dest_field:
            agent.is_busy = False
            agent.item = None

        if next_step is not None:
            time.sleep(0.5)
            if functions.check_turn(agent, next_step):
                agent.move_forward(board)
                if len(path) != 0:
                    next_step = path.pop()
                else:
                    next_step = None
                    # print(next_step, path)
                    for row in board:
                        for field in row:
                            if not field.is_shelf:
                                field.image = pygame.image.load('img/Field.png')

            else:
                functions.change_turn(agent, next_step)

        draw_board(board)
        agent.blitme()

        pygame.display.flip()



run()
