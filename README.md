# Lab Semana 1 - <Titanic>
 - Persona A: <Livia Rojas>
 - Persona B: <Wilmer Puerta>
 - Dataset: <https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv>
 - Tarea: <clasificacion>   Variable objetivo: <Survived>
 
## Como correr
 
    uv sync
    uv run pytest -q
    uv run python main.py
 
## Hallazgos
- (A) La columna `Cabin` concentra la mayor cantidad de valores faltantes, por lo que no aporta suficiente información confiable para conservarla en la limpieza inicial.
 
## Decisiones de limpieza
Se eliminó `Cabin` porque tiene una gran proporción de valores faltantes 77.01%.
- Los valores faltantes en columnas numéricas se completan con la mediana para no perder filas.
- Los valores faltantes en columnas de texto se completan con la moda para conservar la mayor cantidad de datos.
- Se normalizó el texto con `strip()` y `lower()` y luego se eliminaron duplicados.