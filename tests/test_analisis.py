# tests/test_analisis.py
import numpy as np
import pandas as pd
import pytest
from src.analisis import zscore, resumen_por_grupo, filtrar, top_k, recta_minimos_cuadrados

@pytest.fixture
def df_mini():
    return pd.DataFrame({
        "grupo": ["a", "a", "b", "b"],
        "valor": [10.0, 20.0, 30.0, 40.0],
    })

def test_filtrar_deja_solo_los_mayores():
    df = pd.DataFrame({"edad": [10, 25, 40]})
    resultado = filtrar(df, "edad", 20)
    assert len(resultado) == 2
    assert resultado["edad"].min() > 20

def test_zscore_tiene_media_cero(df_mini):
    z = zscore(df_mini[["valor"]].to_numpy())
    assert z.mean() == pytest.approx(0.0, abs=1e-9)

def test_zscore_desviacion_uno(df_mini):
    z = zscore(df_mini[["valor"]].to_numpy())
    assert z.std() == pytest.approx(1.0, abs=1e-9)

def test_resumen_por_grupo_calcula_media(df_mini):
    r = resumen_por_grupo(df_mini, "grupo", ["valor"])
    assert r.loc["a", ("valor", "mean")] == pytest.approx(15.0)

def test_recta_minimos_cuadrados_perfecta():
    x = np.array([0, 1, 2])
    y = np.array([1, 3, 5])  # y = 2x + 1
    a, b = recta_minimos_cuadrados(x, y)
    assert a == pytest.approx(2.0, abs=1e-9)
    assert b == pytest.approx(1.0, abs=1e-9)

def test_top_k(df_mini):
    result = top_k(df_mini, "valor", 2)
    assert len(result) == 2
    assert result["valor"].iloc[0] == 40.0