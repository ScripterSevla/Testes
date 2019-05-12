from tkinter import *



class Root(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args,  **kwargs)

        self.grid()


