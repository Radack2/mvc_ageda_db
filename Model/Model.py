from mysql  import connector

class Model:
    """"
    **************************************
    A data model with Mysql for a Diary DB 
    **************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()


    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    ******************************
    *       Date methods     *
    ******************************
    """

    def create_cita(self, lugar, ciudad, estado, fecha, asunto):
        try:
            sql = 'INSERT INTO cita (`c_lugar`, `c_ciudad`, `c_estado`, `c_fecha`, `c_asunto`) VALUES (%s, %s, %s, %s, %s)'
            vals = (lugar, ciudad, estado, fecha, asunto)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_cita(self, id_cita):
        try:
            sql =  'SELECT * FROM cita WHERE id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_citas(self):   #Caution with large amount of data
        try:
            sql =  'SELECT * FROM cita'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_citas_asunto(self, asunto):
        try:
            sql =  'SELECT * FROM cita WHERE c_asunto = %s'
            vals = (asunto,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_cita_fecha(self, fecha):
        try:
            sql =  'SELECT * FROM cita WHERE c_fecha = %s'
            vals = (fecha, )
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_cita(self, fields, vals):
        try:
            sql = 'UPDATE cita SET '+','.join(fields)+' WHERE id_cita = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_cita(self, id_cita):
        try:
            sql =  'DELETE FROM cita WHERE id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************************
    *       Contacto methods     *
    ******************************
    """
    def create_contacto(self, name, apellidoP, apellidoM, calle, noext, noint, col, ciudad, estado, email, phone):
        try:
            sql = 'INSERT INTO contacto (`c_nombre`, `c_apellidoP`, `c_apellidoM`, `c_calle`, `c_noext`, `c_noint`, `c_col`, `c_ciudad`,`c_estado`, `c_email`, `c_telefono`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = ( name, apellidoP, apellidoM, calle, noext, noint, col, ciudad, estado, email, phone )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_contacto(self, id_contacto):
        try:
            sql = 'SELECT  * FROM contacto WHERE id_contacto = %s'
            vals = (id_contacto,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_contactos(self):   #Caution with large amount of data
        try:
            sql =  'SELECT * FROM contacto'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_contacto(self, fields, vals):
        try:
            sql = 'UPDATE contacto SET '+','.join(fields)+' WHERE id_contacto = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_contacto(self, id_contacto):
        try:
            sql =  'DELETE FROM contacto WHERE id_contacto = %s'
            vals = (id_contacto,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************************
    *   Detalles-Cita methods    *
    ******************************
    """

    def create_detalles_cita(self, id_cita, id_contacto, nombre, descripcion):
        try:
            sql = 'INSERT INTO detalles_cita (`id_cita`,`id_contacto`,`nombre`,`descripcion`) VALUES (%s, %s, %s, %s)'
            vals = ( id_cita, id_contacto, nombre, descripcion )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_contactos_cita(self, id_cita):
        try:
            sql = 'SELECT contacto.* FROM contacto JOIN detalles_cita ON contacto.id_contacto = detalles_cita.id_contacto and detalles_cita.id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err  

    def read_citas_contacto(self, id_contacto):
        try:
            sql =  'SELECT cita.* FROM cita JOIN detalles_cita ON cita.id_cita = detalles_cita.id_cita and detalles_cita.id_contacto = %s'
            vals = (id_contacto,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err 

    def read_detalles_cita(self, id_cita):
        try:
            sql = 'SELECT * FROM detalles_cita WHERE id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err  

    def update_detalles_cita(self, fields, vals):
        try:
            sql = 'UPDATE detalles_cita SET '+','.join(fields)+' WHERE id_cita = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_detalles_cita(self, id_cita,id_contacto):
        try:
            sql = 'DELETE id_contacto FROM detalles_cita WHERE id_cita = %s and id_contacto=%s'  
            vals = (id_cita,id_contacto)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err