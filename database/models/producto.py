from database.db_manager import get_connection

class Producto:
    def __init__(self, id=None, nombre="", marca="", precio=0.0, stock=0):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock

    @staticmethod
    def create_table():
        print("Creando tabla productos...")
        conn = get_connection()
        
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(255) NOT NULL,
                            marca VARCHAR(255) NOT NULL,
                            precio DECIMAL(10, 2) NOT NULL,
                            stock INT NOT NULL)''')
        conn.commit()
        conn.close()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            # En MySQL, los parámetros en la consulta se pasan usando %s, no ?
            cursor.execute("UPDATE productos SET nombre=%s, marca=%s, precio=%s, stock=%s WHERE id=%s",
                           (self.nombre, self.marca, self.precio, self.stock, self.id))
        else:
            cursor.execute("INSERT INTO productos (nombre, marca, precio, stock) VALUES (%s, %s, %s, %s)",
                           (self.nombre, self.marca, self.precio, self.stock))
            self.id = cursor.lastrowid  # MySQL usa lastrowid para obtener el ID insertado
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = [Producto(*row) for row in cursor.fetchall()]
        conn.close()
        return productos
