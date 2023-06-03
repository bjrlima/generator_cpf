from tkinter import *
from generator import validation, generation

class windom():

    def __init__(self):
        self.windon_generator = Tk()
        self.windon_cpf()
        self.objects()
        self.windon_generator.mainloop()

    def windon_cpf(self):
        self.windon_generator.title('Generator')
        self.windon_generator.config(bg = 'white')
        width = 330
        height = 200
        tela_largura = self.windon_generator.winfo_screenwidth()
        tela_altura = self.windon_generator.winfo_screenheight()
        x = (tela_largura/2) - (width/2)
        y = (tela_altura/2) - (height/2)
        self.windon_generator.geometry('%dx%d+%d+%d' %(width,height,x,y))
        self.windon_generator.resizable(0,0)

    def objects(self):
        self.entry_cpf = Entry (self.windon_generator, font=('Microsoft Yahei UI Light', 12), fg = 'black', bd = 2)
        self.entry_cpf.place (relx= 0.1, rely = 0.25, relwidth = 0.8, relheight = 0.14)

        self.button_validate = Button (self.windon_generator, text = 'VALIDAR CPF', cursor = 'hand2', bd = 0, bg = 'black', command = lambda: self.validate()) 
        self.button_validate.configure(font = ('Microsoft Yahei UI Light', 8, 'bold'), fg = 'white', activebackground = 'red', activeforeground = 'white') 
        self.button_validate.place(relx= 0.1, rely = 0.6, relwidth = 0.35, relheight = 0.15)

        self.button_validate = Button (self.windon_generator, text = 'GERAR CPF', cursor = 'hand2', bd = 0, bg = 'black', command = lambda: self.generate()) 
        self.button_validate.configure(font = ('Microsoft Yahei UI Light', 8, 'bold'), fg = 'white', activebackground = 'red', activeforeground = 'white') 
        self.button_validate.place(relx= 0.55, rely = 0.6, relwidth = 0.35, relheight = 0.15)

        self.text = Label(self.windon_generator, text= 'Validador e Gerador de CPF', bg = 'white', fg ='black')
        self.text.configure(font = ('Microsoft Yahei UI Light', 10, 'bold'),)
        self.text.place(relx= 0.15, rely = 0.1, relwidth = 0.7, relheight = 0.08)

        self.text_info = Label(self.windon_generator, text= '', bg = 'white', fg ='black')
        self.text_info.configure(font = ('Microsoft Yahei UI Light', 9, 'bold'),)
        self.text_info.place(relx= 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.08)

    def validate(self):
        if self.entry_cpf.get() == '':
            self.text_info.config(text='Digite um CPF', fg ='red')
        else:
            if validation.validate(self.entry_cpf.get()) == True:
                self.text_info.config(text='CPF Válido', fg ='green')
            else:
                self.text_info.config(text='CPF Inválido', fg ='red')

    def generate(self):
        self.entry_cpf.delete(0, END)
        self.entry_cpf.insert(0,generation.generate())

windom()