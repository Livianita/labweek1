import matplotlib.pyplot as plt
import pandas as pd

from src.labweek1.carga import DEFAULT_URL, cargar, limpiar


def tasa_por_grupo(df: pd.DataFrame, columna: str, grupos: pd.Series) -> pd.DataFrame:
    datos = df[[columna, "Survived"]].copy()
    datos["grupo"] = grupos

    return (
        datos.groupby("grupo", observed=True)["Survived"]
        .agg(tasa_supervivencia="mean", pasajeros="count")
        .assign(tasa_supervivencia=lambda tabla: tabla["tasa_supervivencia"] * 100)
        .reset_index()
    )


def crear_graficos(df: pd.DataFrame) -> None:
    rangos_edad = pd.cut(
        df["Age"],
        bins=[0, 12, 18, 30, 50, float("inf")],
        labels=["0-12", "13-18", "19-30", "31-50", "51+"],
    )
    supervivencia_por_edad = tasa_por_grupo(df, "Age", rangos_edad)

    plt.figure(figsize=(8, 5))
    plt.bar(
        supervivencia_por_edad["grupo"].astype(str),
        supervivencia_por_edad["tasa_supervivencia"],
        color="#27ae60",
    )
    plt.xlabel("Rango de edad")
    plt.ylabel("Tasa de supervivencia (%)")
    plt.title("Edad y tasa de supervivencia")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig("edad_vs_sobrev.png")
    plt.close()

    rangos_tarifa = pd.qcut(df["Fare"], q=4, duplicates="drop")
    supervivencia_por_tarifa = tasa_por_grupo(df, "Fare", rangos_tarifa)

    plt.figure(figsize=(9, 5))
    plt.bar(
        supervivencia_por_tarifa["grupo"].astype(str),
        supervivencia_por_tarifa["tasa_supervivencia"],
        color="#2f80ed",
    )
    plt.xlabel("Rango de tarifa pagada")
    plt.ylabel("Tasa de supervivencia (%)")
    plt.title("Tarifa pagada y tasa de supervivencia")
    plt.ylim(0, 100)
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig("tarifa_vs_sobrev.png")
    plt.close()

    print("Gráficos guardados en edad_vs_sobrev.png y tarifa_vs_sobrev.png")


if __name__ == "__main__":
    datos = limpiar(cargar(DEFAULT_URL))
    crear_graficos(datos)