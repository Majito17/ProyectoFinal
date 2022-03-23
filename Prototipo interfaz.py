from cgitb import text
import tkinter
from turtle import Screen
import random

screen=tkinter.Tk()
screen.geometry("900x800")
screen.title("BINGO")
screen.config(background="#0ec29b")

tag=tkinter.Label(screen, 
                    text="B", 
                    font=('Arial Baltic', 47, 'bold'), 
                    fg='white', 
                    bg='#10b31e',
                    relief=tkinter.GROOVE, 
                    bd=10,
                    padx=20)
tag.place(x=40, y=20)
tag2=tkinter.Label(screen, 
                    text="I", 
                    font=('Arial Baltic', 47, 'bold'), 
                    fg='white', 
                    bg='#b520f5', 
                    relief=tkinter.GROOVE, 
                    bd=10,
                    padx=35
                    )
tag2.place(x=165, y=20)
tag3=tkinter.Label(screen, 
                    text="N", 
                    font=('Arial Baltic', 47, 'bold'), 
                    fg='white', 
                    bg='#e62b1e',
                    relief=tkinter.GROOVE, 
                    bd=10,
                    padx=20)
tag3.place(x=295, y=20)
tag4=tkinter.Label(screen, 
                    text="G", 
                    font=('Arial Baltic', 47, 'bold'), 
                    fg='white', 
                    bg='#f5f50a',
                    relief=tkinter.GROOVE, 
                    bd=10,
                    padx=20)
tag4.place(x=420, y=20)
tag5=tkinter.Label(screen, 
                    text="O", 
                    font=('Arial Baltic', 47, 'bold'), 
                    fg='white', 
                    bg='#f28416',
                    relief=tkinter.GROOVE, 
                    bd=10,
                    padx=20)
tag5.place(x=550, y=20)
#Numeros
def textChange(widget):
    widget.config(text="X")
#ColumnaB
columna1a=tkinter.Button(screen,
                    text="2",
                    command = lambda: textChange(columna1a),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=15)
columna1a.place(x=40, y=130)
columna1b=tkinter.Button(screen, 
                    text="6",
                    command = lambda: textChange(columna1b),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=15,
                    )
columna1b.place(x=40, y=240)
columna1c=tkinter.Button(screen, 
                    text="10", 
                    command = lambda: textChange(columna1c),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=2,
                    )
columna1c.place(x=40, y=350)
columna1d=tkinter.Button(screen, 
                    text="16", 
                    command = lambda: textChange(columna1d),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=2)
columna1d.place(x=40, y=460)
columna1e=tkinter.Button(screen, 
                    text="13", 
                    command = lambda: textChange(columna1e),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=2,
                    )
columna1e.place(x=40, y=570)
#ColumnaI
columna2a=tkinter.Button(screen, 
                    text="24", 
                    command = lambda: textChange(columna2a),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna2a.place(x=169, y=130)
columna2b=tkinter.Button(screen, 
                    text="21", 
                    command = lambda: textChange(columna2b),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna2b.place(x=169, y=240)
columna2c=tkinter.Button(screen, 
                    text="16", 
                    command = lambda: textChange(columna2c),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna2c.place(x=169, y=350)
columna2d=tkinter.Button(screen, 
                    text="28", 
                    command = lambda: textChange(columna2d),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna2d.place(x=169, y=460)
columna2e=tkinter.Button(screen, 
                    text="19", 
                    command = lambda: textChange(columna2e),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna2e.place(x=169, y=570)
#ColumnaN
columna3a=tkinter.Button(screen, 
                    text="38", 
                    command = lambda: textChange(columna3a),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4)
columna3a.place(x=295, y=130)
columna3b=tkinter.Button(screen, 
                    text="40", 
                    command = lambda: textChange(columna3b),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna3b.place(x=295, y=240)
columna3c=tkinter.Button(screen, 
                    text="31", 
                    command = lambda: textChange(columna3c),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna3c.place(x=295, y=350)
columna3d=tkinter.Button(screen, 
                    text="33", 
                    command = lambda: textChange(columna3d),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna3d.place(x=295, y=460)
columna3e=tkinter.Button(screen, 
                    text="42", 
                    command = lambda: textChange(columna3e),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna3e.place(x=295, y=570)
#ColumnaG
columna4a=tkinter.Button(screen, 
                    text="47", 
                    command = lambda: textChange(columna4a),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4)
columna4a.place(x=425, y=130)
columna4b=tkinter.Button(screen, 
                    text="55", 
                    command = lambda: textChange(columna4b),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna4b.place(x=425, y=240)
columna4c=tkinter.Button(screen, 
                    text="59", 
                    command = lambda: textChange(columna4c),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna4c.place(x=425, y=350)
columna4d=tkinter.Button(screen, 
                    text="48", 
                    command = lambda: textChange(columna4d),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna4d.place(x=425, y=460)
columna4e=tkinter.Button(screen, 
                    text="60", 
                    command = lambda: textChange(columna4e),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna4e.place(x=425, y=570)
#ColumnaO
columna5a=tkinter.Button(screen, 
                    text="63", 
                    command = lambda: textChange(columna5a),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4)
columna5a.place(x=555, y=130)
columna5b=tkinter.Button(screen, 
                    text="67", 
                    command = lambda: textChange(columna5b),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna5b.place(x=555, y=240)
columna5c=tkinter.Button(screen, 
                    text="72", 
                    command = lambda: textChange(columna5c),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna5c.place(x=555, y=350)
columna5d=tkinter.Button(screen, 
                    text="61", 
                    command = lambda: textChange(columna5d),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna5d.place(x=555, y=460)
columna5e=tkinter.Button(screen, 
                    text="70", 
                    command = lambda: textChange(columna5e),
                    font=('Arial Baltic', 35, 'bold'), 
                    fg='white', 
                    bg='#0ec29b',
                    relief=tkinter.SOLID, 
                    bd=2,
                    padx=4,
                    )
columna5e.place(x=555, y=570)
#BotónCarton
carton_nuevo=tkinter.Button(screen,
                            text="Nuevo cartón",
                            font=('Arial Baltic', 15, 'bold'),
                            fg='white', 
                            bg='#0b9c9c',
                            relief=tkinter.RAISED, 
                            bd=2,
                            padx=20)
carton_nuevo.place(x=690, y=625)
#Aleatorionumeros
numero=random.randint(1,75)
numero_aleatorio=tkinter.Label(screen,
                                text=numero,
                                font=('Arial Baltic', 40, 'bold'),
                                fg='black', 
                                bg='white',
                                relief=tkinter.SUNKEN, 
                                bd=2,
                                padx=20)
numero_aleatorio.place(x=730, y=50)
#BotonSortearnumeros
def change(widget):
    widget.config(text=random.randint(1,75))
sortearnum = tkinter.Button(screen,
                            text="Sortear", 
                            command = lambda: change(numero_aleatorio),
                            font=('Arial Baltic', 15, 'bold'),
                            fg='white', 
                            bg='#0b9c9c',
                            relief=tkinter.RAISED, 
                            bd=2,
                            padx=20)
sortearnum.place(x=720, y=150)
screen.mainloop()

