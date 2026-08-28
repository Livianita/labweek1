import matplotlib.pyplot as plt
import pandas as pd

from src.labweek1.carga import DEFAULT_URL, cargar, limpiar


def calcular_supervivencia_por_tarifa(df: pd.DataFrame) -> pd.DataFrame:
    datos = df[["Fare", "Survived"]].copy()
    datos["rango_tarifa"] = pd.qcut(datos["Fare"], q=4, duplicates="drop")

    return (
        datos.groupby("rango_tarifa", observed=True)["Survived"]
        .agg(tasa_supervivencia="mean", pasajeros="count")
        .assign(tasa_supervivencia=lambda tabla: tabla["tasa_supervivencia"] * 100)
        .reset_index()
    )


if __name__ == "__main__":
    datos = limpiar(cargar(DEFAULT_URL))
    resumen = calcular_supervivencia_por_tarifa(datos)

    print(resumen.to_string(index=False))

    etiquetas = resumen["rango_tarifa"].astype(str)
    plt.figure(figsize=(9, 5))
    plt.bar(etiquetas, resumen["tasa_supervivencia"], color="#2f80ed")
    plt.xlabel("Rango de tarifa pagada")
    plt.ylabel("Tasa de supervivencia (%)")
    plt.title("Relación entre tarifa pagada y tasa de supervivencia")
    plt.ylim(0, 100)
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig("figura_tarifa_supervivencia.png")
    plt.close()
    print("Gráfico guardado en figura_tarifa_supervivencia.png")