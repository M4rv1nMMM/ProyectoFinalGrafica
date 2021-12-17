#PROYECTOFINALCGV
#By ING. Eduardo JOC amd ING. Marvin MMM
import tkinter

def saludar2():
    def saludar():
        MenuMainPage.deiconify()
        segunda_ventana.destroy()
    # Segunda ventana con valores negativos
    MenuMainPage.withdraw()
    segunda_ventana = tkinter.Tk()
    segunda_ventana.geometry("300x300-0-0")
    segunda_ventana.title("Posicion x=-0 y=-0")
    etiqueta = tkinter.Label(segunda_ventana, text="Posicion x=-0 y=-0")
    bt2= tkinter.Button(segunda_ventana, text="volveremos", command= saludar)
    etiqueta.pack()
    bt2.pack()
    segunda_ventana.mainloop()


#           MenuMainPage
#   Definicion de Ventana MenuMainPage
MenuMainPage = tkinter.Tk()
MenuMainPage.geometry("300x200+0+0")
MenuMainPage.title("Parking Zott")
lblTitulo = tkinter.Label(MenuMainPage, text="Menu Principal")
btnCamaraVivo = tkinter.Button(MenuMainPage, text="Camara en VIVO!", command= saludar2)
btnCancelacion = tkinter.Button(MenuMainPage, text="Cancelaciones", command= saludar2)
btnUsuarios = tkinter.Button(MenuMainPage, text="Usuarios", command= saludar2)
btnVehiculos = tkinter.Button(MenuMainPage, text="Vehiculos", command= saludar2)
btnReportes = tkinter.Button(MenuMainPage, text="Reportes", command= saludar2)
lblTitulo.pack()
btnCamaraVivo.pack()
btnCancelacion.pack()
btnUsuarios.pack()
btnVehiculos.pack()
btnReportes.pack()
MenuMainPage.mainloop()
