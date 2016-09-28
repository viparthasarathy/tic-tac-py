class Board(object):
    def __init__(self):
        self.tiles = []
        for _ in range(3):
            self.tiles.append([" ", " ", " "])
        self.turn = 0

    def display(self):
      for row in self.tiles:
          print(" %s | %s | %s " % (row[0], row[1], row[2]))
          print("-----------")

    def is_winner(self):
        
    def is_over(self):
        return self.is_winner or self.is_tie

    def is_tie(self):
        space = False
        for row in self.tiles:
            for tile in row:
                if tile == " ":
                    space = True
        return space

    def play(self):
