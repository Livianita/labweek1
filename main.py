import matplotlib.pyplot as plt

from src.analisis import recta_minimos_cuadrados, resumen_por_grupo, top_k
from src.labweek1.carga import DEFAULT_URL, cargar, limpiar, reporte_nulos

if __name__ == "__main__":
    datos_crudos = cargar(DEFAULT_URL)

    print("Reporte de nulos del dataset crudo:")
    print(reporte_nulos(datos_crudos).to_string(index=False))

    datos_limpios = limpiar(datos_crudos)

    print("\nResumen por clase del dataset limpio:")
    resumen = resumen_por_grupo(datos_limpios, "Pclass", ["Age", "Fare", "Survived"])
    print(resumen)

    print("\nCinco pasajeros con mayor tarifa:")
    print(top_k(datos_limpios, "Fare", 5).to_string(index=False))

    pendiente, intercepto = recta_minimos_cuadrados(
        datos_limpios["Age"].to_numpy(),
        datos_limpios["Fare"].to_numpy(),
    )
    print(f"\nRecta Fare = a * Age + b: pendiente={pendiente:.4f}, intercepto={intercepto:.4f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(datos_limpios["Age"], datos_limpios["Fare"], alpha=0.4)
    plt.xlabel("Edad")
    plt.ylabel("Tarifa")
    plt.title("Relación entre edad y tarifa")
    plt.tight_layout()
    plt.savefig("figura.png")
    plt.close()
    print("Gráfico guardado en figura.png")