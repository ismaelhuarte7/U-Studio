from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from database.models.producto import Producto  # Importamos la clase Producto
from database.models.venta import Venta  # Importamos la clase Venta

class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Registrar Venta")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        # Dropdown para seleccionar el producto
        self.product_dropdown = QComboBox(self)
        self.load_products()

        # Campo de cantidad
        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Cantidad")
        self.quantity_input.setValidator(QLineEdit().validator())  # Asegura solo números

        # Botón para registrar la venta
        self.btn_register_sale = QPushButton("Registrar Venta", self)
        self.btn_register_sale.clicked.connect(self.register_sale)

        # Agregar widgets al layout
        layout.addWidget(QLabel("Producto:"))
        layout.addWidget(self.product_dropdown)
        layout.addWidget(QLabel("Cantidad:"))
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.btn_register_sale)

        self.setLayout(layout)

    def load_products(self):
        productos = Producto.get_all()  # Usamos el método get_all de Producto

        # Llenamos el ComboBox con los productos
        for producto in productos:
            self.product_dropdown.addItem(producto.nombre, producto.id)

    def register_sale(self):
        product_id = self.product_dropdown.currentData()  # ID del producto seleccionado
        quantity = self.quantity_input.text()

        # Validación de cantidad
        if not quantity.isdigit():
            QMessageBox.warning(self, "Error", "La cantidad debe ser un número.")
            return

        quantity = int(quantity)

        # Obtenemos el producto seleccionado
        producto = next((p for p in Producto.get_all() if p.id == product_id), None)

        if not producto:
            QMessageBox.warning(self, "Error", "Producto no encontrado.")
            return

        # Verificamos si hay stock suficiente
        if producto.stock >= quantity:
            # Calculamos el total
            total = producto.precio * quantity

            # Creamos la venta
            venta = Venta(producto_id=product_id, cantidad=quantity, total=total)
            venta.save()  # Guardamos la venta usando el método save de Venta

            # Actualizamos el stock
            producto.stock -= quantity
            producto.save()  # Actualizamos el producto

            QMessageBox.information(self, "Éxito", "Venta registrada correctamente.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Stock insuficiente.")
