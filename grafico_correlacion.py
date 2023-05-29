
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib as plt


def grafico_autocorrelacion (columna_objetivo, num_lags):
    fig, ax = plt.subplots(figsize=(7, 3))
    plot_acf(columna_objetivo, ax=ax, lags=num_lags)
    plt.show()