import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from carga_datos import cargador

def plot_correlation_heatmap(data):
    f, ax = plt.subplots(figsize=(10, 8))
    corr = data.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
                cmap=sns.diverging_palette(220, 10, as_cmap=True), square=True, ax=ax)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    data = cargador(os.path.join(os.path.dirname(main_file_path), "hormigon.csv"))
    plot_correlation_heatmap(data)
