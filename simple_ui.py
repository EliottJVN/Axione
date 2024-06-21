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
        self.full_scr = True
        self.attributes("-fullscreen", self.full_scr)
        self.resizable(width=False, height=False)
        self.bind("<F11>", self.toggle_scr)

        titre = tk.Label(self, text="Simple UI\nMenu",
                         font=FONT, bg=BG, fg=FONT_COLOR, justify='center')
        titre.place(relheight=0.25, relwidth=1)


        self.action_name = tk.Entry(self, font=FONT,
                               fg=FONT_COLOR, bg=BG_BT)
        self.learn_butt = tk.Button(self, text='learn_action', font=FONT,
                               fg=FONT_COLOR, bg=BG_BT, command=self.learn_action)
        self.save_butt = tk.Button(self, text='save_action', font=FONT,
                               fg=FONT_COLOR, bg=BG_BT, command=self.save_action)
        
        self.select_action = tk.Listbox()
        self.play_action = tk.Button()

        
        
        self.action_name.pack()
        self.learn_butt.pack()
        self.save_butt.pack()

        self.select_action.pack()
        self.play_action.pack()
        #ard_ri = tk.Button(self, text='Ard-Ri', font=pol_t,
        #                   fg=col, bg="#fcc461", command=self.V1)
        #ard_ri.place(anchor="n", height=size_w,
        #            width=size_h, relx=0.5, rely=0.28)

        # hnefatafl = tk.Label(self, text="Hnefatafl:",
        #                      font=pol_t, bg="#d38008", fg=col, justify='center')
        # #hnefatafl_v1.place(anchor="ne", height=size_w,
        #                    width=size_h/2 - 5, relx=0.5, rely=0.84, x=-5)

        size_w = 60
        size_h = 350


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
                self.mouse_listener.stop()
                self.key_listener.stop()
                self.save_action()
            
            else:
                self.move_n_click.append([key])
        except AttributeError:
            pass

    def save_action(self):
        if self.action_name.get() == '':
            print("Please enter a name for your action.")
            return
       
        try:
            with open('save/'+self.action_name.get()+'.txt', 'w') as fichier:
                for element in self.move_n_click:
                    fichier.write(f"{element}\n")
            print(f"La liste a été sauvegardée avec succès dans le fichier.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la sauvegarde de la liste : {e}")

        
if __name__ == '__main__':
    simple_UI = UI()
    simple_UI.mainloop()