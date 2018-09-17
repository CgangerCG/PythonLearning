import turtle , datetime
def gap():
    turtle.penup()
    turtle.fd(5)
def drawline(math0):
    gap()
    turtle.pendown() if math0 else turtle.penup()
    turtle.fd(50)
    gap()
    turtle.left(90)

def onedraw(math):
    if math in [2,3,4,5,6,8,9]:
        drawline(True)
    else:
        drawline(False)
    if math in [0,1,2,3,4,7,8,9]:
        drawline(True)
    else:
        drawline(False)
    if math in [0,2,3,5,6,7,8,9]:
        drawline(True)
    else:
        drawline(False)
    if math in [0,4,5,6,8,9]:
        drawline(True)
    else:
        drawline(False)
    turtle.right(90)

    if math in [0,2,6,8]:
        drawline(True)
    else:
        drawline(False)
    if math in [0,2,3,5,6,8,9]:
        drawline(True)
    else:
        drawline(False)
    if math in [0,1,3,4,5,6,7,8,9]:
        drawline(True)
    else:
        drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawall(date):
    for i in date:
        if i == "+" :
            turtle.pencolor("black")
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.fd(40)
        elif i == "-" :
            turtle.pencolor("black")
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == "="   :
            turtle.pencolor("black")

            turtle.write('日', font=("Arial", 18, "normal"))
            turtle.fd(40)
        else:
            turtle.color("red")
            onedraw(eval(i))


def main():
    turtle.setup(1000,500,300,300)
    turtle.penup()
    turtle.pensize(5)
    turtle.fd(-400)
    turtle.speed(500)
    drawall(datetime.datetime.now().strftime('%Y+%m-%d='))
    turtle.hideturtle()

main()
