from tkinter import *
import random

# root
root = Tk()
root.title("Piedra, papel o tijera")
root.config(bg="pink")

pc_valores = {
        '0': "piedra",
        '1': "papel",
        '2': "tijera"
    }
   
 # var contadores
c_empates = 0
c_humano = 0
c_maquina = 0

def ppt():
    # pc opciones
    

    # saludo inicial
    name = Label(root, text="PIEDRA, PAPEL O TIJERA")
    name.config(bg="lightblue", height=5, font='Helvetica 14 bold')
    name.pack(fill='x')
    saludo = Label(root, text='Bienvenidx al juego! \n\nElige!')
    saludo.config(bg='yellow', font='Helvetica 10 bold')
    saludo.pack(fill='x')
    # frame base
    frame = Frame(root)
    frame.pack()
    # frame1
    frame1 = Frame(root)
    frame1.config(bg='lightblue')
    frame1.pack(fill='x')
    # botones opcion
    boton1 = Button(frame1, text="PIEDRA", command=lambda: user_Piedra())
    boton2 = Button(frame1, text='PAPEL', command=lambda: user_Papel())
    boton3 = Button(frame1, text="TIJERA", command=lambda: user_Tijera())
    boton1.config(bg='orange')
    boton1.grid(row=2, column=0, ipadx=40)
    boton2.config(bg='orange')
    boton2.grid(row=2, column=2, ipadx=40)
    boton3.config(bg="orange")
    boton3.grid(row=2, column=3, ipadx=40)

    def desclickar():
        boton1["state"] = "disable"
        boton2["state"] = "disable"
        boton3["state"] = "disable"
        # reset funcion

    def resetear():
        boton1["state"] = "normal"
        boton2["state"] = "normal"
        boton3["state"] = "normal"
        l1.config(text="Humanx")
        l3.config(text="Máquina")
        l4.config(text="")
        

    def user_Piedra():
        pc = pc_valores[str(random.randint(0, 2))]
        while True:
            if pc == "piedra":
                resultado = "Empate"
            elif pc == "papel":
                resultado = "Te gané!"
            else:
                resultado = "Humanx: Ganaste!"
                l4.config(text=resultado)
                l1.config(text="Piedra")
                l3.config(text=pc)
                desclickar()
                break

    def user_Papel():
        pc = pc_valores[str(random.randint(0, 2))]
        while True:
            if pc == "papel":
                resultado = "Empate"
            elif pc == "piedra":
                resultado = "Humanx: Ganaste!"
            else:
                resultado = "Te gané"
            l4.config(text=resultado)
            l1.config(text="Papel")
            l3.config(text=pc)
            desclickar()
            break

    def user_Tijera():
        pc = pc_valores[str(random.randint(0, 2))]
        if pc == "tijera":
            resultado = "Empate"
        elif pc == "papel":
            resultado = "Humanx: Ganaste!"
        else:
            resultado = "Te gané"
        l4.config(text=resultado)
        l1.config(text="Tijera       ")
        l3.config(text=pc)
        desclickar()

    def contador():
        global c_empates, c_maquina, c_humano

        while True:
            if resultado == "Empate":
                c_empates += 1
                l5.config(text="Empates: " + str(c_empates))
                l6.pack(frame2)
            elif resultado == "Te gané":
                c_maquina += 1
                l6.config(text="Máquina: " + str(c_maquina))
                l6.pack(frame2)
            else:
                c_humano += 1
                l7.config(text="Humanx: " + str(c_humano))
                l7.pack(frame2)
            break



    # frame 2
    frame2 = Frame(root)
    frame2.config(bg='lightblue')
    frame2.pack(fill='x')

    # inicializar contadores
    c_empates = 0
    c_maquina = 0
    c_humano = 0
    resultado = 0
    # labels
    l1 = Label(frame, text="Humanx")
    l1.config(bg="fuchsia", font="normal 10")

    l2 = Label(frame, text="||")
    l2.config(bg='fuchsia', font="normal 10")

    l3 = Label(frame, text="Máquina")
    l3.config(bg="fuchsia", font="normal 10")

    l1.pack(fill='x', side=LEFT)
    l2.pack(fill="x", side=LEFT)
    l3.pack(fill="x")

    l4 = Label(root, text="")
    l4.config(bg='fuchsia', font="normal 20 bold",
            width=15, borderwidth=4, relief="solid")
    l4.pack(pady=20)

    l5 = Label(frame2, text="Empates: " + str(c_empates))
    l5.grid(row=0, column=0)

    l6 = Label(frame2, text="Máquina: " + str(c_maquina))
    l6.grid(row=1, column=0)

    l7 = Label(frame2, text="Humanx: " + str(c_humano))


    l7.grid(row=2, column=0)
        # reset boton
    reset=Button(root,  text="Reiniciar", 	command=lambda:  resetear())
    reset.pack()
    root.mainloop()


ppt()
