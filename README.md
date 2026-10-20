# Parcial Segundo Cómputo – Programación Computacional III

## Integrantes
- Xiomara Elizabeth Alfaro Ortez
- María Fernanda Orellana Argueta

## Descripción del proyecto
Este proyecto consiste en el análisis del inventario de una empresa salvadoreña que comercializa productos en cinco sucursales: San Salvador, Santa Ana, San Miguel, La Libertad y Sonsonate.

Se utilizó Python y la biblioteca Pandas para analizar los datos del inventario. Además, se desarrolló una aplicación gráfica con PyQt5 y Matplotlib para visualizar la información mediante tablas y gráficos.

## Tecnologías utilizadas
- Python
- Pandas
- PyQt5
- Matplotlib
- CSV

## Archivos del proyecto
- `datos.csv`: contiene los registros del inventario.
- `inventario.py`: realiza el análisis de datos mediante Pandas.
- `ventana.py`: contiene la aplicación gráfica.
- `requirements.txt`: incluye las bibliotecas necesarias.
- `.gitignore`: excluye archivos temporales.
- `informe_consultoria.pdf`: presenta los resultados, conclusiones y recomendaciones.

## Instalación y ejecución

Primero, instalar las bibliotecas necesarias:

```bash
pip install -r requirements.txt
```

Para ejecutar el análisis del inventario:

```bash
python inventario.py
```

Para abrir la aplicación gráfica:

```bash
python ventana.py
```

## Información del inventario
El conjunto de datos contiene 50 registros y seis columnas: Sucursal, Producto, Categoria, Precio, Stock y Stock_Minimo.

La aplicación permite visualizar las existencias por sucursal y consultar los productos registrados.
