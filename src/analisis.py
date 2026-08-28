import numpy as np


def filtrar(df, columna, umbral):
    return df[df[columna] > umbral]


def resumen_por_grupo(df, col_grupo, cols_num):
    return df.groupby(col_grupo)[cols_num].agg(["mean", "std", "count"])


def zscore(matriz):
    matriz = np.asarray(matriz)
    return (matriz - matriz.mean(axis=0)) / matriz.std(axis=0)


def top_k(df, columna, k):
    indices = np.argsort(df[columna].to_numpy())[-k:][::-1]
    return df.iloc[indices]


def recta_minimos_cuadrados(x, y):
    matriz_diseno = np.column_stack([x, np.ones(len(x))])
    coeficientes, _, _, _ = np.linalg.lstsq(matriz_diseno, y, rcond=None)
    return tuple(coeficientes)