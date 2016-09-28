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
