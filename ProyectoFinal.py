#PROYECTOFINALCGV
#By ING. Eduardo JOC amd ING. Marvin MMM
import tkinter
from tkinter import *
import pymysql

#<editor-fold desc="CamaraVivoPage">
def CamaraVivoPage():
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
            sql='SELECT u.id_usuario, u.nombre, u.apellido, u.email, u.telefono, v.placa, u.id_tipousuario FROM usuario u inner join vehiculo v on u.id_vehiculo=v.id_vehiculo'
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
                    placa=alum[5]
                    if(alum[6]==1):
                        tipousuario="Ocacional"
                    else:
                        tipousuario="Recurrente"
                    record = (str(id)+"    ||    "+str(name)+" "+str(apellido)+"    ||    "+str(email)+"    ||    "+str(telefono)+"    ||    "+str(placa)+"    ||    "+str(tipousuario))
                    lx.insert(contador, record)
            except Exception as e:
                raise
        def insertdata(self, Nombre, Apellido, Email, Telefono, Idvehi, Idtipou):
            sql="INSERT INTO usuario(nombre, apellido, email, telefono, id_vehiculo, id_tipousuario) VALUES ('{}','{}','{}','{}','{}','{}') ".format(Nombre, Apellido, Email, Telefono, Idvehi, Idtipou)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise
        def get_one_record(self,Id):
            sql='select * from usuario where id_usuario={}'.format(Id)
            try:
                self.cursor.execute(sql)
                Alum = self.cursor.fetchone()
                txtNombre.insert(0,Alum[1])
                txtApellido.insert(0,Alum[2])
                txtEmail.insert(0,Alum[3])
                txtTelefono.insert(0,Alum[4])
                txtIdVehi.insert(0,Alum[5])
                txtIdTipoU.insert(0,Alum[6])
            except Exception as e:
                raise
        def updatedata(self, Id, Nombre, Apellido, Email, Telefono, Idvehi, Idtipou):
            sql="UPDATE usuario SET nombre='{}',apellido='{}',email='{}',telefono='{}',id_vehiculo='{}',id_tipousuario='{}' WHERE id_usuario='{}'".format(Nombre, Apellido, Email, Telefono, Idvehi, Idtipou, Id)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise
        def deleteonlyone(self, Id):
            sql="DELETE FROM usuario WHERE id_usuario='{}'".format(Id)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
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
    def GuardarData():
        nombre = txtNombre.get()
        apellido = txtApellido.get()
        email = txtEmail.get()
        telefono = txtTelefono.get()
        idvehi = txtIdVehi.get()
        idtipou = txtIdTipoU.get()
        obj_db1.insertdata(nombre, apellido, email, telefono, idvehi, idtipou)
        lx.delete(0,END)
        obj_db1.USUARIOS_get_all_records()
        Limpiar()
    def Buscar():
        id = txtId.get()
        obj_db1.get_one_record(id)
    def ActualizarData():
        id = txtId.get()
        nombre = txtNombre.get()
        apellido = txtApellido.get()
        email = txtEmail.get()
        telefono = txtTelefono.get()
        idvehi = txtIdVehi.get()
        idtipou = txtIdTipoU.get()
        obj_db1.updatedata(id, nombre, apellido, email, telefono, idvehi, idtipou)
        lx.delete(0,END)
        obj_db1.USUARIOS_get_all_records()
        Limpiar()
    def EliminarData():
        id = txtId.get()
        obj_db1.deleteonlyone(id)
        lx.delete(0,END)
        obj_db1.USUARIOS_get_all_records()
        Limpiar()
    def Limpiar():
        txtId.delete(0, 'end')
        txtNombre.delete(0, 'end')
        txtApellido.delete(0, 'end')
        txtEmail.delete(0, 'end')
        txtTelefono.delete(0, 'end')
        txtIdVehi.delete(0, 'end')
        txtIdTipoU.delete(0, 'end')
    MenuMainPage.withdraw()
    UsuariosPage = tkinter.Tk()
    UsuariosPage.geometry("800x700+0+0")
    UsuariosPage.title("Parking Pabito")
    lblTitulo = tkinter.Label(UsuariosPage, text="USUARIOS")
    lblcrear = tkinter.Label(UsuariosPage, text="Crear Usuarios")
    lblNombre = tkinter.Label(UsuariosPage, text="NOMBRE:")
    lblApellido = tkinter.Label(UsuariosPage, text="APELLIDO:")
    lblEmail = tkinter.Label(UsuariosPage, text="EMAIL:")
    lblTelefono = tkinter.Label(UsuariosPage, text="TELEFONO:")
    lblIdVehi = tkinter.Label(UsuariosPage, text="ID DEL VEHICULO:")
    lblIdTipoU = tkinter.Label(UsuariosPage, text="ID DEL TIPO DE USUARIO:")
    lblIdSearch = tkinter.Label(UsuariosPage, text="Traer por Id")
    lblOpciones = tkinter.Label(UsuariosPage, text="Opciones:")
    txtNombre = Entry(UsuariosPage)
    txtApellido = Entry(UsuariosPage)
    txtEmail = Entry(UsuariosPage)
    txtTelefono = Entry(UsuariosPage)
    txtIdVehi = Entry(UsuariosPage)
    txtIdTipoU = Entry(UsuariosPage)
    txtId = Entry(UsuariosPage)
    btnVolver= tkinter.Button(UsuariosPage, text="<-- Volver", command= VolverMenu)
    btnCrear= tkinter.Button(UsuariosPage, text="Crear", command= GuardarData)
    btnBuscar= tkinter.Button(UsuariosPage, text="Buscar", command= Buscar)
    btnModificar= tkinter.Button(UsuariosPage, text="Modificar", command= ActualizarData)
    btnEliminar= tkinter.Button(UsuariosPage, text="Eliminar", command= EliminarData)
    lx = Listbox(UsuariosPage, width=100)
    btnVolver.pack()
    lblTitulo.pack()
    lx.pack()
    lblcrear.pack()
    lblNombre.pack()
    txtNombre.pack()
    lblApellido.pack()
    txtApellido.pack()
    lblEmail.pack()
    txtEmail.pack()
    lblTelefono.pack()
    txtTelefono.pack()
    lblIdVehi.pack()
    txtIdVehi.pack()
    lblIdTipoU.pack()
    txtIdTipoU.pack()
    btnCrear.pack()
    lblIdSearch.pack()
    txtId.pack()
    btnBuscar.pack()
    lblOpciones.pack()
    btnModificar.pack()
    btnEliminar.pack()
    MostrarData()
    UsuariosPage.mainloop()
#</editor-fold>

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
            sql='SELECT u.id_usuario, u.nombre, u.apellido, u.email, u.telefono, v.placa, u.id_tipousuario FROM usuario u inner join vehiculo v on u.id_vehiculo=v.id_vehiculo'
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
                    placa=alum[5]
                    if(alum[6]==1):
                        tipousuario="Ocacional"
                    else:
                        tipousuario="Recurrente"
                    record = (str(id)+"    ||    "+str(name)+" "+str(apellido)+"    ||    "+str(email)+"    ||    "+str(telefono)+"    ||    "+str(placa)+"    ||    "+str(tipousuario))
                    lx.insert(contador, record)
            except Exception as e:
                raise
        def insertdata(self, Nombre, Apellido, Email, Telefono, Idvehi, Idtipou):
            sql="INSERT INTO usuario(nombre, apellido, email, telefono, id_vehiculo, id_tipousuario) VALUES ('{}','{}','{}','{}','{}','{}') ".format(Nombre, Apellido, Email, Telefono, Idvehi, Idtipou)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise
        def get_one_record(self,Id):
            sql='select * from usuario where id_usuario={}'.format(Id)
            try:
                self.cursor.execute(sql)
                Alum = self.cursor.fetchone()
                txtNombre.insert(0,Alum[1])
                txtApellido.insert(0,Alum[2])
                txtEmail.insert(0,Alum[3])
                txtTelefono.insert(0,Alum[4])
                txtIdVehi.insert(0,Alum[5])
                txtIdTipoU.insert(0,Alum[6])
            except Exception as e:
                raise
        def updatedata(self, Id, Nombre, Apellido, Email, Telefono, Idvehi, Idtipou):
            sql="UPDATE usuario SET nombre='{}',apellido='{}',email='{}',telefono='{}',id_vehiculo='{}',id_tipousuario='{}' WHERE id_usuario='{}'".format(Nombre, Apellido, Email, Telefono, Idvehi, Idtipou, Id)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise
        def deleteonlyone(self, Id):
            sql="DELETE FROM usuario WHERE id_usuario='{}'".format(Id)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
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
    def GuardarData():
        nombre = txtNombre.get()
        apellido = txtApellido.get()
        email = txtEmail.get()
        telefono = txtTelefono.get()
        idvehi = txtIdVehi.get()
        idtipou = txtIdTipoU.get()
        obj_db1.insertdata(nombre, apellido, email, telefono, idvehi, idtipou)
        lx.delete(0,END)
        obj_db1.USUARIOS_get_all_records()
        Limpiar()
    def Buscar():
        id = txtId.get()
        obj_db1.get_one_record(id)
    def ActualizarData():
        id = txtId.get()
        nombre = txtNombre.get()
        apellido = txtApellido.get()
        email = txtEmail.get()
        telefono = txtTelefono.get()
        idvehi = txtIdVehi.get()
        idtipou = txtIdTipoU.get()
        obj_db1.updatedata(id, nombre, apellido, email, telefono, idvehi, idtipou)
        lx.delete(0,END)
        obj_db1.USUARIOS_get_all_records()
        Limpiar()
    def EliminarData():
        id = txtId.get()
        obj_db1.deleteonlyone(id)
        lx.delete(0,END)
        obj_db1.USUARIOS_get_all_records()
        Limpiar()
    def Limpiar():
        txtId.delete(0, 'end')
        txtNombre.delete(0, 'end')
        txtApellido.delete(0, 'end')
        txtEmail.delete(0, 'end')
        txtTelefono.delete(0, 'end')
        txtIdVehi.delete(0, 'end')
        txtIdTipoU.delete(0, 'end')
    MenuMainPage.withdraw()
    UsuariosPage = tkinter.Tk()
    UsuariosPage.geometry("800x700+0+0")
    UsuariosPage.title("Parking Pabito")
    lblTitulo = tkinter.Label(UsuariosPage, text="USUARIOS")
    lblcrear = tkinter.Label(UsuariosPage, text="Crear Usuarios")
    lblNombre = tkinter.Label(UsuariosPage, text="NOMBRE:")
    lblApellido = tkinter.Label(UsuariosPage, text="APELLIDO:")
    lblEmail = tkinter.Label(UsuariosPage, text="EMAIL:")
    lblTelefono = tkinter.Label(UsuariosPage, text="TELEFONO:")
    lblIdVehi = tkinter.Label(UsuariosPage, text="ID DEL VEHICULO:")
    lblIdTipoU = tkinter.Label(UsuariosPage, text="ID DEL TIPO DE USUARIO:")
    lblIdSearch = tkinter.Label(UsuariosPage, text="Traer por Id")
    lblOpciones = tkinter.Label(UsuariosPage, text="Opciones:")
    txtNombre = Entry(UsuariosPage)
    txtApellido = Entry(UsuariosPage)
    txtEmail = Entry(UsuariosPage)
    txtTelefono = Entry(UsuariosPage)
    txtIdVehi = Entry(UsuariosPage)
    txtIdTipoU = Entry(UsuariosPage)
    txtId = Entry(UsuariosPage)
    btnVolver= tkinter.Button(UsuariosPage, text="<-- Volver", command= VolverMenu)
    btnCrear= tkinter.Button(UsuariosPage, text="Crear", command= GuardarData)
    btnBuscar= tkinter.Button(UsuariosPage, text="Buscar", command= Buscar)
    btnModificar= tkinter.Button(UsuariosPage, text="Modificar", command= ActualizarData)
    btnEliminar= tkinter.Button(UsuariosPage, text="Eliminar", command= EliminarData)
    lx = Listbox(UsuariosPage, width=100)
    btnVolver.pack()
    lblTitulo.pack()
    lx.pack()
    lblcrear.pack()
    lblNombre.pack()
    txtNombre.pack()
    lblApellido.pack()
    txtApellido.pack()
    lblEmail.pack()
    txtEmail.pack()
    lblTelefono.pack()
    txtTelefono.pack()
    lblIdVehi.pack()
    txtIdVehi.pack()
    lblIdTipoU.pack()
    txtIdTipoU.pack()
    btnCrear.pack()
    lblIdSearch.pack()
    txtId.pack()
    btnBuscar.pack()
    lblOpciones.pack()
    btnModificar.pack()
    btnEliminar.pack()
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
        #<editor-fold desc="VehiculoCRUD">
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
        def insertdata(self, Marca, Modelo, Color, Placa):
            sql="INSERT INTO vehiculo(marca, modelo, color, placa) VALUES ('{}','{}','{}','{}') ".format(Marca, Modelo, Color, Placa)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise
        def get_one_record(self,Id):
            sql='select * from vehiculo where id_vehiculo={}'.format(Id)
            try:
                self.cursor.execute(sql)
                Alum = self.cursor.fetchone()
                txtMarca.insert(0,Alum[1])
                txtModelo.insert(0,Alum[2])
                txtColor.insert(0,Alum[3])
                txtPlaca.insert(0,Alum[4])
            except Exception as e:
                raise
        def updatedata(self, Id, Marca, Modelo, Color, Placa):
            sql="UPDATE vehiculo SET marca='{}',modelo='{}',color='{}',placa='{}' WHERE id_vehiculo='{}'".format(Marca, Modelo, Color, Placa, Id)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise
        def deleteonlyone(self, Id):
            sql="DELETE FROM vehiculo WHERE id_vehiculo='{}'".format(Id)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
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
    def GuardarData():
        marca = txtMarca.get()
        modelo = txtModelo.get()
        color = txtColor.get()
        placa = txtPlaca.get()
        obj_db1.insertdata(marca, modelo, color, placa)
        lx.delete(0,END)
        obj_db1.VEHICULOS_get_all_records()
        Limpiar()
    def Buscar():
        id = txtId.get()
        obj_db1.get_one_record(id)
    def ActualizarData():
        id = txtId.get()
        marca = txtMarca.get()
        modelo = txtModelo.get()
        color = txtColor.get()
        placa = txtPlaca.get()
        obj_db1.updatedata(id, marca, modelo, color, placa)
        lx.delete(0,END)
        obj_db1.VEHICULOS_get_all_records()
        Limpiar()
    def EliminarData():
        id = txtId.get()
        obj_db1.deleteonlyone(id)
        lx.delete(0,END)
        obj_db1.VEHICULOS_get_all_records()
        Limpiar()
    def Limpiar():
        txtId.delete(0, 'end')
        txtMarca.delete(0, 'end')
        txtModelo.delete(0, 'end')
        txtColor.delete(0, 'end')
        txtPlaca.delete(0, 'end')
    MenuMainPage.withdraw()
    UsuariosPage = tkinter.Tk()
    UsuariosPage.geometry("600x600+0+0")
    UsuariosPage.title("Parking Pabito")
    lblTitulo = tkinter.Label(UsuariosPage, text="VEHICULOS")
    lblcrear = tkinter.Label(UsuariosPage, text="Crear Vehiculo")
    lblMarca = tkinter.Label(UsuariosPage, text="MARCA:")
    lblModelo = tkinter.Label(UsuariosPage, text="MODELO:")
    lblColor = tkinter.Label(UsuariosPage, text="COLOR:")
    lblPlaca = tkinter.Label(UsuariosPage, text="PLACA:")
    lblIdSearch = tkinter.Label(UsuariosPage, text="Traer por Id")
    lblOpciones = tkinter.Label(UsuariosPage, text="Opciones:")
    txtMarca = Entry(UsuariosPage)
    txtModelo = Entry(UsuariosPage)
    txtColor = Entry(UsuariosPage)
    txtPlaca = Entry(UsuariosPage)
    txtId = Entry(UsuariosPage)
    btnVolver= tkinter.Button(UsuariosPage, text="<-- Volver", command= VolverMenu)
    btnCrear= tkinter.Button(UsuariosPage, text="Crear", command= GuardarData)
    btnBuscar= tkinter.Button(UsuariosPage, text="Buscar", command= Buscar)
    btnModificar= tkinter.Button(UsuariosPage, text="Modificar", command= ActualizarData)
    btnEliminar= tkinter.Button(UsuariosPage, text="Eliminar", command= EliminarData)
    lx = Listbox(UsuariosPage, width=80)
    btnVolver.pack()
    lblTitulo.pack()
    lx.pack()
    lblcrear.pack()
    lblMarca.pack()
    txtMarca.pack()
    lblModelo.pack()
    txtModelo.pack()
    lblColor.pack()
    txtColor.pack()
    lblPlaca.pack()
    txtPlaca.pack()
    btnCrear.pack()
    lblIdSearch.pack()
    txtId.pack()
    btnBuscar.pack()
    lblOpciones.pack()
    btnModificar.pack()
    btnEliminar.pack()
    MostrarData()
    UsuariosPage.mainloop()
#</editor-fold>

#<editor-fold desc="MenuMainPage">
MenuMainPage = tkinter.Tk()
MenuMainPage.geometry("300x200+0+0")
MenuMainPage.title("Parking Pabito")
lblTitulo = tkinter.Label(MenuMainPage, text="Menu Principal")
btnCamaraVivo = tkinter.Button(MenuMainPage, text="Camara en Vivo", command= CamaraVivoPage)
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