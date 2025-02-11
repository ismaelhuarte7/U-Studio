import sys
from PyQt6.QtWidgets import QApplication
from ui.app import App
from database.models import create_all_tables

if __name__ == "__main__":
    print("Iniciando la aplicación...")
    create_all_tables()  # Crea las tablas si no existen
    print("Tablas creadas correctamente.")
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
