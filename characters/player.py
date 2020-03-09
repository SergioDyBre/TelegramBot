from characters.character import Character


class Player(Character):
    id = None
    name = ""
    life = 100
    board = None
    board_x = None
    board_y = None

    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
