
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib as plt
from LimpiezaDatos.utilidades.carga_datos import cargador

def grafico_auto (self, columna_valor, num_lags):
        fig, ax = plt.subplots(figsize=(7, 3))
        plot_acf(columna_valor, ax=ax, lags=num_lags)
        plt.show()

if __name__ == "__main__":
    datos = cargador("https://raw.githubusercontent.com/JoaquinAmatRodrigo/skforecast/master/data/vic_elec.csv")
