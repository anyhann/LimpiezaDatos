import matplotlib as plt

#Función que separa los datos del train y del test en un grafico
def separa_train_val(self, fecha_inicio_validacion):
    dataframe = self.dataframe
    posicion = dataframe.index.get_loc(fecha_inicio_validacion)

    self.set_entrenamiento = dataframe.iloc[:posicion]
    self.set_validacion = dataframe.iloc[posicion:]
    grafico_sets(self)
    
def grafico_sets(self):  
    self.set_entrenamiento[self.columna_valores].plot(legend=True)
    self.set_validacion[self.columna_valores].plot(legend=True)
    plt.legend(['Entrenamiento', 'Validación'])
    plt.show()






