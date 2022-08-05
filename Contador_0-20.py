import tkinter

class App:
    def __init__(self):

        self.valor = 20

        self.janela = tkinter.Tk()
        #atribuindo dentro da var janela as propriedades da janela 
        self.janela.title("Marcador")
        self.janela.minsize(width=380, height=150)
        self.janela.maxsize(width=380, height=150)


        self.texto= tkinter.Label(self.janela, text="20",font="Arial 50 bold", pady=10)
        #coloca dentro da janela. 1º parametro é este para label
        self.texto.pack()
        

        self.framee= tkinter.Frame(self.janela,height=200, background="grey",borderwidth=4)
        self.framee.pack()

        self.botao_menos = tkinter.Button(self.framee, text="Menos", font="Arial 10 bold",foreground="white", bg="red",width=20, command=self.menos)
        #joga dentro do framee em vez de janela
        self.botao_menos.pack(side="left")

        self.botao_mais = tkinter.Button(self.framee, text="Mais", font="Arial 10 bold",foreground="white", bg="green",width=20, command=self.mais)
        self.botao_mais.pack(side="left")


        self.janela.mainloop()

    def mais(self):
        if self.valor < 20:
            self.valor += 1
            self.texto.config(text=self.valor)

    def menos(self):
        if self.valor > 0:
            self.valor -= 1
            self.texto.config(text=self.valor)

App()
