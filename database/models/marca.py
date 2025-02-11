from database.db_manager import get_connection

class Marca:
    def __init__(self, id=None, nombre="", telefono="", duracion_contrato=0):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.duracion_contrato = duracion_contrato

    @staticmethod
    def create_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS marcas (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(255) NOT NULL,
                            telefono VARCHAR(255),
                            duracion_contrato INT NOT NULL)''')
        conn.commit()
        conn.close()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE marcas SET nombre=%s, telefono=%s, duracion_contrato=%s WHERE id=%s",
                           (self.nombre, self.telefono, self.duracion_contrato, self.id))
        else:
            cursor.execute("INSERT INTO marcas (nombre, telefono, duracion_contrato) VALUES (%s, %s, %s)",
                           (self.nombre, self.telefono, self.duracion_contrato))
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
