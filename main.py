import sys
import argparse
from PyQt6.QtWidgets import QApplication
from ui.app import App
from database.db_manager import reset_database  # Importar la función de reset
from database import init_db  # Importar la nueva función de inicialización
from database.db_manager import seed  # Importar la función de seed

def parse_args():
    parser = argparse.ArgumentParser(description="Iniciar la aplicación de gestión de stock.")
    parser.add_argument(
        '--reset', 
        action='store_true', 
        help='Resetea la base de datos antes de iniciar la aplicación'
    )
    parser.add_argument(
        '--seed', 
        action='store_true', 
        help='Ejecuta el seed para agregar datos de prueba a la base de datos'
    )
    return parser.parse_args()

if __name__ == "__main__":
    # Parsear los argumentos
    args = parse_args()

    print("Iniciando la aplicación...")

    # Si se pasa el argumento --reset, resetear la base de datos
    if args.reset:
        print("Reseteando la base de datos...")
        reset_database()

    # Si se pasa el argumento --seed, ejecutar el seed
    if args.seed:
        print("Sembrando la base de datos con datos de prueba...")
        seed()  # Llamar a la función seed

    # Crear las tablas si no existen
    init_db()  # Llamar a la nueva función para crear las tablas
    print("Tablas creadas correctamente.")
    
    # Iniciar la aplicación
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
