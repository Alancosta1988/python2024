from tkinter import *
from tkinter import ttk

#----cores-----

co0 = '#ffffff' #branca / white
co1 = '#444466'#preta /black
co2 = '#4065a1'#azul / blue

janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co0)

#--------dividindo A JANELA em duas etapas ------------

Frame_cima= Frame(janela, width=295, height=50, bg=co0, pady= 0,padx= 0, relief='flat')
Frame_cima.grid(row=0, column=0, sticky=NSEW)

Frame_baixo= Frame(janela, width= 295, height= 180, bg= co0, pady= 0,padx= 0, relief='flat')
Frame_baixo.grid(row=1, column=0, sticky=NSEW)

#------configurando frame cima-------

app_nome = Label(Frame_cima, text='calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('ivy 16 bold'), bg=co0,fg=co1)
app_nome.place(x=0, y=0)

app_linha = Label(Frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('ivy 1'), bg=co2,fg=co1)
app_linha.place(x=0, y=35)

#-------------- funcao calcular ---

def calcular():
    
    peso = float(e_peso.get())
    altura = float(e_altura.get())
    
    imc = peso /altura**2
    
    resultado = imc
    
    if resultado < 18.5:
        l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"
        
    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = "Seu IMC é: Normal"
        
    elif resultado >= 25 and resultado < 30:
        l_resultado_texto['text'] = "Seu IMC é: Sobrepeso"
        
    else:
        l_resultado_texto['text'] = 'Seu IMC é: Obesidade'
    
    
    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

#-------configurando frame baixo--------

l_peso = Label(Frame_baixo, text='insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('ivy 10'), bg=co0,fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(Frame_baixo, width=5, relief='solid', font=('Ivy 10'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(Frame_baixo, text='insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('ivy 10'), bg=co0,fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(Frame_baixo, width=5, relief='solid', font=('Ivy 10'),justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(Frame_baixo, text='---', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg=co2,fg=co0)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(Frame_baixo, text='', width=37, height=1, pady=12, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0,fg=co1)
l_resultado_texto.place(x=0, y=90)

b_calcular = Button(Frame_baixo, command= calcular, text='calcular', width=34, height=1,overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10'), bg=co2,fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)
      

janela.mainloop()
