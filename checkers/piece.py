from .checker_const import *

class Piece:
    PADDING = 10
    BORDER = 2
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.king = True

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_postion()

    def calc_postion(self) -> None:
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king(self) -> None:
        self.king = True

    def draw(self, window) -> None :
        radius = SQUARE_SIZE // 2 - self.PADDING
        pg.draw.circle(window, BORDER_COLOR, (self.x, self.y), radius)
        pg.draw.circle(window, self.color, (self.x, self.y), radius + self.BORDER)
        if self.king:
            window.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_width()//2))

    def __repr__(self) -> str: 
        return str(self.color)