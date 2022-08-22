import requests
from tkinter import *
import json

class App:

    def __init__(self):
        self.janela = Tk()
        self.janela.title("Filmes")
        self.janela.resizable(0, 0)
        self.janela.geometry("400x400")



        self.framme = Frame(self.janela)
        self.framme.pack()

        self.texto = Entry(self.framme, font="Arial 16", width=20)
        self.texto.grid(row=0, column=0)

        self.pesquisar = Button(self.framme, font="Arial 12", text="Procurar", command=self.pesquisar)
        self.pesquisar.grid(row=0, column=1, )

        self.lista = Listbox(self.janela)
        self.lista.pack(fill=BOTH, expand=True)

        self.janela.mainloop()

    def pesquisar(self):
        requisicao = requests.get("http://www.omdbapi.com/?s=starwars&apikey=dbb11bd6")
        #s é pedido um titulo para pegar o filme. É um parametro. & significa passar um parametro novo
        # s - titulo
        # y - ano
        dict = json.loads(self.requisicao.text)

#

#http://www.omdbapi.com/?

App()