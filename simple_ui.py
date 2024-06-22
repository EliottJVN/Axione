import tkinter as tk
from data_ui import *
import json

from pynput import mouse, keyboard
import pyautogui
import time


class UI(tk.Tk):
    def __init__(self):
        # Création de la fenêtre.
        tk.Tk.__init__(self)
        self.configure(bg=BG)  # f0b45f
        self.title("Simple UI")

        # Icône d'application.
        #self.iconbitmap('image/icon.ico')

        # Taille de l'écran.
        scr_l = self.winfo_screenwidth()
        scr_h = self.winfo_screenheight()

        # Gère le FullScreen.
        self.geometry("{}x{}".format(2*W +3*PADDING , H+6*OFFSET))
        
        self.Button =  []
        
        titre = tk.Label(self, text="Simple UI\nMenu",
                         font=FONT, bg=BG, fg=FONT_COLOR, justify='center')
        self.Button.append(titre) 
        
        name_action = tk.Label(self, font=FONT, fg=FONT_COLOR, bg = BG, text="macro name :", justify='right')
        self.Button.append(name_action)
        self.action_name = tk.Entry(self, font=FONT,
                               fg=FONT_COLOR, bg=BG_BT)
        self.Button.append(self.action_name)
       
        learn_butt = tk.Button(self, text='learn_macro', font=FONT,
                               fg=FONT_COLOR, bg=BG_BT, command=self.learn_action)
        self.Button.append(learn_butt)
        
        save_butt = tk.Button(self, text='save_macro', font=FONT,
                               fg=FONT_COLOR, bg=BG_BT, command=self.save_action)
        self.Button.append(save_butt)
        
        play_action = tk.Button(self, text='play_macro', font=FONT,
                               fg=FONT_COLOR, bg=BG_BT, command=self.play_action)
        self.Button.append(play_action)
        
        for i in range(len(self.Button)):
            self.Button[i].place(x=X, y=Y+i*OFFSET, height = H, width= W)
        
        label_select = tk.Label(self, font=FONT, fg=FONT_COLOR, bg = BG, text="macros saved", justify='right')
        self.select_action = tk.Listbox()
        self.load_files()
        self.select_action.place(x=X + PADDING + W, y = Y + 2*OFFSET, height = 4*H+3*PADDING, width= W)
        label_select.place(x=X + PADDING + W, y=Y+OFFSET, height = H, width= W)
     
  
    def learn_action(self):
        if self.action_name.get() == '':
            print("Please enter a name for your action.")
            return
        
        self.move_n_click = []

        # Configure le listener pour la souris
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.key_listener = keyboard.Listener(on_press=self.on_press)
        self.mouse_listener.start()
        self.key_listener.start()


    def on_click(self, x, y, button, pressed):
        if button== mouse.Button.left:
            bouton_str = 'left'
        elif button == mouse.Button.right:         
            bouton_str = 'right'
        elif button == mouse.Button.middle:
            bouton_str = 'middle'  
        else:
            raise ValueError("Bouton de souris non reconnu")
        self.move_n_click.append([[x,y], bouton_str, pressed])


    def on_press(self,key):
        # Permet de quitter les listeners
        try:
            if key.char == QUIT: 
                self.mouse_listener.stop()
                self.key_listener.stop()
            
            elif key.char == PAUSE:
                self.mouse_listener.stop()

            elif key.char == UNPAUSE:
                self.mouse_listener = mouse.Listener(on_click=self.on_click)
                self.mouse_listener.start()

            elif key.char == SAVE:
                self.save_action()
        
        except AttributeError:
            pass
        
        try:
            self.move_n_click.append([key.char])
        except:
            self.move_n_click.append([self.give_char(key)])
        
        
        

    def save_action(self):
        self.mouse_listener.stop()
        self.key_listener.stop()

        if self.action_name.get() == '':
            print("Please enter a name for your action.")
            return

        if self.move_n_click == []:
            print('Your macro is empty.')
            return
        
        print(self.move_n_click)
        try:
            with open(PATH + self.action_name.get()+'.json', 'w',encoding='UTF-8') as fichier:
                json.dump(self.move_n_click, fichier, ensure_ascii=False, indent=4)
                self.move_n_click = []
                self.load_files()
        except Exception as e:
            print(f"Une erreur s'est produite lors de la sauvegarde de la liste : {e}")

    def load_files(self):
        try:
            # Créer le dossier s'il n'existe pas déjà
            os.makedirs(PATH, exist_ok=True)
        except Exception as e:
            pass
        
        self.select_action.delete(0, tk.END)
        files = self.find_files(PATH)
        for file in files:
            self.select_action.insert(tk.END, file)

    def play_action(self):
        if self.select_action.get(self.select_action.curselection()) == '':
            print("Please select an action you want to play.")
            return
        file = PATH + self.select_action.get(self.select_action.curselection()) + '.json'
        with open(file,'r') as op_file:
            commandes = json.load(op_file)
            print (commandes)
        for line in commandes:
            print(line)
            self.executer_commande(line)
            time.sleep(SLEEP)  # Pause de 0.1 seconde entre chaque commande
        
    def executer_commande(self, commande):
        if isinstance(commande, list) and len(commande) == 1 and isinstance(commande[0], str):
            # Il s'agit d'une frappe de touche
            line = commande[0]
            if len(line) != 1:
                pyautogui.press(line)
                return
            keyboard.Controller().press(line)
            keyboard.Controller().release(line)
        
        elif isinstance(commande, list) and len(commande) == 3:
            # Il s'agit d'une commande de souris
            position, bouton, etat = commande
            x, y = position
            if etat:
                pyautogui.mouseDown(x=x, y=y, button=bouton)
            else:
                pyautogui.mouseUp(x=x, y=y, button=bouton)
        else:
            raise ValueError("Commande non reconnue")

    def find_files(self, folder):
        files = []
        with os.scandir(folder) as entries:
            for entry in entries:
                if entry.is_file():
                    a = entry.name[:-5]
                    files.append(a)
        return files


    def give_char(self,key):
        if key == keyboard.Key.space:
            key = 'space'
        elif key == keyboard.Key.enter:
            key = 'enter'
        elif key == keyboard.Key.backspace:
            key = "backspace"
        elif key == keyboard.Key.up:
            key = 'up'
        elif key == keyboard.Key.down:
            key = 'down'
        elif key == keyboard.Key.right:
            key = 'right'
        elif key == keyboard.Key.left:
            key = 'left'
        elif key == keyboard.Key.shift:
            key = 'shift'
        elif key == keyboard.Key.shift_r:
            key = 'shift_r'
        elif key == keyboard.Key.shift_l:
            key = 'shift_l'
        elif key == keyboard.Key.ctrl:
            key = 'ctrl'
        elif key == keyboard.Key.ctrl_r:
            key = 'ctrl_r'
        elif key == keyboard.Key.ctrl_l:
            key = 'ctrl_l'
        elif key == keyboard.Key.f1:
            key = 'f1'
        elif key == keyboard.Key.f2:
            key = 'f2'
        elif key == keyboard.Key.f3:
            key = 'f3'
        elif key == keyboard.Key.f4:
            key = 'f4'
        elif key == keyboard.Key.f5:
            key = 'f5'
        elif key == keyboard.Key.f6:
            key = 'f6'
        elif key == keyboard.Key.f7:
            key = 'f7'
        elif key == keyboard.Key.f8:
            key = 'f8'
        elif key == keyboard.Key.f9:
            key = 'f9'
        elif key == keyboard.Key.f10:
            key = 'f10'
        elif key == keyboard.Key.alt:
            key = 'alt'
        elif key == keyboard.Key.alt_gr:
            key = 'alt_gr'
        elif key == keyboard.Key.alt_l:
            key = 'alt_l'   
        elif key == keyboard.Key.alt_r:
            key = 'alt_r'
        return key


if __name__ == '__main__':
    simple_UI = UI()
    simple_UI.mainloop()