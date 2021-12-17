
import tkinter

def saludar2():
    def saludar():
        primer_ventana.deiconify()
        segunda_ventana.destroy()
    # Segunda ventana con valores negativos
    primer_ventana.withdraw()
    segunda_ventana = tkinter.Tk()
    segunda_ventana.geometry("300x300-0-0")
    segunda_ventana.title("Posicion x=-0 y=-0")
    etiqueta = tkinter.Label(segunda_ventana, text="Posicion x=-0 y=-0")
    bt2= tkinter.Button(segunda_ventana, text="volveremos", command= saludar)
    etiqueta.pack()
    bt2.pack()
    segunda_ventana.mainloop()


# Primera ventana con valores positivos
primer_ventana = tkinter.Tk()
primer_ventana.geometry("300x300+0+0")
# A modo estetico le di un titulo
primer_ventana.title("Posicion x=+0 y=+0")
# Este tambien es estetico y no influye en el uso del metodo
etiqueta = tkinter.Label(primer_ventana, text="Posicion x=+0 y=+0")
bt2= tkinter.Button(primer_ventana, text="Ir a Test a:", command= saludar2)

etiqueta.pack()
bt2.pack()




primer_ventana.mainloop()
