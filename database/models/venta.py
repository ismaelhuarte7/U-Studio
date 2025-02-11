from database.db_manager import get_connection

class Venta:
    def __init__(self, id=None, producto_id=None, cantidad=0, total=0.0):
        self.id = id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.total = total

    @staticmethod
    def create_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            producto_id INT,
                            cantidad INT NOT NULL,
                            total DECIMAL(10, 2) NOT NULL,
                            FOREIGN KEY (producto_id) REFERENCES productos(id))''')
        conn.commit()
        conn.close()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ventas (producto_id, cantidad, total) VALUES (%s, %s, %s)",
                       (self.producto_id, self.cantidad, self.total))
        self.id = cursor.lastrowid  # MySQL usa lastrowid para obtener el ID insertado
        conn.commit()
        conn.close()
