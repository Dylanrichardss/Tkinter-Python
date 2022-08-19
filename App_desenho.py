from tkinter import  *
from PIL import Image
from tkinter.colorchooser import askcolor


class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("App de desenho")
        self.janela.minsize(width=1000, height=720)
        self.janela.maxsize(width=1000, height=720)
        self.janela.resizable(0,0)

        self.framee = Frame(self.janela, background="#3b3b3b", height=60)
        self.framee.pack(fill="x")

        self.cores = ("black", "grey", "white", "red", "green", "blue", "purple", "brown", "orange", "cyan", "yellow")
        

        self.texto_cor = Label(self.framee, text="  Cores:   ", foreground="white", background="#3b3b3b").pack(side="left")
        
        self.pegar_cor = "black"

        for i in self.cores:
            self.botao_cor = Button(self.framee, background=i, width=3, height=2, command=lambda cor=i: self.mudar_cor(cor)).pack(side="left")
            #command=lambda cor=i: self.mudar_cor(cor)
            # passa o parametro cor i, em lambda, e dps vai rodar com o parametro na chamada

        self.imagem_linha = PhotoImage(file="icones/linha.png")
        self.imagem_oval = PhotoImage(file="icones/oval.png")
        self.imagem_borracha = PhotoImage(file="icones/borracha.png")
        #self.imagem_salvar = PhotoImage(file="icones/salvar.png")
        self.imagem_novo = PhotoImage(file="icones/novo.png")
        self.imagem_cor = PhotoImage(file="icones/cor.png")

        self.cor_especifica_texto = Label(self.framee, text="   Escolher cor:  ", foreground="white", background="#3b3b3b")
        self.cor_especifica_texto.pack(side="left")
        self.cor_especifica = Button(self.framee, image=self.imagem_cor, bd=0, command=self.selecionar_cor).pack(side="left")
        


        self.texto_tamnho_pincel = Label(self.framee, text="    Tamanho:   ", foreground="white", background="#3b3b3b").pack(side="left")
        self.tamanho_pincel = Spinbox(self.framee, from_=1, to=50 )
        #tem que desenpacotar (colocar pack separado) 
        #Entao é uma váriavel e depois empacota
        self.tamanho_pincel.pack(side="left")


        self.pincel_linha = False
        self.pincel_oval = True
        self.pincel_borracha = False

        self.texto_pincel = Label(self.framee, text="    Pincel:   ", foreground="white", background="#3b3b3b").pack(side="left")

        self.botao_linha = Button(self.framee, image=self.imagem_linha, bd=0, command=self.pincel_linha_opcao).pack(side="left")
        self.botao_oval = Button(self.framee, image=self.imagem_oval, bd=0, command=self.pincel_oval_opcao).pack(side="left")
        self.botao_borracha = Button(self.framee, image=self.imagem_borracha, bd=0, command=self.pincel_borracha_opcao).pack(side="left")


        #self.texto_opcoes = Label(self.framee, text="    Opções:   ", foreground="white", background="#3b3b3b").pack(side="left")
        #self.botao_salvar = Button(self.framee, image=self.imagem_salvar, bd=0,command= self.salvar).pack(side="left")
        self.botao_novo = Button(self.framee, image=self.imagem_novo, bd=0, command=self.limpar).pack(side="left")

        self.area_desenho = Canvas(self.janela, background="white", height=700)
        self.area_desenho.pack(fill="both")
        self.area_desenho.bind('<B1-Motion>', self.desenhar)

        #Eventos, chama o bind. Passar aspas e dentro de tag.
        #Nome do evento. Tkinter tem lista de eventos. 
        #B1 é botao 1 do mouse
        #Motion é movimento

        self.janela.bind('<F1>', self.limpar)


        self.janela.mainloop()
        
    def desenhar(self, event):
        x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y
    
        #outline é contorno da linha. fill é preencher
        #create oval 
        #get é para pegar numero dentro da caixa spinbox


        if self.pincel_oval:
            self.area_desenho.create_oval(x1, y1, x2, y2, fill=self.pegar_cor, outline=self.pegar_cor, width=self.tamanho_pincel.get())
        elif self.pincel_linha:
            self.area_desenho.create_line(x1 - 5, y1 - 1, x2, y2, fill=self.pegar_cor, width=self.tamanho_pincel.get())
        else: 
            self.area_desenho.create_oval(x1, y1, x2, y2, fill="white", outline="white", width=self.tamanho_pincel.get())

    def mudar_cor(self, cor):
        self.pegar_cor = cor

    def pincel_linha_opcao(self):
        self.pincel_linha = True
        self.pincel_oval = False
        self.pincel_borracha = False

    def pincel_oval_opcao(self):
        self.pincel_linha = False
        self.pincel_oval = True
        self.pincel_borracha = False

    def pincel_borracha_opcao(self):
        self.pincel_linha = False
        self.pincel_oval = False
        self.pincel_borracha = True

    def limpar(self, event):
        self.area_desenho.delete("all")

    def selecionar_cor(self):
        corr = askcolor()
        self.pegar_cor = corr[1]

    '''def salvar2(self):
        #x = self.janela.winfo_rootx()
        #pega posição da janela, nao do canvas
        x = self.janela.winfo_rootx() + self.area_desenho.winfo_x()
        y = self.janela.winfo_rooty() + self.area_desenho.winfo_y()
        x1 = self.janela.winfo_rootx() + self.area_desenho.winfo_width()
        y1 = self.janela.winfo_rooty() + self.area_desenho.winfo_height()

        img = pyscreenshot.imcodec.grab(bbox=(x,y,x1,y1))
        img.save("imagem.png", "png")

    def salvar(self):
        self.area_desenho.postscript(file="opa.eps")
        img = Image.open("opa.eps")
        img.save("opa.eps")'''
        
App()
