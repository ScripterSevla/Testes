from Gui.Raiz.Root import *


class Login(Frame):
    def __init__(self, master=Root, *args, **kwargs):
        Frame.__init__(self, master=master, *args, **kwargs)
        self.config(bg="black")
        self.text = Label(self, text="ESTE È O EXEMPLO CORRETO")
        self.text.grid(row=0)
        self.grid(row=0, sticky=NSEW)