import keyboard
from puzzle import Board
board1=Board()
board1.print_board()
print("  ")
  

  
def disable_hotkeys():
    keyboard.block_key('right')
    keyboard.block_key('left')
    keyboard.block_key('up')
    keyboard.block_key('down')  
    print("Congratulations, You have won the game")


def move_right():
    
    board1.move_right()
    board1.print_board()
    if board1.check_win():
        disable_hotkeys()

def move_left():
    board1.move_left()
    board1.print_board()
    if board1.check_win():
        disable_hotkeys()

def move_up():
    board1.move_up()
    board1.print_board()
    if board1.check_win():
        disable_hotkeys()

def move_down():
    board1.move_down()
    board1.print_board()
    if board1.check_win():
        disable_hotkeys()

def next_states():
    possible_state = board1.Next_state()
    for direction, board in possible_state:
     print(f"move {direction}")
     board.print_board()
     print("--------")

def move_stack():
 moves_stack = board1.get_moves_stack()
 for i, move in enumerate(moves_stack):
    print(f"Move {i+1}:")
    move.print_board()

keyboard.add_hotkey('right', move_right)
keyboard.add_hotkey('left', move_left)
keyboard.add_hotkey('up', move_up)
keyboard.add_hotkey('down', move_down)
keyboard.add_hotkey('L', next_states)
keyboard.add_hotkey('S', move_stack)

keyboard.wait('esc')
