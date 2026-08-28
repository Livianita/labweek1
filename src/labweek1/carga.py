from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

DEFAULT_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
DEFAULT_OUTPUT = Path("data/limpio.parquet")


def cargar(url: str, na_values: list[str] | list[int] | None = None) -> pd.DataFrame:
    return pd.read_csv(url, na_values=na_values)


def reporte_nulos(df: pd.DataFrame) -> pd.DataFrame:
    nulos = df.isna().sum()
    porcentaje = (nulos / len(df)) * 100 if len(df) else pd.Series(0.0, index=df.columns)

    return (
        pd.DataFrame({"columna": df.columns, "nulos": nulos.values, "porcentaje": porcentaje.values})
        .sort_values(by=["nulos", "porcentaje"], ascending=False)
        .reset_index(drop=True)
    )


def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    limpio = df.copy()
    limpio = limpio.replace([np.inf, -np.inf], np.nan)

    columnas_texto = limpio.select_dtypes(include=["object", "string"]).columns
    for columna in columnas_texto:
        serie = limpio[columna]
        limpio[columna] = serie.map(lambda valor: valor.strip().lower() if isinstance(valor, str) else valor)

    limpio = limpio.drop_duplicates()

    columnas_a_eliminar: list[str] = []

    for columna in limpio.columns:
        porcentaje_nulos = limpio[columna].isna().mean()

        if porcentaje_nulos >= 0.8:
            columnas_a_eliminar.append(columna)
            continue

        if not limpio[columna].isna().any():
            continue

        if pd.api.types.is_numeric_dtype(limpio[columna]):
            mediana = limpio[columna].median()
            limpio[columna] = limpio[columna].fillna(mediana)
            continue

        moda = limpio[columna].mode(dropna=True)
        if not moda.empty:
            limpio[columna] = limpio[columna].fillna(moda.iloc[0])
        else:
            limpio[columna] = limpio[columna].fillna("desconocido")

    if columnas_a_eliminar:
        limpio = limpio.drop(columns=columnas_a_eliminar)

    return limpio.reset_index(drop=True)


def guardar(df: pd.DataFrame, ruta: str | Path) -> None:
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(destino, index=False)


if __name__ == "__main__":
    datos_crudos = cargar(DEFAULT_URL)
    print("Reporte de nulos original:")
    print(reporte_nulos(datos_crudos).to_string(index=False))

    datos_limpios = limpiar(datos_crudos)
    guardar(datos_limpios, DEFAULT_OUTPUT)
    print(f"\nArchivo limpio guardado en {DEFAULT_OUTPUT}")
