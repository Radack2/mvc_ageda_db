class View:
    """
    *******************************
    *     A view for a store DB   *
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
        print('8. Regresar')

    def show_a_cita(self, record):
        print('ID: ', record[0])
        print('Lugar: ', record[1])
        print('Ciudad: ', record[2])
        print('Estado: ', record[3])
        print('Fecha: ', record[4])
        print('Asunto: ', record[4])

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
        print('2. Leer Contactos')
        print('3. Leer todos los Contactos')
        print('4. Actualizar Contactos')
        print('5. Borrar Contactos')
        print('7. Regresar')

    def show_a_contacto(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido Paterno: ', record[2])
        print('Apellido Materno: ', record[3])
        print('Calle: ', record[4])
        print('No Exterior: ', record[5])
        print('No INterior: ', record[6])
        print('Colonia: ', record[7])
        print('Ciudad: ', record[11])
        print('Estado: ', record[12])
        print('Email: ', record[9])
        print('Telefono: ', record[10])
        
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
    def show_a_order_details(self, record):
        print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<20}|{record[3]:<11}|{record[4]:<9}|{record[5]:<11}')
        
    def show_detalles_cita_header(self):
        print('-'*81)
        print('ID'.ljust(5)+'|'+'Producto'.ljust(20)+'|'+'Marca'.ljust(20)+'|'+'Precio'.ljust(11)+'|'+'Cantidad'.ljust(9)+'|'+'Total'.ljust(11))
        print('-'*81)

    def show_detalles_cita_footer(self):
        print('-'*81)


    