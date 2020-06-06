from constants import SEG_SIZE

class Segment():
    """ Single snake segment """
    def __init__(self, canvas, x, y):
        self.instance = canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="#46866f")