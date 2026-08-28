import numpy as np
import pandas as pd


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
    return tuple(coeficientes)# src/analisis.py
import numpy as np
import pandas as pd

def filtrar(df, columna, umbral):
    """Máscara booleana: devuelve solo filas donde df[columna] > umbral"""
    return df[df[columna] > umbral]

def resumen_por_grupo(df, col_grupo, cols_num):
    """groupby con agregación: mean, std, count por grupo"""
    return df.groupby(col_grupo)[cols_num].agg(['mean', 'std', 'count'])

def zscore(matriz):
    """
    Normaliza matriz 2D por columna usando broadcasting.
    Fórmula: (m - m.mean(axis=0)) / m.std(axis=0)
    Prohibido usar for loops.
    """
    return (matriz - matriz.mean(axis=0)) / matriz.std(axis=0)

def top_k(df, columna, k):
    """Los k registros con mayor valor usando np.argsort"""
    indices = np.argsort(df[columna].values)[-k:][::-1]
    return df.iloc[indices]

def recta_minimos_cuadrados(x, y):
    """
    Ajusta y = a*x + b usando np.linalg.lstsq
    Devuelve tupla (a, b)
    
    Tip: armar matriz de diseño apilando x junto a columna de unos
    """
    A = np.column_stack([x, np.ones(len(x))])
    coefs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    return coefs[0], coefs[1]