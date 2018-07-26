from tkinter import *
import random
import time
from ball import Ball
from paddle import Paddle


tk = Tk()
tk.title("Games")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
    if ball.floor == False:
        ball.draft()
        paddle.draft()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
