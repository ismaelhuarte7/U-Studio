from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from database.models.producto import Producto  # Importamos la clase Producto

class ProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Registrar Producto")
        self.setGeometry(150, 150, 300, 250)

        layout = QVBoxLayout()

        # Nombre del producto
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Nombre del Producto")

        # Marca del producto
        self.brand_input = QLineEdit(self)
        self.brand_input.setPlaceholderText("Marca del Producto")

        # Precio del producto
        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Precio del Producto")
        self.price_input.setValidator(QDoubleValidator(0.01, 999999.99, 2))  # Permite decimales

        # Stock del producto
        self.stock_input = QLineEdit(self)
        self.stock_input.setPlaceholderText("Stock Inicial")
        self.stock_input.setValidator(QIntValidator(0, 999999))  # Solo permite números enteros

        # Botón de guardar
        self.btn_save = QPushButton("Guardar Producto", self)
        self.btn_save.clicked.connect(self.save_product)

        # Agregar widgets al layout
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Marca:"))
        layout.addWidget(self.brand_input)
        layout.addWidget(QLabel("Precio:"))
        layout.addWidget(self.price_input)
        layout.addWidget(QLabel("Stock:"))
        layout.addWidget(self.stock_input)
        layout.addWidget(self.btn_save)

        self.setLayout(layout)

    def save_product(self):
        name = self.name_input.text().strip()
        brand = self.brand_input.text().strip()
        price = self.price_input.text().strip()
        stock = self.stock_input.text().strip()

        # Validaciones
        if not name or not brand or not price or not stock:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        if not price.replace(".", "", 1).isdigit():  # Validar precio como número decimal
            QMessageBox.warning(self, "Error", "El precio debe ser un número válido.")
            return
        if not stock.isdigit():  # Validar stock como número entero
            QMessageBox.warning(self, "Error", "El stock debe ser un número entero.")
            return

        # Crear el producto y guardarlo
        producto = Producto(nombre=name, marca=brand, precio=float(price), stock=int(stock))
        producto.save()

        QMessageBox.information(self, "Éxito", "Producto registrado correctamente.")
        self.close()
