from tkinter import *
import random
import time
from ball import Ball
from paddle import Paddle


"""Zadania strona 217"""
"""Zadanie 1: Opóżnienie rozpoczęcia gry """
"""Zadanie 2: Napisanie tekstu GAME OVER po tym jak piłka spadnie na podłogę"""
"""Zadanie 3: Przyśpieszanie piłki po odbicu od paletki"""
"""Zadanie 4: zapisywanie wyniku"""

tk = Tk()
tk.title("Games")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

startGame = False

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')


while 1:
    if ball.floor == False:
        ball.draft()
        paddle.draft()

    tk.update_idletasks()
    tk.update()

    if startGame == False:
        time.sleep(1)
        startGame = True
    
    time.sleep(0.01)
