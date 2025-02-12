from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QDoubleSpinBox, QPushButton, QHBoxLayout, QComboBox
from database.models.producto import Producto, TipoProducto
from database.models.marca import Marca
from PyQt6 import QtCore

class ViewProducts(QWidget):
    def __init__(self):
        super().__init__()
        self.sort_order = QtCore.Qt.SortOrder.AscendingOrder  # Uso correcto de SortOrder
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lista de Productos")
        self.setGeometry(150, 150, 800, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Filtros de búsqueda
        filter_layout = QHBoxLayout()

        self.search_name = QLineEdit(self)
        self.search_name.setPlaceholderText("Buscar por nombre")
        filter_layout.addWidget(self.search_name)

        # ComboBox para marcas
        self.search_brand = QComboBox(self)
        self.search_brand.addItem("Seleccionar Marca")
        self.load_brands()
        filter_layout.addWidget(self.search_brand)

        # ComboBox para tipos
        self.search_type = QComboBox(self)
        self.search_type.addItem("Seleccionar Tipo")
        self.load_types()
        filter_layout.addWidget(self.search_type)

        self.min_price = QDoubleSpinBox(self)
        self.min_price.setPrefix("$")
        self.min_price.setRange(0.0, 10000.0)
        self.min_price.setDecimals(2)
        self.min_price.setSingleStep(0.1)
        filter_layout.addWidget(self.min_price)

        self.max_price = QDoubleSpinBox(self)
        self.max_price.setPrefix("$")
        self.max_price.setRange(0.0, 10000.0)
        self.max_price.setDecimals(2)
        self.max_price.setSingleStep(0.1)
        filter_layout.addWidget(self.max_price)

        self.search_button = QPushButton("Buscar", self)
        self.search_button.clicked.connect(self.load_products)
        filter_layout.addWidget(self.search_button)

        layout.addLayout(filter_layout)

        # Tabla de productos
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Nombre", "Marca", "Tipo", "Precio", "Stock"])
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().sectionClicked.connect(self.on_header_click)

        layout.addWidget(self.table)
        self.setLayout(layout)

        self.load_products()

    def on_header_click(self, logicalIndex):
        if logicalIndex == 3:  # Si es la columna de precios
            self.sort_order = (
                QtCore.Qt.SortOrder.DescendingOrder
                if self.sort_order == QtCore.Qt.SortOrder.AscendingOrder
                else QtCore.Qt.SortOrder.AscendingOrder
            )
            self.load_products()

    def load_brands(self):
        marcas = Marca.get_all()
        for marca in marcas:
            self.search_brand.addItem(marca.nombre, marca.id)

    def load_types(self):
        for tipo in TipoProducto:
            self.search_type.addItem(tipo.value)

    def load_products(self):
        nombre = self.search_name.text()
        marca = self.search_brand.currentText() if self.search_brand.currentIndex() > 0 else ""
        tipo = self.search_type.currentText() if self.search_type.currentIndex() > 0 else ""
        precio_min = self.min_price.value()
        precio_max = self.max_price.value()

        productos = Producto.get_filtered(nombre, marca, tipo, precio_min, precio_max, self.sort_order)

        self.table.setRowCount(len(productos))

        for row, producto in enumerate(productos):
            self.table.setItem(row, 0, QTableWidgetItem(producto.nombre))
            self.table.setItem(row, 1, QTableWidgetItem(producto.marca.nombre))
            self.table.setItem(row, 2, QTableWidgetItem(producto.tipo.value))
            self.table.setItem(row, 3, QTableWidgetItem(f"${producto.precio:.2f}"))
            self.table.setItem(row, 4, QTableWidgetItem(str(producto.stock)))

        self.table.resizeColumnsToContents()
