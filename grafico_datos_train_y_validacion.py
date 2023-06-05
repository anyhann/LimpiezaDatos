def grafico_sets(dataframe, columna_tiempo, fecha_inicio_validacion, columna_valores):
    dataframe = dataframe.reset_index()
    posicion = dataframe[columna_tiempo].index(fecha_inicio_validacion)
    
    set_entrenamiento = dataframe[columna_valores].iloc[:posicion-1]
    set_validacion = dataframe[columna_valores].iloc[posicion:]
    
    set_entrenamiento.plot(legend=True)
    set_validacion.plot(legend=True)
    
    plt.legend(['Entrenamiento', 'Validación'])
    plt.show()

