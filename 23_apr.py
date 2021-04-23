import tkinter as tk
from random import randint
Width = 300
Height = 200
class Ball:

    def __init__(self):
        self.R = randint(10, 30)
        self.x = randint(self.R, Width - self.R)
        self.y = randint(self.R, Height - self.R)
        self.dx, self.dy = (+2, +3)
        self.color = 'yellow'
        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R, self.y + self.R, fill=self.color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > Width or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > Height or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id,self.dx,self.dy)
# def check_inside(self):
# def check_collisine(self):

def canvas_click_handler(event):
    print('hello, world! x = ', event.x, 'y=', event.y)

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50,tick)

def main():
    global root, canvas, balls

    root = tk.Tk()
    root.geometry(str(Width) +'x'+ str(Height))
    canvas = tk.Canvas(root)
    canvas.pack(anchor= 'nw', fill = tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)

    balls = [Ball() for i in range(5)]

    tick()
    root.mainloop()
if __name__ == "__main__":
    main()
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
