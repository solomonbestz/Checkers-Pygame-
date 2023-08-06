from checkers import *



def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x //SQUARE_SIZE
    return row, col

def main():
    game_running = True 
    clock = pg.time.Clock()
    game = GameManager(WIN)
    


    while game_running:
        clock.tick(FPS)

        if game.board.winner() != None:
            print(game.board.winner())

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    pg.QUIT()

if __name__=='__main__':
    WIN = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Checkers')

    main()