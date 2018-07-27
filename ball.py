import random


class Ball:
    """docstring for Ball."""

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvasHeight = self.canvas.winfo_height()
        self.canvasWidth = self.canvas.winfo_width()
        self.floor = False

    def hitPaddle(self, pos):
        posPaddle = self.canvas.coords(self.paddle.id)
        if pos[2] >= posPaddle[0] and pos[0] <= posPaddle[2]:
            if pos[3] >= posPaddle[1] and pos[1] <= posPaddle[3]:
                return True
        return False


    def draft(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 3
        if pos[1] <= 0:
            self.y = 3
        if pos[2] >= self.canvasWidth:
            self.x = -3
        if pos[3] >= self.canvasHeight:
            # self.y = -3*/
            self.floor == True
        if self.hitPaddle(pos) == True:
            self.y = -3
