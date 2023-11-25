# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
import time
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, BLUE, WHITE, COUNT
from checkers.game import Game
from minimax.algorithm import minimax
COUNT = 0

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            start_time = time.time()
            value, new_board = minimax(game.get_board(), 2, WHITE, game, float('-inf'), float('inf'), False)
            end_time = time.time()
            print("Time taken: ", end_time - start_time)
            game.ai_move(new_board)

        if game.winner():
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()