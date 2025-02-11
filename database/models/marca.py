from database.db_manager import get_connection
from datetime import datetime

class Marca:
    def __init__(self, id=None, nombre="", telefono="", duracion_contrato=0, fecha_inicio_contrato=None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.duracion_contrato = duracion_contrato
        self.fecha_inicio_contrato = fecha_inicio_contrato if fecha_inicio_contrato else datetime.today().strftime('%Y-%m-%d')

    @staticmethod
    def create_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS marcas (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(255) NOT NULL,
                            telefono VARCHAR(255),
                            duracion_contrato INT NOT NULL,
                            fecha_inicio_contrato DATE NOT NULL)''')
        conn.commit()
        conn.close()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE marcas SET nombre=%s, telefono=%s, duracion_contrato=%s, fecha_inicio_contrato=%s WHERE id=%s",
                           (self.nombre, self.telefono, self.duracion_contrato, self.fecha_inicio_contrato, self.id))
        else:
            cursor.execute("INSERT INTO marcas (nombre, telefono, duracion_contrato, fecha_inicio_contrato) VALUES (%s, %s, %s, %s)",
                           (self.nombre, self.telefono, self.duracion_contrato, self.fecha_inicio_contrato))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM marcas")
        marcas = [Marca(*row) for row in cursor.fetchall()]
        conn.close()
        return marcas

    @staticmethod
    def get_by_id(marca_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM marcas WHERE id = %s", (marca_id,))
        row = cursor.fetchone()
        conn.close()
        return Marca(*row) if row else None
