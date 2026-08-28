# Lab Semana 1 - <Titanic>
 - Persona A: <Livia Rojas>
 - Persona B: <Wilmer Puerta>
 - Dataset: <https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv>
 - Tarea: <clasificacion>   Variable objetivo: <Survived>
 
## Como correr
 
    uv sync
    uv run pytest -q
    uv run python main.py
    uv run python grafico_tarifa_supervivencia.py
    uv run python graficos_adicionales.py
 
## Hallazgos
- (A) La columna `Cabin` concentra la mayor cantidad de valores faltantes, por lo que no aporta suficiente información confiable para conservarla en la limpieza inicial.
- (B) Se observa una tasa de sobrevivientes mayor relacionada con el mayor costo del boleto 
 
## Decisiones de limpieza
Se eliminó `Cabin` porque tiene una gran proporción de valores faltantes 77.01%.
- Los valores faltantes en columnas numéricas se completan con la mediana para no perder filas.
- Los valores faltantes en columnas de texto se completan con la moda para conservar la mayor cantidad de datos.
- Se normalizó el texto con `strip()` y `lower()` y luego se eliminaron duplicados.

## Preguntas de investigación

1. `uv sync` puede reconstruir el entorno aunque `.venv/` no esté versionado porque usa `uv.lock`. Este archivo guarda las versiones exactas y las dependencias resueltas del proyecto, permitiendo instalar el mismo entorno en otra computadora.

2. `pytest` puede ejecutarse con el Python y las dependencias disponibles en el sistema, aunque el entorno virtual no esté activado. `uv run pytest` ejecuta las pruebas dentro del entorno administrado por uv y usa las dependencias declaradas y bloqueadas del proyecto.
