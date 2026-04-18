import csv
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent
ARCHIVO_DATOS = BASE_DIR / "tiempos_ordenacion.tsv"
ARCHIVO_GRAFICA = BASE_DIR / "grafica_comparativa_ordenacion.png"


def cargar_datos(ruta):
    tamanos = []
    quick = []
    merge = []
    heap = []
    bubble = []

    with ruta.open("r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter="\t")
        for fila in lector:
            tamanos.append(int(fila["n"]))
            quick.append(float(fila["quick_sort"]))
            merge.append(float(fila["merge_sort"]))
            heap.append(float(fila["heap_sort"]))
            bubble.append(float(fila["bubble_sort"]))

    return tamanos, quick, merge, heap, bubble


def main():
    tamanos, quick, merge, heap, bubble = cargar_datos(ARCHIVO_DATOS)

    plt.figure(figsize=(11, 6))
    plt.plot(tamanos, quick, color="#1d4ed8", linewidth=2.0, marker="o", markersize=3, label="Quick Sort")
    plt.plot(tamanos, merge, color="#16a34a", linewidth=2.0, marker="s", markersize=3, label="Merge Sort")
    plt.plot(tamanos, heap, color="#f97316", linewidth=2.0, marker="^", markersize=3, label="Heap Sort")
    plt.plot(tamanos, bubble, color="#dc2626", linewidth=2.0, marker="d", markersize=3, label="Bubble Sort")

    plt.title("Comparativa de algoritmos de ordenacion (promedio de 3 ejecuciones)")
    plt.xlabel("n (numero de elementos)")
    plt.ylabel("tiempo (s)")
    plt.grid(True, linestyle="--", alpha=0.35)
    plt.legend()
    plt.tight_layout()
    plt.savefig(ARCHIVO_GRAFICA, dpi=140)


if __name__ == "__main__":
    main()
