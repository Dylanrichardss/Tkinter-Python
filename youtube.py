from tkinter import *
#from pytube  import YouTube
import youtube_dl
import os  
from tkinter import filedialog

class App:

    def __init__(self):

        self.janela = Tk()
        self.janela.title("Youtube")
        self.janela.resizable(0, 0)
        self.janela.geometry("1000x520")

        self.imagem_logo = PhotoImage(file="icones\youtube.png")
        
        self.audio = False
        self.video = False
        
        self.framee = Frame(self.janela, bg='#3b3b3b', pady=30)
        self.framee.pack(fill='x')

        self.label_logo = Label(self.framee, image=self.imagem_logo, bg='#3b3b3b')
        self.label_logo.pack()

        self.framee2 = Frame(self.janela, pady=10)
        self.framee2.pack()

        self.label_insert = Label(self.framee2, text=' Inserir link: ', font='arial 12 bold')
        self.label_insert.pack(side='left')

        self.link = Entry(self.framee2,font='arial 20', width=50)
        self.link.pack(side='left')

        self.play = Button(self.framee2, bg='red', text=' > ', bd=0, fg='white',
                           width=4, heigh=2, command=lambda: self.download(self.link.get())).pack()
        self.ab = lambda: self.download(self.link.get())
        print(self.ab)

        self.framee3 = Frame(self.janela)
        self.framee3.pack()
        
        self.radio1 = Radiobutton(self.framee3, text="Aúdio", value=0, command=self.Audio).pack(side="left")
        self.radio2 = Radiobutton(self.framee3, text="Video", value=1, command=self.Video).pack(side="left")
        self.radio3 = Radiobutton(self.framee3, text="Audio e Video", value=2, command=self.All).pack(side="left")

      
        self.janela.mainloop()

    def Audio(self):
        self.audio = True
        self.video = False
      
    def Video(self):
        self.audio = False
        self.video = True
    

    def All(self):
        self.audio = False
        self.video = False
        
    def download(self, link):
        try:
            os.system("youtube-dl " + str(link)) # Faz download do video.
            self.mensagem_sucesso()
        except:
            self.mensagem_erro()

    def mensagem_erro(self):
        janela = Toplevel()
        #top level é janela que sobrepoe a principal
        janela.title("Erro")
        janela.resizable(0, 0)
        janela.geometry("150x60")

        texto = Label(janela, text="Link não válido",pady=5)
        texto.pack()

        botao_saida = Button(janela, text="Sair", background="red", bd=0 ,foreground="white", command=janela.destroy)
        botao_saida.pack()

        
    def mensagem_sucesso(self):
        janela = Toplevel()
        #top level é janela que sobrepoe a principal
        janela.title("Sucesso")
        janela.resizable(0, 0)
        janela.geometry("150x60")

        texto = Label(janela, text="Download Concluido",pady=5)
        texto.pack()

        botao_saida = Button(janela, text="Ok", background="green", bd=0 ,foreground="white", command=janela.destroy)
        botao_saida.pack()
          
App()        

