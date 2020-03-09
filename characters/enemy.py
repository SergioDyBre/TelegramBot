from random import randint

from characters.character import Character


class Enemy(Character):
    name = ""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def make_move(self):
        # aquí de momento vamos a randomizar o movemento do enemigo, máis adiante faremos a predicción de movemento en base ao pj pra atacalo
        move = randint(0, 3)
        if move == 0:
            self.move_up()
        elif move == 1:
            self.move_right()
        elif move == 2:
            self.move_down()
        elif move == 3:
            self.move_left()
