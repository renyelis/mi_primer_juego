from tkinter import *
import random

#...................
# variables globales
#...................
x = 460
y = 220
radio = 10
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2

centro_x = random.randint(radio, x)
centro_y = random.randint(radio, y)

def mover_carrojo():
    global desplazamiento_x, desplazamiento_y

    x0, y0, x1, y1 = c.coords(carrojo)
    if x0 < 0 or x1 > x: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > y: 
        desplazamiento_y = -desplazamiento_y
    c.move(carrojo, desplazamiento_x, desplazamiento_y)
    iniciar = ventana_principal.after(intervalo, carrojo)

    if x0 > 300:
        ventana_principal.after_cancel(iniciar)
    if x0>300:
        desplazamiento_x = 0    



# ventana principal

ventana_principal = Tk()
ventana_principal.title("Juego")
ventana_principal.geometry("500x500")
ventana_principal.config(bg="turquoise1")


# frame de graficacion

frame_graficacion= Frame(ventana_principal)
frame_graficacion.config(bg="white",width=480, height=240)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion,width=x, height=y)
c.config(bg="gray26")
c.place(x=10,y=10)

rect_1 =c.create_rectangle(x-45,y+5,x-95,y-250,fill="black", outline="black")
rect_2 =c.create_rectangle(x-360,y+2,x-410,y-250,fill="black", outline="black")
rect_3 =c.create_rectangle(x-120,y-100,x-340,y-115,fill="white", outline="black")

img_carrojo = PhotoImage(file="img/carrojo.png")
carrojo = c.create_image(x/2-170,y-180,image=img_carrojo)

img_carranja = PhotoImage(file="img/carranja.png")
carranja = c.create_image(x/2-170,y-60,image=img_carranja)

texto_1 =c.create_text(x/2-155, y-160, anchor="center",text="S",font=("Mandingo",10, "bold"),fill="white")
texto_2 =c.create_text(x/2-155, y-140, anchor="center",text="T",font=("Mandingo",10, "bold"),fill="white")
texto_3 =c.create_text(x/2-155, y-120, anchor="center",text="A",font=("Mandingo",10, "bold"),fill="white")
texto_4 =c.create_text(x/2-155, y-100, anchor="center",text="R",font=("Mandingo",10, "bold"),fill="white")
texto_5 =c.create_text(x/2-155, y-80, anchor="center",text="T",font=("Mandingo",10, "bold"),fill="white")


texto_1 =c.create_text(x-70, y-160, anchor="center",text="F",font=("Mandingo",10, "bold"),fill="white")
texto_2 =c.create_text(x-70, y-140, anchor="center",text="I",font=("Mandingo",10, "bold"),fill="white")
texto_3 =c.create_text(x-70, y-120, anchor="center",text="N",font=("Mandingo",10, "bold"),fill="white")
texto_4 =c.create_text(x-70, y-100, anchor="center",text="I",font=("Mandingo",10, "bold"),fill="white")
texto_5 =c.create_text(x-70, y-80, anchor="center",text="S",font=("Mandingo",10, "bold"),fill="white")
texto_6 =c.create_text(x-70, y-60, anchor="center",text="H",font=("Mandingo",10, "bold"),fill="white")




# frame de conroles

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="turquoise1", width=480, height=230)
frame_controles.place(x=10, y=260)


bt=Button(frame_controles)
bt.config(width=20, height=5, text="¡Empezar!", command=mover_carrojo)
bt.place(x=150,y=10)




ventana_principal.mainloop()