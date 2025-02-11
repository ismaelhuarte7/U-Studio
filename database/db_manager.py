import pymysql
import os
from dotenv import load_dotenv

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

