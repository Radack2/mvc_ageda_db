from Model.Model import Model
from View.View import View
from datetime import date


class Controller:
    """
    *********************************
    *  A controller for a store DB  *
    *********************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()


    """
    *********************************
    *       General Controller      *
    *********************************
    """
    def main_menu(self):
        o = '0'
        while 0 != '3':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.cita_menu()
            elif o == '2':
                self.contacto_menu()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals


    """
    *********************************
    *     Controllers for dates     *
    *********************************
    """
    def cita_menu(self):
        o = '0'
        while o != '8':
            self.view.cita_menu()
            self.view.option('13')
            o = input()
            if o == '1':
                self.create_cita()
            elif o == '2':
                self.read_a_cita()
            elif o == '3':
                self.read_all_citas()
            elif o == '4':
                self.read_citas_asunto()
            elif o == '5':
                self.read_cita_fecha()
            elif o == '6':
                self.update_cita()
            elif o == '7':
                self.delete_cita()
            elif o == '8':
                self.create_detalles_cita()
            elif o == '9':
                self.read_contactos_cita()
            elif o == '10':
                self.read_citas_contacto()
            elif o == '11':
                self.update_detalles_cita()
            elif o == '12':
                self.delete_detalles_cita()
            elif o == '13':
                self.main_menu()
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_cita(self):
        self.view.ask('Lugar: ')
        lugar = input()
        self.view.ask('Ciudad: ')
        ciudad = input()
        self.view.ask('Estado: ')
        estado = input()
        self.view.ask('Fecha: ')
        fecha = input()
        self.view.ask('Asunto: ')
        asunto = input()
        return [ lugar, ciudad, estado, fecha, asunto ]

    def create_cita(self):
        lugar, ciudad, estado, fecha, asunto = self.ask_cita()
        out = self.model.create_cita(lugar, ciudad, estado, fecha, asunto)
        # id_cita = self.read_a_cita(asunto)
        if out == True:
            self.view.ok(lugar+' '+fecha+' '+asunto, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA CITA. REVISA')
        return

    def read_a_cita(self):
        self.view.ask('ID cita: ')
        id_cita = input()
        cita = self.model.read_a_cita(id_cita)
        if type(cita) == tuple:
            self.view.show_cita_header(' Datos de la cita '+id_cita+' ')
            self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            if cita == None:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA CITA. REVISA')
        return

    def read_all_citas(self):
        citas = self.model.read_all_citas()
        if type(citas) == list:
            self.view.show_cita_header(' Todas las citas ') 
            for cita in citas:
                self.view.show_a_cita(cita)
                self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA')
        return

    def read_citas_asunto(self):
        self.view.ask('Asunto: ')
        asunto = input()
        citas = self.model.read_citas_asunto(asunto)
        if type(citas) == list:
            self.view.show_cita_header(' Asunto de la cita '+asunto+' ')
            for cita in citas:
                self.view.show_a_cita(cita)
                self.view.show_cita_midder()
            self.view.show_cita_footer
        else:
            self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA')
        return

    def read_cita_fecha(self):
        self.view.ask('Fecha: ')
        fecha = input()
        citas = self.model.read_cita_fecha(fecha)
        if type(citas) == list:
            self.view.show_cita_header(' Fecha: '+fecha+' ')
            for cita in citas:
                self.view.show_a_cita(cita)
                self.view.show_cita_midder() 
            self.view.show_cita_footer() 
        else:
            self.view.error('PROBLEMA AL LEER La CITA. REVISA')
        return

    def update_cita(self):
        self.view.ask('ID de cita a modificar: ')
        id_cita = input()
        cita = self.model.read_a_cita(id_cita)    
        if type(cita) == tuple:
            self.view.show_cita_header(' Datos del producto '+id_cita+' ')
            self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            if cita == None:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_cita()
        fields, vals = self.update_lists(['c_lugar', 'c_ciudad', 'c_estado', 'c_fecha', 'c_asunto'], whole_vals)
        vals.append(id_cita)
        vals = tuple(vals)
        out = self.model.update_cita(fields,vals)
        if out == True:
            self.view.ok(id_cita, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA CITA. REVISA')
        return      
        
    def delete_cita(self):
        self.view.ask('Id de la cita a borrar: ')
        id_cita = input()
        count = self.model.delete_cita(id_cita)
        if count != 0:
            self.view.ok(id_cita, 'borro')
        else:
            if count == 0:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA CITA. REVISA.')
        return


    """
    ***********************************
    *   Controllers for Contactos     *
    ***********************************
    """
    def contacto_menu(self):
        o = '0'
        while o != '6':
            self.view.contacto_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_contacto()
            elif o == '2':
                self.read_a_contacto()
            elif o == '3':
                self.read_all_contactos()
            elif o == '4':
                self.update_contacto()
            elif o == '5':
                self.delete_contacto()
            elif o == '6':
                self.main_menu()
                return
            else:
                self.view.not_valid_option()
        return

    def ask_contacto(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        apellidoP = input()
        self.view.ask('Apellido materno: ')
        apellidoM = input()
        self.view.ask('Calle: ')
        calle = input()
        self.view.ask('No. exterior: ')
        noext = input()
        self.view.ask('No interior: ')
        noint = input()
        self.view.ask('Colonia: ')
        col = input()
        self.view.ask('Ciudad: ')
        ciudad = input()
        self.view.ask('Estado: ')
        estado = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Telefono: ')
        phone = input()
        return [ name, apellidoP, apellidoM, calle, noext, noint, col, ciudad, estado, email, phone ]

    def create_contacto(self):
        name, apellidoP, apellidoM, calle, noext, noint, col, ciudad, estado, email, phone = self.ask_contacto()
        out = self.model.create_contacto(name, apellidoP, apellidoM, calle, noext, noint, col, ciudad, estado, email, phone)
        if out == True:
            self.view.ok(name+' '+apellidoP+' '+apellidoM, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL CONTACTO. REVISA')
        return
    
    def read_a_contacto(self):
        self.view.ask('ID Contacto: ')
        id_contacto = input()
        contacto = self.model.read_a_contacto(id_contacto)
        if type(contacto) == tuple:
            self.view.show_contacto_header(' Datos del contacto '+id_contacto+' ')
            self.view.show_a_contacto(id_contacto)
            self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            if contacto == None:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CONTACTO. REVISA')
        return
    
    def read_all_contactos(self):
        contactos = self.model.read_all_contactos()
        if type(contactos) == list:
            self.view.show_contacto_header(' Todos los contacto ')
            for contacto in contactos:
                self.view.show_a_contacto(contacto)
                self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CONTACTOS. REVISA')
        return

    def update_contacto(self):
        self.view.ask('ID de contacto a modificar: ')
        id_contacto = input()
        contactos = self.model.read_a_contacto(id_contacto)
        if type(contactos) == tuple:
            self.view.show_contacto_header(' Datos del contacto '+id_contacto+' ')
            self.view.show_a_contacto(contactos)
            self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            if contactos == None:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CONTACTO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_contacto()
        fields, vals = self.update_lists(['c_nombre', 'c_apellidoP', 'c_apellidoM', 'c_calle', 'c_noext', 'c_noint', 'c_col', 'c_ciudad','c_estado', 'c_email', 'c_telefono'], whole_vals)
        vals.append(id_contacto)
        vals = tuple(vals)
        out = self.model.update_contacto(fields, vals)
        if out == True:
            self.view.ok(id_contacto, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL CONTACTO. REVISA')
        return

    def delete_contacto(self):
        self.view.ask('ID de contacto a borrar: ')
        id_contacto = input()
        count = self.model.delete_contacto(id_contacto)
        if count != 0:
            self.view.ok(id_contacto, 'borro')
        else:
            if count == 0:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CONTACTO. REVISA')
        return
    

    """
    **************************************
    *   Controllers for Detalles-Cita    *
    **************************************
    """
    def create_detalles_cita(self):
        self.read_all_citas()
        self.view.ask('ID cita: ')
        id_cita = input()
        if id_cita != '':
            cita = self.model.read_a_cita(id_cita)
            if type(cita) == tuple:
                self.view.show_cita_header(' Datos de la cita '+id_cita+' ')
                self.view.show_a_cita(cita)
                self.view.show_cita_footer()
                self.view.ask('Cita: ')
                nombre = input()
                self.view.ask('Notas: ')
                descripcion = input()
                self.read_all_contactos()
                self.view.ask('ID contacto: ')
                id_contacto = input()
                if id_contacto != '':
                    contacto = self.model.read_a_contacto(id_contacto)
                    self.view.show_contacto_header(' Datos del contacto '+id_contacto+' ')
                    self.view.show_a_contacto(contacto)
                    self.view.show_contacto_midder()
                    self.view.show_contacto_footer()
                    if type(contacto) == tuple:
                        out = self.model.create_detalles_cita(id_cita, id_contacto, nombre, descripcion)
                        if out == True:
                            self.view.ok(contacto[1],'Agrego')
                        else:
                            if out.errno == 1062:
                                self.view.error('LA CITA YA NO ESTA PROGRAMADA')
                            else:
                                self.view.error('NO SE PUDO AGREGAR LA CITA. REVISA')
                    else:
                        if contacto == None:
                            self.view.error('EL CONTACTO NO EXISTE')
                        else:
                            self.view.error('NO SE PUDO AGREGAR EL CONTACTO. REVISA')
                else:
                    if cita == None:
                        self.view.error('LA CITA NO EXISTE')
                    else:
                        self.view.error('NO SE PUDO AGREGAR LA CITA. REVISA')
            else:
                if cita == None:
                    self.view.error('LA CITA NO EXISTE')
                else:
                    self.view.error('PROBLEMA AL LEER LA CITA. REVISA')
        return

    def read_contactos_cita(self):
        self.view.ask('ID Cita: ')
        id_cita = input()
        contacto_cita = self.model.read_contactos_cita(id_cita)
        if type(contacto_cita) == list:
            self.view.show_contacto_cita_header('Usuarios dentro de Cita')
            for contacto in contacto_cita:
                self.view.show_a_contacto(contacto)
                self.view.show_contacto_midder()
            self.view.show_contacto_footer() 
        else:
            if contacto_cita == None:
                self.view.error('LA CITA NO TIENE CONTACTOS')
            else:
                self.view.error('PROBLEMA AL LEER EL CONTACTO CON CITA. REVISA')
        return

    def read_citas_contacto(self):
        self.view.ask('ID Contacto: ')
        id_contacto = input()
        contactos_citas = self.model.read_citas_contacto(id_contacto)
        if type(contactos_citas) == list:
            self.view.show_contacto_cita_header(' Todas la Citas para el contacto ')
            for cita in contactos_citas:
                self.view.show_a_cita(cita)
                self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CONTACTOS Y CITAS. REVISA')
        return

    
    def ask_detalles_cita(self):
        self.view.ask('Nombre de Cita: ')
        nombre = input()
        self.view.ask('Nota: ')
        descripcion = input()
        return [nombre, descripcion ]


    def update_detalles_cita(self):
        self.view.ask('ID de la cita a modificar: ')
        id_cita = input()
        cita = self.model.read_detalles_cita(id_cita)
        if type(cita) == tuple:
            self.view.show_cita_header('Detalles_Cita')
            self.view.show_a_detalles_cita(cita)
            self.view.show_contacto_cita_midder()
            self.view.show_contacto_cita_footer()
        else:
            if cita == None:
                self.view.error('La cita no existe')
            else:
                self.view.error('PROBLEMA AL LEER LA CITA. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_detalles_cita()
        fields, vals = self.update_lists(['nombre', 'descripcion'],whole_vals)
        vals.append(id_cita)
        vals = tuple(vals)
        print('vals',vals)
        print('fiels',fields)
        out = self.model.update_detalles_cita(fields,vals)
        print(out)
        if out == True:
            self.view.ok(id_cita, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL CONTACTO CON LA CITA. REVISA')
        return

       
    def delete_detalles_cita(self):
        self.read_all_detalles_citas()
        self.view.ask('ID de la cita a borrar del contacto: ')
        id_cita = input()
        count = self.model.delete_detalles_cita(id_cita)
        if count != 0:
            self.view.ok(id_cita, 'borro')
        else:
            if count == 0:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA CITA DEL CONTACTO. REVISA')
        return