
import sys
import pandas as pd

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QComboBox,
    QTableWidget, QTableWidgetItem
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Inventario")
        self.resize(950, 700)

        # Leer los datos del inventario
        self.df = pd.read_csv("datos.csv")

        # Crear la ventana
        central = QWidget()
        layout = QVBoxLayout()

        # Titulo
        titulo = QLabel("INVENTARIO DE SUCURSALES")
        titulo.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: #234a7d;"
        )
        layout.addWidget(titulo)

        # Seleccionar sucursal
        layout.addWidget(QLabel("Seleccione una sucursal:"))

        self.selector = QComboBox()
        self.selector.addItem("Todas las sucursales")
        self.selector.addItems(self.df["Sucursal"].unique())

        layout.addWidget(self.selector)

        # Resumen
        self.resumen = QLabel()
        self.resumen.setStyleSheet(
            "font-size: 14px; padding: 8px;"
        )
        layout.addWidget(self.resumen)

        # Grafico
        self.figura = Figure(figsize=(7, 3))
        self.canvas = FigureCanvas(self.figura)

        layout.addWidget(self.canvas)

        # Tabla de inventario
        layout.addWidget(QLabel("LISTADO DE PRODUCTOS"))

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)

        self.tabla.setHorizontalHeaderLabels([
            "Sucursal", "Producto", "Categoria",
            "Precio", "Stock", "Stock Minimo"
        ])

        layout.addWidget(self.tabla)

        # Colocar elementos en la ventana
        central.setLayout(layout)
        self.setCentralWidget(central)

        # Actualizar al cambiar de sucursal
        self.selector.currentTextChanged.connect(
            self.actualizar
        )

        # Mostrar datos al iniciar
        self.actualizar()

    def actualizar(self):

        sucursal = self.selector.currentText()

        # Filtrar los datos
        if sucursal == "Todas las sucursales":
            datos = self.df
        else:
            datos = self.df[
                self.df["Sucursal"] == sucursal
            ]

        # Resumen del inventario
        registros = len(datos)
        stock_total = datos["Stock"].sum()

        self.resumen.setText(
            f"Registros: {registros}    |    "
            f"Stock total: {stock_total}"
        )

        # Crear grafico
        serie = datos.groupby("Sucursal")["Stock"].sum()

        self.figura.clear()
        ax = self.figura.add_subplot(111)

        ax.bar(serie.index, serie.values, color="steelblue")

        ax.set_title("Stock por sucursal")
        ax.set_xlabel("Sucursal")
        ax.set_ylabel("Unidades")
        ax.tick_params(axis="x", rotation=15)

        self.figura.tight_layout()
        self.canvas.draw()

        # Llenar tabla
        self.tabla.setRowCount(len(datos))

        for fila, (_, registro) in enumerate(datos.iterrows()):
            for columna, valor in enumerate(registro):
                self.tabla.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(str(valor))
                )

        self.tabla.resizeColumnsToContents()


app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

sys.exit(app.exec_())
