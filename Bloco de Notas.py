import tkinter
from tkinter import *


def novo_arquivo():
    texto_1.delete(1.0,"end")


def salvar_arquivo():
    documento = texto_1.get(1.0,"end")
    #armazena tudo. Do inicio ao fim
    arquivo = open("notepad.txt", "w")
    #variavel recebe o método open e (variavel pode ter método print por exemplo) 
    #falamos que ele cria o documento chamado notepad e escreva tudo que esta em documento nele e feche o arquivo  
    arquivo.write(documento)
    arquivo.close()
    # w é de write. Escrever. R é de read. Ler o documento.

def abrir_arquivo():
    texto_1.delete(1.0,"end")
    arquivo = open("notepad.txt", "r")
    documento = arquivo.read()
    texto_1.insert(1.0, documento)


def atualizar_fonte():
    fonte = spin_font.get()
    tamanho = spin_size.get()
    texto_1.config(font="{} {}".format(fonte, tamanho))


janela = tkinter.Tk()

janela.title("Notepad")
janela.minsize(width=1280, height=720)
janela.maxsize(width=1280, height=720)
janela.resizable(0,0)


barra = tkinter.Frame(janela, height=30)
barra.pack(fill="x")
#fill é sempre adaptar (quando aumentar e diminuir) o frame, não importa a resolução, no eixo x 


fonte_texto = tkinter.Label(barra, text=" Fonte: ")
#label é texto. rotular o texto
#Colocar dentro do frame (barra)
fonte_texto.pack(side="left")
spin_font = tkinter.Spinbox(barra, values=("Arial", "Verdana"))
#spin é caixa com 2 barrinhas com setas para cima e para baixo
spin_font.pack(side="left")

font_size = tkinter.Label(barra, text=" Tamanho da Fonte: ")
font_size.pack(side="left")
#sempre coloca na esquerda após o ultimo da esquerda
spin_size = Spinbox(barra, from_=1, to=60)
spin_size.pack(side="left")


botao = Button(barra, text="Aplicar",command=atualizar_fonte)
botao.pack(side="left")


texto_1 = tkinter.Text(janela, font="Arial 22 bold", width=1280, height=720) #Da a opção da pessoa escrever
texto_1.pack() #pack é mostrar o texto (Topo e centralizado)

main_menu = tkinter.Menu(janela) 
#1 É o próprio menu com as opções e (aonde queremos colocar o menu). Var que recebe parte da bibilioteca tkinter chamada menu

#4 Menu dentro de outro menu. Vai ser o menu (dentro no main_menu (cascade))
arquivo_menu= tkinter.Menu(main_menu, tearoff=0)
arquivo_menu.add_command(label="Novo", command=novo_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
arquivo_menu.add_command(label="Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="Sair", command=janela.quit)

#cascade é um leque de opções. O add comand é quando clica, executa uma função


main_menu.add_cascade(label='Arquivo', menu=arquivo_menu) 
#3 adiciona opções na variavel menu. Label é o texto. 
janela.config(menu=main_menu) 
#2 Janela configura o menu dela, como o menu. 


janela.mainloop()