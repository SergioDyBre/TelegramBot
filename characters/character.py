class Character:
    name = ""
    life = 100
    board = None
    board_x = None
    board_y = None

    def __init__(self):
        pass

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
