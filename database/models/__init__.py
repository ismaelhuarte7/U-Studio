from database.models.producto import Producto
from database.models.venta import Venta
from database.models.marca import Marca

def create_all_tables():
    Marca.create_table()
    Producto.create_table()
    Venta.create_table()
