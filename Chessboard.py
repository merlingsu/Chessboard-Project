import turtle

def drawChessboard(startx, starty, size):
    square_size = size // 8

    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                turtle.fillcolor("white")
            else:
                turtle.fillcolor("black")

            turtle.penup()
            turtle.goto(startx + col * square_size, starty - row * square_size)
            turtle.pendown()
            turtle.begin_fill()
            for _ in range(4):  # Draw square
                turtle.forward(square_size)
                turtle.right(90)
            turtle.end_fill()

turtle.setup(800, 400)
turtle.speed(100)
turtle.hideturtle()

drawChessboard(-350, 150, 300)
drawChessboard(50, 150, 300)
turtle.done()