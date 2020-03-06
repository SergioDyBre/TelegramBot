from random import randint
class Enemy:
    name = ""
    life = 100
    board_x = None
    board_y = None
    board = None

    def __init__(self, name):
        self.name = name
        
   
 
    def set_coordinates(self, x, y):
        self.board_x = x
        self.board_y = y

    def set_board(self, board):
        self.board = board
 
    def move_up(self):
        if self.board_y == 0:
            return
        self.board.cells[self.board_y][self.board_x] = 0
        self.board.cells[self.board_y - 1][self.board_x] = self
        self.set_coordinates(self.board_x, self.board_y - 1)

    def move_down(self):
        if self.board_y == self.board.size_y - 1:
            return
        self.board.cells[self.board_y][self.board_x] = 0
        self.board.cells[self.board_y + 1][self.board_x] = self
        self.set_coordinates(self.board_x, self.board_y + 1)

    def move_left(self):
        if self.board_x == 0:
            return
        self.board.cells[self.board_y][self.board_x] = 0
        self.board.cells[self.board_y][self.board_x - 1] = self
        self.set_coordinates(self.board_x - 1, self.board_y)

    def move_right(self):
        if self.board_x == self.board.size_x - 1:
            return
        self.board.cells[self.board_y][self.board_x] = 0
        self.board.cells[self.board_y][self.board_x + 1] = self
        self.set_coordinates(self.board_x + 1, self.board_y)



    #aquí de momento vamos a randomizar o movemento do enemigo, máis adiante faremos a predicción de movemento en base ao pj pra atacalo
    def make_move(self):
        move = randint(0, 3)
        if move == 0:
            self.move_up()
        elif move == 1:
            self.move_right()
        elif move == 2:
            self.move_down()
        elif move == 3:
            self.move_left()		
