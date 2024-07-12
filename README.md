### Sistema Experto con Redes Bayesianas para Gestión de Inventarios

Este proyecto implementa un sistema experto utilizando redes bayesianas para la gestión de inventarios, permitiendo tomar decisiones informadas sobre cuándo reponer el inventario basado en diversos factores como eventos especiales y tiempos de entrega.

#### Estructura del Proyecto

- **inventario.py:** Script principal que contiene la definición del modelo de red bayesiana, las CPDs, la lógica de inferencia y la interfaz de usuario para la entrada de datos y visualización de resultados.

#### Librerías Utilizadas

- **pgmpy:** Biblioteca para modelado probabilístico gráfico, incluyendo redes bayesianas y otros modelos probabilísticos.
- **numpy:** Biblioteca para cálculos numéricos y manipulación de matrices, utilizada para manejar probabilidades y datos.
- **pandas:** Herramienta para manipulación y análisis de datos, empleada para estructurar y organizar datos en tablas.

#### Instalación

Para ejecutar el proyecto, asegúrate de tener Python instalado junto con las siguientes librerías:

```bash
pip install pgmpy numpy pandas
