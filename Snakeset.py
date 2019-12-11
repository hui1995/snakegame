import tkinter.messagebox
import threading
import time
from foodset import Food
##贪吃蛇初始设置
class Snake(threading.Thread):
    '''class Snake use to create snake and response action'''

    def __init__(self, gui, queue):
        threading.Thread.__init__(self)
        self.gui = gui
        self.queue = queue
        self.daemon = True
        self.points_score = 0
        self.snake_points = [(495, 55), (485, 55), (475, 55), (465, 55), (455, 55)]
        self.food = Food(queue)
        self.direction = 'Left'
        self.start()

##移动设置
    def run(self):
        if self.gui.is_game_over:
            self._delete()
        while not self.gui.is_game_over:
            self.queue.put({'move': self.snake_points})
            time.sleep(0.2)
            self.move()

    def key_pressed(self, e):
        key = e.keysym
        key_dict = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if key_dict.__contains__(key) and not key == key_dict[self.direction]:
            self.direction = e.keysym
##分数设置
    def move(self):
        new_snake_point = self.calculate_new_coordinates()
        if self.food.position == new_snake_point:
            add_snake_point = self.calculate_new_coordinates()
            self.snake_points.append(add_snake_point)
            self.points_score += 1
            self.queue.put({'points_score': self.points_score})
            self.food.make_food()
        else:
            self.snake_points.pop(0)
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)
##方向键移动设置
    def calculate_new_coordinates(self):
        last_x, last_y = self.snake_points[-1]
        if self.direction == 'Up':
            new_snake_point = last_x, last_y - 10
        elif self.direction == 'Down':
            new_snake_point = last_x, last_y + 10
        elif self.direction == 'Left':
            new_snake_point = last_x - 10, last_y
        elif self.direction == 'Right':
            new_snake_point = last_x + 10, last_y
        return new_snake_point
##gameover检查
    def check_game_over(self, snake_point):
        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            message = tkinter.messagebox.showinfo("Game Over", "your score is %d" % self.points_score) ##gameover检查并弹窗分数
            self.queue.put({'game_over': True})