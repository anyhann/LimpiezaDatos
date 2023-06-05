import matplotlib as plt

def grafico_sets(dataframe, columna_tiempo, fecha_inicio_validacion, columna_valores):
    posicion = dataframe.index.get_loc(fecha_inicio_validacion)
    
    set_entrenamiento = dataframe[columna_valores].iloc[:posicion-1]
    set_validacion = dataframe[columna_valores].iloc[posicion:]
    
    set_entrenamiento.plot(legend=True)
    set_validacion.plot(legend=True)
    
    plt.legend(['Entrenamiento', 'Validación'])
    plt.show()


