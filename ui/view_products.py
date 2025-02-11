from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from database.models.producto import Producto  # Importamos la clase Producto

class ViewProducts(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lista de Productos")
        self.setGeometry(150, 150, 500, 300)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_products()

    def load_products(self):
        productos = Producto.get_all()  # Obtener productos usando la clase Producto

        self.table.setRowCount(len(productos))
        self.table.setColumnCount(4)  # Ahora tenemos 4 columnas
        self.table.setHorizontalHeaderLabels(["Nombre", "Marca", "Precio", "Stock"])

        for row, producto in enumerate(productos):
            self.table.setItem(row, 0, QTableWidgetItem(producto.nombre))
            self.table.setItem(row, 1, QTableWidgetItem(producto.marca))
            self.table.setItem(row, 2, QTableWidgetItem(f"${producto.precio:.2f}"))  # Formatear precio
            self.table.setItem(row, 3, QTableWidgetItem(str(producto.stock)))

        self.table.resizeColumnsToContents()  # Ajustar el ancho de las columnas automáticamente
