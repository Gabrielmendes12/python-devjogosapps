import tkinter as tk

#criar uma janela principal
janela = tk.Tk()

#titulo da janela
janela.title("Minha Janela")

#definindo o tamanho da janela
janela.geometry("600x300") #dimensões de largura por altura

#cor da janela
janela.configure(bg = "SkyBlue")

#criando um texto dentro da janela
texto = tk.Label(janela, text="Meu Texto", font=("Arial, 20"),bg="SkyBlue", fg="DarkBlue") #bg = fundo, fg = cor do texto
texto.pack(pady = 50) #espaço vertical ao redor da janela

#criar um botão
botao = tk.Button(janela, text="Clique em Mim")
botao.pack()

janela.mainloop()