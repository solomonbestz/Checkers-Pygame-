from checkers import *



def main():
    game_running = True 
    clock = pg.time.Clock()
    board = Board()

    while game_running:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                ...

        board.draw(WIN)
        pg.display.update()
    pg.QUIT()

if __name__=='__main__':
    WIN = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Checkers')

    main()