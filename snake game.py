from tkinter import *
import random

GAMEWIDTH = 700
GAMEHEIGHT = 700
SPACESIZE = 50
BODYPARTS = 3

SNAKECOLOR = "#00FF00"
FOODCOLOR = "#FF0000"
BACKGROUNDCOLOR = "#000000"
SPEED = 1000

class Snake:
    def __init__(self):
        self.body_size = BODYPARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODYPARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACESIZE, y + SPACESIZE, fill=SNAKECOLOR, tag="snake")
            self.squares.append(square)

class FoodA:
    def __init__(self):
        x = random.randint(0, (GAMEWIDTH // SPACESIZE) - 1) * SPACESIZE
        y = random.randint(0, (GAMEHEIGHT // SPACESIZE) - 1) * SPACESIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACESIZE, y + SPACESIZE, fill=FOODCOLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACESIZE
    elif direction == "down":
        y += SPACESIZE
    elif direction == "left":
        x -= SPACESIZE
    elif direction == "right":
        x += SPACESIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACESIZE, y + SPACESIZE, fill=SNAKECOLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = FoodA()
    else:
        del snake.coordinates[-1]
        if check_collision(snake):
            game_over()
        else:
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_collision(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAMEWIDTH:
        return True
    if y < 0 or y >= GAMEHEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(GAMEWIDTH/2, GAMEHEIGHT/2, text="Game Over", fill="red", font=("consolas", 70))

window = Tk()
window.title("Snake Game")
window.resizable(False, False)
score = 0
direction = 'down'
label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()
canvas = Canvas(window, bg=BACKGROUNDCOLOR, height=GAMEHEIGHT, width=GAMEWIDTH)
canvas.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
snake = Snake()
food = FoodA()
next_turn(snake, food)
window.mainloop()
