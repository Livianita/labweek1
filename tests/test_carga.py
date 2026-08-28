import numpy as np
import pandas as pd

from src.labweek1.carga import limpiar, reporte_nulos


def test_limpiar_elimina_duplicados_y_normaliza_texto():
    df = pd.DataFrame(
        {
            "nombre": [" Ana ", "ana", "Luis"],
            "edad": [20, 20, 30],
            "cabina": ["C85", "C85", "E12"],
        }
    )

    resultado = limpiar(df)

    assert len(resultado) == 2
    assert "ana" in resultado["nombre"].values
    assert " Ana " not in resultado["nombre"].values


def test_limpiar_reemplaza_inf_e_imputa_numericos():
    df = pd.DataFrame(
        {
            "edad": [10.0, np.inf, 30.0],
            "fare": [7.25, np.nan, 8.05],
        }
    )

    resultado = limpiar(df)

    assert not np.isinf(resultado[["edad", "fare"]].to_numpy()).any()
    assert not resultado[["edad", "fare"]].isna().any().any()


def test_reporte_nulos_devuelve_conteo_por_columna():
    df = pd.DataFrame(
        {
            "a": [1, None, 3],
            "b": [None, None, 2],
        }
    )

    resultado = reporte_nulos(df)

    assert list(resultado["columna"]) == ["b", "a"]
    assert list(resultado["nulos"]) == [2, 1]