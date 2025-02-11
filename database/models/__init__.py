from database.models.producto import Producto
from database.models.venta import Venta

def create_all_tables():
    Producto.create_table()
    Venta.create_table()
