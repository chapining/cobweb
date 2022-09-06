import turtle as trl

def draw_cobweb(length1, length2, length3, length4):
    i = 0
    while i != 8:
        trl.forward(850)
        trl.left(180)
        trl.forward(850)
        trl.right(135)
        i += 1
    i = 0
    trl.forward(length1)
    trl.left(112.5)

    while i != 8:
        trl.forward(267.88)
        trl.left(45)
        i += 1
    i = 0

    trl.left(67.5)
    trl.forward(length1)
    trl.left(180)

    trl.forward(length2)
    trl.left(112.5)
    while i != 8:
        trl.forward(153.07)
        trl.left(45)
        i += 1
    i = 0

    trl.right(112.5)
    trl.forward(length1 - length2)

    while i != 8:
        trl.left(112.5)
        trl.forward(267.88 / 2)
        trl.left(90)
        trl.forward(323.36)
        trl.right(157.5)
        trl.forward(length1)
        i += 1
    i = 0

    trl.left(112.5)
    while i != 8:
        trl.forward(267.88)
        trl.left(45)
        i += 1
    i = 0

    trl.right(45)
    while i != 8:
        trl.forward(646.72)
        trl.left(135)
        trl.forward(646.72)
        trl.forward(267.88)
        i += 1
    i = 0



# настройка
trl.screensize(2000,2000)
trl.goto(0, 0)
trl.shape("turtle")
trl.speed(5)
length1 = 350
length2 = 200
length3 = 100
length4 = 150

draw_cobweb(length1, length2, length3, length4)
trl.done()
