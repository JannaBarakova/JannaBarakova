import tkinter as tk
from random import randint
Width = 300
Height = 200
def canvas_click_handler(event):
    print('hello, world! x = ', event.x, 'y=', event.y)

def tick():
    global x,y, dx, dy
    x +=dx
    y +=dy
    if x+R > Width or x-R<=  0:
        dx =-dx
    if y+R > Height or y-R<=  0:
        dy =-dy
    canvas.move(ball_id,dx,dy)
    root.after(50,tick)

def main():
    global root, canvas
    global ball_id, x,y,dx,dy, R

    root = tk.Tk()
    root.geometry(str(Width) +'x'+ str(Height))
    canvas = tk.Canvas(root)
    canvas.pack(anchor= 'nw', fill = tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)

    R = randint(20,50)
    x = randint(R, Width-R)
    y = randint(R, Height-R)
    dx, dy = (+2, +3)
    ball_id= canvas.create_oval(x-R, y-R, x+R, y+R, fill= 'green')

    tick()
    root.mainloop()
if __name__ == "__main__":
    main()

