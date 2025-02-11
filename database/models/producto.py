from enum import Enum
from database.db_manager import get_connection
from database.models.marca import Marca

# Definir un Enum para los tipos de producto
class TipoProducto(Enum):
    ACCESORIO = "Accesorio"
    REMERA = "Remera"
    JEAN = "Jean"
    SHORT = "Short"
    HODDIE = "Hoddie"
    CALZADO = "Calzado"
    CAMISA = "Camisa"
    # Agrega más tipos según sea necesario

class Producto:
    def __init__(self, id=None, nombre="", marca=None, precio=0.0, stock=0, tipo=None):
        self.id = id
        self.nombre = nombre
        self.marca = marca  # Ahora será una instancia de la clase Marca
        self.precio = precio
        self.stock = stock
        self.tipo = tipo

    @staticmethod
    def create_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(255) NOT NULL,
                            marca_id INT NOT NULL,
                            precio DECIMAL(10, 2) NOT NULL,
                            stock INT NOT NULL,
                            tipo VARCHAR(255) NOT NULL,
                            FOREIGN KEY (marca_id) REFERENCES marcas(id))''')  # Agregar la clave foránea
        conn.commit()
        conn.close()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE productos SET nombre=%s, marca_id=%s, precio=%s, stock=%s, tipo=%s WHERE id=%s",
                           (self.nombre, self.marca.id, self.precio, self.stock, self.tipo.value, self.id))
        else:
            cursor.execute("INSERT INTO productos (nombre, marca_id, precio, stock, tipo) VALUES (%s, %s, %s, %s, %s)",
                           (self.nombre, self.marca.id, self.precio, self.stock, self.tipo.value))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT p.id, p.nombre, p.marca_id, p.precio, p.stock, p.tipo, 
                m.nombre AS marca_nombre
            FROM productos p
            JOIN marcas m ON p.marca_id = m.id
        """)

        productos = []
        for row in cursor.fetchall():
            id_producto, nombre, marca_id, precio, stock, tipo_str, marca_nombre = row
            
            marca = Marca(id=marca_id, nombre=marca_nombre)
            tipo = TipoProducto(tipo_str)  # Convertimos el string al Enum

            productos.append(Producto(id=id_producto, nombre=nombre, marca=marca, precio=precio, stock=stock, tipo=tipo))

        conn.close()
        return productos
    
    @staticmethod
    def get_by_marca(marca_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.id, p.nombre, p.marca_id, p.precio, p.stock, p.tipo, m.nombre
            FROM productos p
            JOIN marcas m ON p.marca_id = m.id
            WHERE p.marca_id = %s
        """, (marca_id,))
        
        productos = []
        for row in cursor.fetchall():
            id_producto, nombre, marca_id, precio, stock, tipo_str, marca_nombre = row
            marca = Marca(id=marca_id, nombre=marca_nombre)
            tipo = TipoProducto(tipo_str)
            productos.append(Producto(id=id_producto, nombre=nombre, marca=marca, precio=precio, stock=stock, tipo=tipo))
        
        conn.close()
        return productos

