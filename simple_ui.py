import os
import tkinter as tk
from data_ui import *

from pynput import mouse, keyboard

class UI(tk.Tk):
    def __init__(self):
        # Création de la fenêtre.
        tk.Tk.__init__(self)
        self.configure(bg=BG)  # f0b45f
        self.title("Simple UI")

        # Icône d'application.
        # self.iconbitmap('image/icone.ico')

        # Taille de l'écran.
        scr_l = self.winfo_screenwidth()
        scr_h = self.winfo_screenheight()

        # Gère le FullScreen.
        self.geometry("{}x{}".format(int(scr_l/2), int(scr_h/2)+250))
        self.full_scr = False
        self.attributes("-fullscreen", self.full_scr)
        self.resizable(width=False, height=False)
        self.bind("<F11>", self.toggle_scr)
        
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
        
        
        self.select_action = tk.Listbox()
        self.load_files()
        self.select_action.place(x=X + 10 + W, y = Y + 2*OFFSET, height = 4*H+3*PADDING, width= W)

    def toggle_scr(self, event):
        """FullScreen bind avec <F11>"""
        if self.full_scr:
            self.full_scr = False
        else:
            self.full_scr = True
        self.attributes("-fullscreen", self.full_scr)

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
        self.move_n_click.append([(x,y),button,pressed])
        print([(x,y),button,pressed])

    def on_press(self,key):
        print(key)
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
            
            else:
                self.move_n_click.append([key])
        except AttributeError:
            pass

    def save_action(self):
        self.mouse_listener.stop()
        self.key_listener.stop()

        if self.action_name.get() == '':
            print("Please enter a name for your action.")
            return

        if self.move_n_click == []:
            print('Your macro is empty.')
            return
        
        try:
            with open('save/'+self.action_name.get()+'.txt', 'w') as fichier:
                for element in self.move_n_click:
                    fichier.write(f"{element}\n")
            print(f"La liste a été sauvegardée avec succès dans le fichier.")
            self.move_n_click = []
            self.load_files()
        except Exception as e:
            print(f"Une erreur s'est produite lors de la sauvegarde de la liste : {e}")

    def load_files(self):
        self.select_action.delete(0, tk.END)
        files = self.find_files('save/')
        for file in files:
            self.select_action.insert(tk.END, file)

    def play_action(self):
        if self.select_action.get() == '':
            print("Please select an action you want to play.")
            return
    
    def find_files(self, folder):
        files = []
        with os.scandir(folder) as entries:
            for entry in entries:
                if entry.is_file():
                    a = entry.name[:-4]
                    files.append(a)
        return files

if __name__ == '__main__':
    simple_UI = UI()
    simple_UI.mainloop()