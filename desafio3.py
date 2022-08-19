from turtle import width
from pytube import YouTube
from tkinter import *

'''url = input("Digite a URL do vídeo:")

video = YouTube(url)

video.streams.get_lowest_resolution().download(
    output_path = "C:\artu",
    filename = video.title
)'''

janela = Tk()
janela.geometry('500x300')
janela.title('KKKKK que daora')
janela.configure(background = "pink")

texto1 = Label(
    janela,
    text = "Oi, meu amigo, você foi convocado para o banho dos campeões!!",
    font = (
        "Helvetica", 10, "bold"
    )
)

texto1.place(
    x = 0,
    y = 0,
    width = 500,
    height = 300
)

butao = Button(
    janela,
    text="clique aqui",
)



janela.mainloop()
