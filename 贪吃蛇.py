'''
注意，由于是多线程，begin每次只能点一下，否则会出双线程无法操作
'''
from tkinter import *
import queue
from GUImod import GUI
from Snakeset import Snake

def snake():
    global gui, q
    snake = Snake(gui, q)
    gui.bind('<Key-Left>', snake.key_pressed)
    gui.bind('<Key-Right>', snake.key_pressed)
    gui.bind('<Key-Up>', snake.key_pressed)
    gui.bind('<Key-Down>', snake.key_pressed)
##主函数
def main():
    global gui, q, main
    q = queue.Queue()
    gui = GUI(q)
    gui.title("我的贪吃蛇")
    Button(gui, text='Begin', command=snake).pack()  ##开始按钮设置
    gui.mainloop()


if __name__ == '__main__':
    main = main()
    main

