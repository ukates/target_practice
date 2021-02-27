from tkinter import *
import random

root = Tk()
root.geometry('700x700')
myCanvas = Canvas(root, width=700, height=700, bg='blue', highlightthickness=0, borderwidth=0)
myCanvas.pack(fill='both', side='right', expand=True)


def create_circle(x, y, r, canvasName):  # center coordinates, radius
    global center_x, center_y, radius
    center_x = x
    center_y = y
    radius = r
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill="white")


def click_circle(event_origin):
    global xc, yc
    random_x = random.randint(50, 650)
    random_y = random.randint(50, 650)
    xc = event_origin.x
    yc = event_origin.y
    if in_circle(center_x, center_y, radius, xc, yc):
        myCanvas.delete("all")
        create_circle(random_x, random_y, 20, myCanvas)
        myCanvas.create_oval(random_x - 10, random_y - 10, random_x + 10, random_y + 10, fill="red")
        myCanvas.create_oval(random_x - 5, random_y - 5, random_x + 5, random_y + 5, fill="white")


def in_circle(circle_x, circle_y, r, x, y):
    if ((x - circle_x) * (x - circle_x) +
            (y - circle_y) * (y - circle_y) <= r * r):
        return True
    else:
        return False


create_circle(350, 350, 20, myCanvas)

root.bind("<Button 1>", click_circle)
root.mainloop()

if in_circle(center_x, center_y, radius, xc, yc):
    print("inside")
else:
    print("outside")
