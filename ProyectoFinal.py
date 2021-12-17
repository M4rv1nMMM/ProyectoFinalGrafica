#PROYECTOFINALCGV
#By ING. Eduardo JOC amd ING. Marvin MMM
import tkinter
from tkinter import *
import pymysql

#<editor-fold desc="UsuariosPage">
def UsuariosPage():
    #<editor-fold desc="BASE DE DATOS">
    class DataBase:
        def __init__(self):
            self.connection=pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='parkingpabito'
            )
            self.cursor = self.connection.cursor()
        #<editor-fold desc="UsuariosCRUD">
        def USUARIOS_get_all_records(self):
            sql='select * from usuario'
            try:
                contador = 0
                record = StringVar()
                self.cursor.execute(sql)
                Alums=self.cursor.fetchall()
                for alum in Alums:
                    contador+=1
                    id=alum[0]
                    name=alum[1]
                    apellido=alum[2]
                    email=alum[3]
                    telefono=alum[4]
                    if(alum[6]==1):
                        tipousuario="Ocacional"
                    else:
                        tipousuario="Recurrente"
                    record = (str(id)+"    ||    "+str(name)+" "+str(apellido)+"    ||    "+str(email)+"    ||    "+str(telefono)+"    ||    "+str(tipousuario))
                    lx.insert(contador, record)
            except Exception as e:
                raise
        def insertdata(self, Id, Name, Email):
            sql="INSERT INTO mydb(Code, Name, Email) VALUES ('{}','{}','{}') ".format(Id, Name, Email)
            print(sql)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
                print("DATOS INGRESADOS CORRECTAMENTE")
            except Exception as e:
                raise
        #</editor-fold>
    obj_db1 = DataBase()
    #</editor-fold>
    def VolverMenu():
        MenuMainPage.deiconify()
        UsuariosPage.destroy()
    def MostrarData():
        lx.delete(0,END)
        obj_db1.USUARIOS_get_all_records()
    MenuMainPage.withdraw()
    UsuariosPage = tkinter.Tk()
    UsuariosPage.geometry("800x600+0+0")
    UsuariosPage.title("Parking Pabito")
    lblTitulo = tkinter.Label(UsuariosPage, text="USUARIOS")
    lblcrear = tkinter.Label(UsuariosPage, text="Crear Usuarios")
    lblId = tkinter.Label(UsuariosPage, text="ID:")
    lblId = tkinter.Label(UsuariosPage, text="ID:")
    lblId = tkinter.Label(UsuariosPage, text="ID:")
    lblId = tkinter.Label(UsuariosPage, text="ID:")
    btnVolver= tkinter.Button(UsuariosPage, text="<-- Volver", command= VolverMenu)#Listbox
    lx = Listbox(UsuariosPage, width=100)
    btnVolver.pack()
    lblTitulo.pack()
    lx.pack()
    lblcrear.pack()
    MostrarData()
    UsuariosPage.mainloop()
#</editor-fold>

#<editor-fold desc="VehiculosPage">
def VehiculosPage():
    #<editor-fold desc="BASE DE DATOS">
    class DataBase:
        def __init__(self):
            self.connection=pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='parkingpabito'
            )
            self.cursor = self.connection.cursor()
        #<editor-fold desc="UsuariosCRUD">
        def VEHICULOS_get_all_records(self):
            sql='select * from vehiculo'
            try:
                contador = 0
                record = StringVar()
                self.cursor.execute(sql)
                Alums=self.cursor.fetchall()
                for alum in Alums:
                    contador+=1
                    id=alum[0]
                    marca=alum[1]
                    modelo=alum[2]
                    color=alum[3]
                    placa=alum[4]
                    record = (str(id)+"    ||    "+str(marca)+"    ||    "+str(modelo)+"    ||    "+str(color)+"    ||    "+str(placa))
                    lx.insert(contador, record)
            except Exception as e:
                raise
        def insertdata(self, Id, Name, Email):
            sql="INSERT INTO mydb(Code, Name, Email) VALUES ('{}','{}','{}') ".format(Id, Name, Email)
            print(sql)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
                print("DATOS INGRESADOS CORRECTAMENTE")
            except Exception as e:
                raise
        #</editor-fold>
    obj_db1 = DataBase()
    #</editor-fold>
    def VolverMenu():
        MenuMainPage.deiconify()
        UsuariosPage.destroy()
    def MostrarData():
        lx.delete(0,END)
        obj_db1.VEHICULOS_get_all_records()
    MenuMainPage.withdraw()
    UsuariosPage = tkinter.Tk()
    UsuariosPage.geometry("600x600+0+0")
    UsuariosPage.title("Parking Pabito")
    lblTitulo = tkinter.Label(UsuariosPage, text="VEHICULOS")
    lblcrear = tkinter.Label(UsuariosPage, text="Crear Vehiculo")
    lblId = tkinter.Label(UsuariosPage, text="ID:")
    lblId = tkinter.Label(UsuariosPage, text="ID:")
    lblId = tkinter.Label(UsuariosPage, text="ID:")
    lblId = tkinter.Label(UsuariosPage, text="ID:")
    btnVolver= tkinter.Button(UsuariosPage, text="<-- Volver", command= VolverMenu)#Listbox
    lx = Listbox(UsuariosPage, width=80)
    btnVolver.pack()
    lblTitulo.pack()
    lx.pack()
    lblcrear.pack()
    MostrarData()
    UsuariosPage.mainloop()
#</editor-fold>

#<editor-fold desc="MenuMainPage">
MenuMainPage = tkinter.Tk()
MenuMainPage.geometry("300x200+0+0")
MenuMainPage.title("Parking Pabito")
lblTitulo = tkinter.Label(MenuMainPage, text="Menu Principal")
btnCamaraVivo = tkinter.Button(MenuMainPage, text="Camara en Vivo", command= UsuariosPage)
btnCancelacion = tkinter.Button(MenuMainPage, text="Cancelaciones", command= UsuariosPage)
btnUsuarios = tkinter.Button(MenuMainPage, text="Usuarios", command= UsuariosPage)
btnVehiculos = tkinter.Button(MenuMainPage, text="Vehiculos", command= VehiculosPage)
btnReportes = tkinter.Button(MenuMainPage, text="Reportes", command= UsuariosPage)
lblTitulo.pack()
btnCamaraVivo.pack()
btnCancelacion.pack()
btnUsuarios.pack()
btnVehiculos.pack()
btnReportes.pack()
MenuMainPage.mainloop()
#</editor-fold>