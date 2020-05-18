class View:
    """
    *******************************
    *     A view for a agenda DB  *
    *******************************
    """

    def start(self):
        print('===========================')
        print('= ¡Bienvenido a tu Agenda =')
        print('===========================')

    def end(self):
        print('=================================')
        print('=        ¡Hasta la vista!       =')
        print('=================================')
        

    def main_menu(self):
        print('************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('1. Citas')
        print('2. Contactos')
        print('3. Salir')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de Nuevo')
    
    def ask(self, output):
        print(output, end='')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id)) + len(op) +24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id)) + len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err) +4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    
    """
    *******************************
    *        View for Citas       *
    *******************************
    """
    def cita_menu(self):
        print('***************************')
        print('* --   Submenu Citas   -- *')
        print('***************************')
        print('1. Agregar Cita')
        print('2. Leer Cita')
        print('3. Leer todas las Citas')
        print('4. Leer Citas por asunto')
        print('5. Leer Citas por fecha')
        print('6. Actualizar Cita')
        print('7. Borrar Cita')
        print('8. Agregar contacto a cita')
        print('9. Leer contacto de una cita')
        print('10. Leer citas de un contacto')
        print('11. Actualizar detalles cita')
        print('12. Eliminar contacto cita')
        print('13. Regresar')

    def show_a_cita(self, record):
        print('ID: ', record[0])
        print('Lugar: ', record[1])
        print('Ciudad: ', record[2])
        print('Estado: ', record[3])
        print('Fecha: ', record[4])
        print('Asunto: ', record[5])

    def show_cita_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_cita_midder(self):
        print('-'*48)

    def show_cita_footer(self):
        print('*'*48)

    
    """
    *******************************
    *      View for Contactos     *
    *******************************
    """
    def contacto_menu(self):
        print('***************************')
        print('* -- Submenu Contactos -- *')
        print('***************************')
        print('1. Agregar Contactos')
        print('2. Leer Contacto')
        print('3. Leer todos los Contactos')
        print('4. Actualizar Contactos')
        print('5. Borrar Contactos')
        print('6. Regresar')

    def show_a_contacto(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido Paterno: ', record[2])
        print('Apellido Materno: ', record[3])
        print('Calle: ', record[4])
        print('No Exterior: ', record[5])
        print('No INterior: ', record[6])
        print('Colonia: ', record[7])
        print('Ciudad: ', record[8])
        print('Estado: ', record[9])
        print('Email: ', record[10])
        print('Telefono: ', record[11])
        
    def show_a_contacto_brief(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1]+' '+record[2]+' '+record[3])
        print('Direccion: ', record[4]+' '+record[5]+' '+record[6]+' '+record[7])
        print(record[11]+' '+record[12]+' '+record[8])
        print('Email: ', record[9])
        print('Telefono: ', record[10])

    def show_contacto_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_contacto_midder(self):
        print('-'*53)

    def show_contacto_footer(self):
        print('*'*53)

    

    """
    *******************************
    *   View for Detalles-Cita    *
    *******************************
    """
    def show_a_contacto_cita(self, record):
        print('ID Contacto: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido Paterno: ', record[2])
        print('Apellido Materno: ', record[3])
        print('Cita: ', record[4])
        print('Nota: ', record[5])
        print('ID Cita: ', record[6])
        print('Lugar: ', record[7])
        print('Fecha: ', record[8])
        
    def show_contacto_cita_header(self, header):
        print(header.center(53, '*'))
        print('-'*48)

    def show_contacto_cita_midder(self):
        print('-'*53)

    def show_contacto_cita_footer(self):
        print('*'*53)

    def show_a_detalles_cita(self, record):
        print('Nombre Cita: ', record[2])
        print('Descripcion ', record[3])
        