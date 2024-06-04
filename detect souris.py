from pynput import mouse

def on_move(x, y):
    print(f'Position: ({x}, {y})')

# Collect events until released
with mouse.Listener(on_move=on_move) as listener:
    listener.join()