from tkinter import *
from tkinter import ttk
import random
import subprocess

WIDTH = 1400
HEIGHT = 800
SPEED = 100
SPACE_SIZE = 20
BODY_SIZE = 3
SNAKE = "#F0FFFF"
FOOD = "#00BFFF"
BACKGROUND = "#87CEEB"


class Snake:
	def __init__(self):
		self.body_size = BODY_SIZE
		self.coordinates = []
		self.squares = []

		for i in range(0, BODY_SIZE):
			self.coordinates.append([0, 0])

		for x, y in self.coordinates:
			square = area.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE, tag="snake")
			self.squares.append(square)

class Food:
	def __init__(self):
		x = random.randint(0, (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
		y = random.randint(0, (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

		self.coordinates = [x, y]

		area.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD, tag="food")

def next_turn(snake, food):

	x, y = snake.coordinates[0]

	if direction == "up":
		y -= SPACE_SIZE
	elif direction == "down":
		y += SPACE_SIZE
	elif direction == "left":
		x -= SPACE_SIZE
	elif direction == "right":
		x += SPACE_SIZE

	snake.coordinates.insert(0, (x, y))
	square = area.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE)
	snake.squares.insert(0, square)

	if x == food.coordinates[0] and y == food.coordinates[1]:

		global score
		score += 10
		counter.config(text="Счёт: {}".format(score))
		area.delete("food")
		food = Food()

	else:
		del snake.coordinates[-1]
		area.delete(snake.squares[-1])
		del snake.squares[-1]

	if check_collisions(snake):
		game_over()
	else:
		window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

	global direction

	if new_direction == 'left':
		if direction != 'right':
			direction = new_direction
	elif new_direction == 'right':
		if direction != 'left':
			direction = new_direction
	elif new_direction == 'up':
		if direction != 'down':
			direction = new_direction
	elif new_direction == 'down':
		if direction != 'up':
			direction = new_direction

def check_collisions(snake):

	x, y = snake.coordinates[0]

	if x < 0 or x >= WIDTH:
		return True
	elif y < 0 or y >= HEIGHT:
		return True

	for body_part in snake.coordinates[1:]:
		if x == body_part[0] and y == body_part[1]:
			return True

	return False

def game_over():
	area.delete(ALL)
	area.create_text(area.winfo_width()/2, area.winfo_height()/2, font=('Segoe print', 70), text="Игра окончена", fill="red", tag="gameover")

def go_back():
	window.destroy()
	subprocess.Popen(["python", "zmeika.py"])

def restart_game():
	window.destroy()
	subprocess.Popen(["python", "play.py"])

if __name__ == '__main__':

	window = Tk()
	window.title("Змейка")
	window.configure(bg='#F0F8FF')
	window.attributes('-fullscreen', True)

	for widget in window.winfo_children():
		widget.destroy()

	score = 0
	direction = 'down'

	counter = Label(window, text="Счёт: {}".format(score), font=('Segoe print', 20), background='#F0F8FF')
	counter.pack(anchor='ne')

	area = Canvas(window, bg=BACKGROUND, height=HEIGHT, width=WIDTH)
	area.pack()

	go_btn = ttk.Button(window, text="<---", command=go_back)
	go_btn.place(x=0, y=0, anchor="nw", width=80, height=40)

	restart_btn = ttk.Button(window, text='↻', command=restart_game)
	restart_btn.place(x=130, y=20, anchor="c", width=80, height=40)

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
	food = Food()

	next_turn(snake, food)

	window.mainloop()


