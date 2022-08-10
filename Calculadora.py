
from tkinter import *

class App:

    def __init__(self):
        
        self.janela = Tk()
        self.janela.title("Calculadora")
        self.janela.resizable(0,0)
        self.janela.config(background="#1d2f38", pady=10, padx=6)
        
        
        self.tela_numeros = Entry(self.janela, font="arial 30 bold", foreground="white", background="#1d2f38", width=17)
        self.tela_numeros.pack()

        self.framme = Frame(self.janela)
        self.framme.pack()

        self.botao_7 = Button(self.framme, background="orange", text="7", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("7"))
        self.botao_8 = Button(self.framme, background="orange", text="8", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("8"))
        self.botao_9 = Button(self.framme, background="orange", text="9", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("9"))
        self.botao_4 = Button(self.framme, background="orange", text="4", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("4"))
        self.botao_5 = Button(self.framme, background="orange", text="5", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("5"))
        self.botao_6 = Button(self.framme, background="orange", text="6", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("6"))
        self.botao_1 = Button(self.framme, background="orange", text="1", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("1"))
        self.botao_2 = Button(self.framme, background="orange", text="2", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("2"))
        self.botao_3 = Button(self.framme, highlightcolor="blue", background="orange", text="3", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("3"))

        self.botao_divisao = Button(self.framme, background="orange", text="/", bd=0, foreground="black", font="arial 20 bold", width=5,height=3, command=lambda: self.touch("/"))
        self.botao_multi = Button(self.framme, background="orange", text="*", bd=0, foreground="black", font="arial 20 bold", width=5,height=3, command=lambda: self.touch("*"))
        self.botao_menos = Button(self.framme, background="orange", text="-", bd=0, foreground="black", font="arial 20 bold", width=5,height=3, command=lambda: self.touch("-"))
        self.botao_mais = Button(self.framme, background="orange", text="+", bd=0, foreground="black", font="arial 20 bold", width=5,height=3, command=lambda: self.touch("+"))

        self.botao_limpar = Button(self.framme, background="orange", text="C", bd=0, foreground="black", font="arial 20 bold", width=5,height=3, padx=3, command= self.clean)
        self.botao_0 = Button(self.framme, background="orange", text="0", bd=0, foreground="white", font="arial 20 bold", width=5,height=3, padx=3, command=lambda: self.touch("0"))
        self.botao_igual = Button(self.framme, background="#ffaa00", text="=", bd=0, foreground="#005eff", font="arial 20 bold", width=5,height=3,padx=3,  command= self.calculo)
        

        self.botao_7.grid(row=0, column=0)
        self.botao_8.grid(row=0, column=1)
        self.botao_9.grid(row=0, column=2)
        self.botao_divisao.grid(row=0, column=3)

        self.botao_4.grid(row=1, column=0)
        self.botao_5.grid(row=1, column=1)
        self.botao_6.grid(row=1, column=2)
        self.botao_multi.grid(row=1, column=3)

        self.botao_1.grid(row=2, column=0)
        self.botao_2.grid(row=2, column=1)
        self.botao_3.grid(row=2, column=2)
        self.botao_menos.grid(row=2, column=3)

        self.botao_limpar.grid(row=3, column=0)
        self.botao_0.grid(row=3, column=1)
        self.botao_igual.grid(row=3, column=2)
        self.botao_mais.grid(row=3, column=3)

        self.janela.mainloop()


    def touch(self, num):
        self.tela_numeros.insert(END, num)
    def clean(self):
        self.tela_numeros.delete(0, END)
    
    def calculo(self):
        try:
            total = eval(self.tela_numeros.get())
        except:
            total = "Erro no cálculo :("
        finally:
            self.clean()
            self.tela_numeros.insert(0, str(total))
        
App()
