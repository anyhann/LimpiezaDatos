
import matplotlib.pyplot as plt

def grafico_datos_train_y_validacion_LSTM (set_entrenamiento,set_validacion, columna_objetivo):
    set_entrenamiento[columna_objetivo].plot(legend=True)
    set_validacion[columna_objetivo].plot(legend=True)
    plt.legend(['Entrenamiento', 'Validación'])
    plt.show()