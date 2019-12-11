import random
class Food():
    '''class Food use to make food'''

    def __init__(self, queue):
        self.queue = queue
        self.make_food()

    def make_food(self):
        x = random.randrange(5, 480, 10)
        y = random.randrange(5, 295, 10)
        self.position = x, y
        self.exppos = x - 5, y - 5, x + 5, y + 5
        self.queue.put({'food': self.exppos})