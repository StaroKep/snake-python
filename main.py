import random
from tkinter import Tk, Canvas
from constants import WIDTH, HEIGHT, SEG_SIZE, IN_GAME
from snake import Snake
from segment import Segment
from helpers import create_game_over_text, create_restart_game_test, set_state


# Helper functions
def create_apple():
    """ Создание яблока, которое будет съедено """
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
    BLOCK = canvas.create_oval(posx, posy, posx+SEG_SIZE, posy+SEG_SIZE, fill="#e46764")


def on_restart_game_button_click(event):
    global IN_GAME
    snake.reset_snake()
    IN_GAME = True
    canvas.delete(BLOCK)
    canvas.itemconfigure(restart_text, state='hidden')
    canvas.itemconfigure(game_over_text, state='hidden')
    start_game()


def start_game():
    global snake
    create_apple()
    snake = create_snake()
    # Reaction on keypress
    canvas.bind("<KeyPress>", snake.change_direction)
    main()


# Создаем змейку из сегментов
def create_snake():
    segments = [Segment(canvas, SEG_SIZE, SEG_SIZE),
                Segment(canvas, SEG_SIZE*2, SEG_SIZE),
                Segment(canvas, SEG_SIZE*3, SEG_SIZE)]
    return Snake(canvas, segments)


def main():
    """ Управление игровым процессом """
    global IN_GAME

    # Если игра не окончена
    if IN_GAME:
        # Передвигаем змейку
        snake.move()

        # Получаем координаты головы змейки
        head_coords = canvas.coords(snake.segments[-1].instance)
        x1, y1, x2, y2 = head_coords

        # Проверяем ударилась ли змейка о стенку
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False

        # Если координаты головы совпадают с координатами яблока (змейка съела яблоко)
        elif head_coords == canvas.coords(BLOCK):
            snake.add_segment()
            canvas.delete(BLOCK)
            create_apple()

        # Добавляем проверку, что змейка не съела сама себя
        else:
            for index in range(len(snake.segments)-1):
                if head_coords == canvas.coords(snake.segments[index].instance):
                    IN_GAME = False

        # Обеспечиваем зацикленность игры
        # Через 150 мс эта функция выполнится еще раз
        root.after(150, main)

    # Если игра окончена (проигрыш), показываем текст и кнопку перезапуска
    else:
        set_state(canvas, restart_text, 'normal')
        set_state(canvas, game_over_text, 'normal')

# --- --- --- --- --- ---

# Настраиваем окно tkinter
root = Tk()
root.title("Snake game")

# Создаем canvas с определенными параметрами
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="#9eccb3")
canvas.pack()

# Т.к. змейка сразу начинает движение,
# надо сразу сфокусироваться на canvas
canvas.focus_set()

# Сразу содаем скрытые текстовки о проигрыше
game_over_text = create_game_over_text(canvas)
restart_text = create_restart_game_test(canvas)
canvas.tag_bind(restart_text, "<Button-1>", on_restart_game_button_click)

start_game()
root.mainloop()