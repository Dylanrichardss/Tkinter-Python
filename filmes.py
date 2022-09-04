import requests
from tkinter import *
import json
import PIL

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
        self.pesquisar.grid(row=0, column=1)

        self.lista = Listbox(self.janela, width=0)
        self.lista.winfo_toplevel()
        self.lista.pack(fill=BOTH, expand=True)

        self.janela.bind('<ENTER>', self.pesquisar)

        self.janela.mainloop()


    def pesquisar(self, event):
        try:
            requisicao = requests.get("http://www.omdbapi.com/?t=" + self.texto.get() + "&apikey=dbb11bd6")
            #s é pedido um titulo para pegar o filme. É um parametro. & significa passar um parametro novo
            # t - titulo
            # y - ano
            dict = json.loads(requisicao.text)

            self.lista.delete(0, END)
            self.lista.insert(END, ("Título: " + dict["Title"]))
            self.lista.insert(END, ("Ano: " + dict["Year"]))
            self.lista.insert(END, ("Lançamento: " + dict["Released"]))
            self.lista.insert(END, ("Duração: " + dict["Runtime"]))
            self.lista.insert(END, ("Gênero: " + dict["Genre"]))
            self.lista.insert(END, ("Diretor: " + dict["Director"]))
            self.lista.insert(END, ("Tipo: " + dict["Type"]))
            img = PIL.Image.open(dict["Poster"])
            #PIL.Image.open()
            print()
            
            print(dict["Poster"])
            self.lista.insert(END, ("Plot: " + dict["Plot"]))

        except:
            self.lista.delete(0, END)
            self.lista.insert(END, "Filme não encontrado")
            
#

#http://www.omdbapi.com/?

App()