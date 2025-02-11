from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from database.models.marca import Marca
from database.models.producto import Producto

class ViewBrands(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lista de Marcas")
        self.setGeometry(150, 150, 600, 400)

        layout = QVBoxLayout()

        # Tabla de marcas
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.load_brands()

    def load_brands(self):
        marcas = Marca.get_all()

        self.table.setRowCount(len(marcas))
        self.table.setColumnCount(2)  # Columnas: Nombre, Ver Detalles
        self.table.setHorizontalHeaderLabels(["Nombre", "Acción"])

        for row, marca in enumerate(marcas):
            self.table.setItem(row, 0, QTableWidgetItem(marca.nombre))
            btn_detalle = QPushButton("Ver Detalles")
            btn_detalle.clicked.connect(lambda _, m=marca: self.show_brand_details(m))
            self.table.setCellWidget(row, 1, btn_detalle)

        self.table.resizeColumnsToContents()

    def show_brand_details(self, marca):
        self.brand_details = ViewBrandDetails(marca.id)
        self.brand_details.show()

class ViewBrandDetails(QWidget):
    def __init__(self, marca_id):
        super().__init__()
        self.marca_id = marca_id
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Detalles de la Marca")
        self.setGeometry(150, 150, 600, 400)

        layout = QVBoxLayout()

        # Cargar información de la marca
        self.marca = Marca.get_by_id(self.marca_id)
        if not self.marca:
            self.close()
            return

        self.label_nombre = QLabel(f"Nombre: {self.marca.nombre}")
        self.label_telefono = QLabel(f"Teléfono: {self.marca.telefono}")
        self.label_duracion = QLabel(f"Duración del contrato: {self.marca.duracion_contrato} meses")
        self.label_fecha_inicio = QLabel(f"Fecha de inicio del contrato: {self.marca.fecha_inicio_contrato}")

        layout.addWidget(self.label_nombre)
        layout.addWidget(self.label_telefono)
        layout.addWidget(self.label_duracion)
        layout.addWidget(self.label_fecha_inicio)

        self.setLayout(layout)
