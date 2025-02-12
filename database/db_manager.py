import pymysql
import os
from dotenv import load_dotenv
from random import randint, choice

load_dotenv()

def get_connection():
    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', '')
    db_name = os.getenv('DB_NAME', 'ustudiodb')

    conn = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name,
    )
    return conn 

def reset_database():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Obtener el nombre de todas las tablas
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Deshabilitar las verificaciones de claves foráneas temporalmente
        cursor.execute("SET foreign_key_checks = 0;")

        # Eliminar cada tabla
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]} CASCADE")  # Usar CASCADE para eliminar en cascada

        # Habilitar nuevamente las verificaciones de claves foráneas
        cursor.execute("SET foreign_key_checks = 1;")

        conn.commit()  # Confirmar cambios
        print("Base de datos reseteada exitosamente.")
    
    except Exception as e:
        print(f"Error al resetear la base de datos: {e}")
    
    finally:
        cursor.close()
        conn.close()

    from database.models.marca import Marca



def seed():
    from database.models.producto import Producto, TipoProducto
    from database.models.marca import Marca
    # Crear marcas
    marcas = [
        "Nike", "Adidas", "Puma", "Reebok", "Under Armour"
    ]

    marca_objects = []
    for marca in marcas:
        marca_obj = Marca(nombre=marca, telefono=f"1234-5678", duracion_contrato=2, fecha_inicio_contrato="2025-01-01")
        marca_obj.save()
        marca_objects.append(marca_obj)
    
    # Tipos de productos
    tipos_producto = [TipoProducto.ACCESORIO, TipoProducto.REMERA, TipoProducto.JEAN, TipoProducto.SHORT, TipoProducto.HODDIE, TipoProducto.CALZADO, TipoProducto.CAMISA]

    # Crear productos
    for marca in marca_objects:
        for _ in range(10):  # Crear 10 productos para cada marca
            tipo = choice(tipos_producto)
            producto = Producto(
                nombre=f"{marca.nombre} {tipo.value} {randint(1, 100)}",
                marca=marca,
                precio=round(randint(20, 150), 2),
                stock=randint(1, 50),
                tipo=tipo
            )
            producto.save()

    print("Seed completed.")



