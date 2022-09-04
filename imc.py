
from cgitb import text
from enum import Flag
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image,ImageTk

#cores
c01 ="#f5eeee"#branco
c02 ="#f2f055"#amarelo
c03 ="#84c7e2"#azul claro
c04 = "#03c78a"#verde
c05 ="#ff0000"#vermelho
c06="#da6523"#laranja
c07 ="#040404"#preto

#criando janela

janela = Tk()
janela.title('')
janela.geometry('250x400')
janela.resizable(width=False,height=False)
janela.configure(bg=c01)
style=ttk.Style(janela)
style.theme_use('clam')

def calcular():
    altura =float(e_valoral.get())
    peso =float(e_valorpe.get())
    imc = peso / (altura * altura)
    if imc > 0 and imc < 18.5:
        l_Resultado ['text']=(f'{imc:,.2f}')
        l_classificacao['text']=("Déficit de massa corporal")
        l_riscos['text']=("Baixo(com risco doenças)")

    elif imc >= 18.5 and imc <25:
        l_Resultado ['text']=(f'{imc:,.2f}')
        l_classificacao['text']=("Massa corporal Normal")
        l_riscos['text']=("Normal")

    elif imc >= 25 and imc <30:
        l_Resultado ['text']=(f'{imc:,.2f}')
        l_classificacao['text']=("Sobrepeso")
        l_riscos['text']=("Elevado")

    elif imc >= 30 and imc <35:
        l_Resultado ['text']=(f'{imc:,.2f}')
        l_classificacao['text']=("Obesidade média")
        l_riscos['text']=("Alto")

    elif imc >= 35 and imc <40:
        l_Resultado['text']=(f'{imc:,.2f}')
        l_classificacao['text']=("Obesidade média")
        l_riscos['text']=("muito Alto")
    
    else:
        l_Resultado ['text']=(f'{imc:,.2f}')
        l_classificacao['text']= ("Obesidade mórbida")
        l_riscos['text']=("iminente")

#Criando frames
framecima = Frame(janela,width=300,height=50,bg=c01,relief='flat')
framecima.grid(row=0,column=0)

framemeio = Frame(janela,width=300,height=110,bg=c01,relief='flat')
framemeio.grid(row=1,column=0)

framebaixo = Frame(janela,width=300,height=290,bg=c01,relief='flat')
framebaixo.grid(row=2,column=0)

#logo
app_ = Label(framecima,text='Calculadora IMC',compound=LEFT,padx=5,anchor=NW,font=('verdana 17'), relief=FLAT,bg=c01,fg=c07)
app_.place(x=0,y=0)
#abrindo imagem
img = Image.open("fita.png")
img =img.resize((35,35))
img = ImageTk.PhotoImage(img)

app_logo=Label(framecima,image=img,compound=LEFT,padx=5,anchor=NW,font=("verdana 20"), relief=FLAT,bg=c01,fg=c07,)
app_logo.place(x=195,y=0)

app_linha = Label(framecima,width=295,anchor=NW,font=('verdana 1'), relief=FLAT,bg=c05,fg=c01)
app_linha.place(x=0,y=47)
# frame do meio

app_= Label(framemeio ,text='Altura?',anchor=NW,font=('ivy 10'), relief=FLAT,bg=c01,fg=c07)
app_.place(x=7,y=10)

e_valoral =Entry(framemeio,width=10,  font=('ivy 10'), relief='solid',justify='center')
e_valoral.place(x=10,y=30)

app_= Label(framemeio ,text='Seu peso?',anchor=NW,font=('ivy 10'), relief=FLAT,bg=c01,fg=c07)
app_.place(x=7,y=60)

e_valorpe =Entry(framemeio,width=10,  font=('ivy 10'), relief='solid',justify='center')
e_valorpe.place(x=10,y=80)

#calcular
btn_calcular=Button(framemeio,text='Calcular'.upper(),command=calcular,font=("ivy 9"),anchor=NW,overrelief=RIDGE,bg=c03,fg=c07)
btn_calcular.place(x=170,y=85)

# frame baixo
# Resultado
l_Resultado =Label(framebaixo,text='Resultado'.upper(),width=30,anchor=NW,font=('verdana 10 bold'),relief=FLAT,bg=c01,fg=c07)
l_Resultado.place(x=0,y=20)
l_Resultado = Label(framebaixo,width=25,anchor=NW,font=('verdana 12'),relief=FLAT,bg=c03,fg=c07)
l_Resultado.place(x=0,y=55)
#Classificação
l_classificacao =Label(framebaixo,text='Classificação'.upper(),width=30,anchor=NW,font=('verdana 10 bold'),relief=FLAT,bg=c01,fg=c07)
l_classificacao.place(x=0,y=95)
l_classificacao = Label(framebaixo,width=25,anchor=NW,font=('verdana 12'),relief=FLAT,bg=c03,fg=c07)
l_classificacao.place(x=0,y=125)

# Riscos
l_riscos =Label(framebaixo,text='Riscos'.upper(),width=30,anchor=NW,font=('verdana 10 bold'),relief=FLAT,bg=c01,fg=c07)
l_riscos.place(x=0,y=165)
l_riscos = Label(framebaixo,width=25,anchor=NW,font=('verdana 12'),relief=FLAT,bg=c03,fg=c07)
l_riscos.place(x=0,y=195)

     
janela.mainloop()