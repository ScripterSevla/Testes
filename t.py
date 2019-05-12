from tkinter import *


class T (Frame):
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master=master, *args, **kwargs)

        text_var = StringVar()
        text_var.set('PRIMEIRO')
        dois_var = StringVar()
        dois_var.set('DOIS')

        self.teste_entry = Entry(self, name='text_var', textvariable=text_var)
        self.teste_entry.bind('<FocusIn>', self.ex_event)
        self.teste_entry.bind('<FocusOut>', self.ex_event)
        self.teste_entry.grid(row=0)

        self.dois_entry = Entry(self, name='dois_var', textvariable=dois_var)
        self.dois_entry.bind('<FocusIn>', self.ex_event)
        self.dois_entry.bind('<FocusOut>', self.ex_event)

        self.dois_entry.grid(row=1)
        self.grid(row=0)



    @staticmethod
    def ex_event(e):
        if str(e.type) is 'FocusIn':
            e.widget.delete(0, 'end')
            if str(e.widget).endswith('dois_var'):
                e.widget.configure(show='*')
                return None
            return None


        if str(e.type) is 'FocusOut':
            if e.widget.get() is '':

                if str(e.widget).endswith('text_var'):
                    e.widget.insert('end', 'Username')
                    return None


                if str(e.widget).endswith('dois_var'):
                    e.widget.configure(show='')
                    e.widget.insert('end', 'Password')
                return None
            return None
        return None









t = T()
t.mainloop()