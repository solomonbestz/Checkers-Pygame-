from .checker_const import *
from .board import Board

class GameManager:
    def __init__(self, window) -> None:
        self._init()
        self.window = window

    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pg.display.update()

    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}


    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected_piece, row, col)
            skipped = self.valid_moves[(row, col)]
            self.change_turn()
            if skipped:
               self.board.remove(skipped) 
        else:
            return False
        return True 
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pg.draw.circle(self.window, GREEN, (col*SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def change_turn(self):
        self.valid_moves = []
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
