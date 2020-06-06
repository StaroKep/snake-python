from constants import WIDTH, HEIGHT


def create_game_over_text(canvas):
    return canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER!", font='Arial 20', fill='red', state='hidden')


def create_restart_game_test(canvas):
    return canvas.create_text(WIDTH/2, HEIGHT - HEIGHT/3, font='Arial 30', fill='white', text="Click here to restart", state='hidden')


def set_state(canvas, item, state):
    canvas.itemconfigure(item, state=state)