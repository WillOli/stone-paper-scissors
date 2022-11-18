import random
import tkinter
from tkinter import *
from tkinter import ttk

# importando o pillow
from PIL import Image, ImageTk

import random

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"  # green / verde
co5 = "#e85151"  # red / vermelha
co6 = "#fcc058"  # orange
co7 = "#e85151"  # vermelha
co8 = "#34eb3d"  # + verde
fundo = "#3b3b3b"

# configurando a janela
janela = Tk()
janela.title('')
# lagura e comprimento
janela.geometry('260x280')
janela.configure(bg=fundo)

# dividindo a janela

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando frame cima
app_1 = Label(frame_cima, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)

app_ = Label(frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=-20)

app_2_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=-20)
app_2 = Label(frame_cima, text='PC', heigth=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=205, y=70)
app_2_linha = Label(frame_cima, text='', heigth=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = Label(frame_cima, text='', width=255, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_pc = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_pc.place(x=190, y=10)

global voce
global pc
global rondas
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rondas = 5


# função logica do jogo
def jogar(i):
    global rondas
    global pontos_voce
    global pontos_pc

    if rondas > 0:
        print(rondas)
        opcoes = ['Stone', 'Paper', 'Scissor']
        pc = random.choice(opcoes)
        voce = i

        app_pc['text'] = pc
        app_pc['fg'] = co1

        # caso for igual
        if voce == 'Stone' and pc == 'Stone':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif voce == 'Paper' and pc == 'Paper':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif voce == 'Scissor' and pc == 'Scissor':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3


        # movendo para frente
        elif voce == 'Stone' and pc == 'Paper':
            print('Pc ganhou!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0

            pontos_pc = 10



        elif voce == 'Paper' and pc == 'Scissor':
            print('Pc ganhou!')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0

            pontos_pc += 10

            # movendo para tras

        elif voce == 'Scissor' and pc == 'Paper':
            print('Você ganhou!')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0

            pontos_voce += 10

        elif voce == 'Scissor' and pc == 'Stone':
            print('Pc ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0

            pontos_pc +=10

        elif voce == 'Paper' and pc == 'Stone':
            print('Você ganhou!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg']= co0

            pontos_voce +=10

        # atualizando a pontuação
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc

        # chamando a função terminar

       # fim_do_jogo()

# função iniciar o jogo

def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('images/stone.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTK.PhotoImage(icon_1)
    b_icon_1 = Button(frame_cima, command=lambda: jogar('Stone'), width=50, image=icon_1, compound=CENTER, bg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=50)

    icon_2= Image.open('images/paper.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTK.PHOTOImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Paper'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y=50)

    icon_3 = Image.open('images/scissors.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTK.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Scissors'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.pĺace(x=170,y=50)






janela.mainloop()