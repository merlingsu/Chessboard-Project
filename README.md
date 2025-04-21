# Chessboard-Project
def draw_chessboard(size):
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                print("⬛", end=" ")
            else:
                print("⬜", end=" ")
        print()

# Draw an 8x8 chessboard
draw_chessboard(8)
