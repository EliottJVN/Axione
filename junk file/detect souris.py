from pynput import mouse, keyboard

# Variable pour stocker la position de la souris
mouse_position = None

# Fonction appelée lorsque la touche T est pressée
def on_press(key):
    try:
        if key.char == 't':
            # Imprime la position actuelle de la souris
            if mouse_position:
                print(f"Position de la souris: {mouse_position}")

        elif key.char == "p":
            quit()
        
    except AttributeError:
        pass

# Fonction appelée lorsque la souris se déplace
def on_move(x, y):
    global mouse_position
    mouse_position = (x, y)

# Configure le listener pour la souris
mouse_listener = mouse.Listener(on_move=on_move)
mouse_listener.start()

# Configure le listener pour le clavier
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Attendre que les listeners se terminent
mouse_listener.join()
keyboard_listener.join()