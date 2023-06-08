import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense


def annade_RN(self):
    modelo = Sequential()
    modelo.add(LSTM(units=50, input_shape=(self.time_step, self.num_dias_pred)))
    modelo.add(Dense(units=self.num_dias_pred))
    self.modelo = modelo

def cuestionario(self):
    while(True):
        try:
            self.epocas = int(input("¿Cuántas epocas quieres hacer?: "))
            self.tamano_lote = int(input("¿Cuántos lotes quieres hacer?: "))
            break  # Importante romper la iteración si todo ha salido bien
        except:
            print("Ha ocurrido un error, introduce bien el número") 
        

def entrenamiento(self, epocas=20, tamano_lotes=20):
    cuestionario(self)
    self.modelo.fit(self.X_train, self.Y_train, epochs=epocas, batch_size=tamano_lotes)

def prediccion(self, x_test,time_step,num_dias_pred):
    X_test = []
    for i in range(time_step, len(x_test)):
        X_test.append(x_test[i-time_step:i,0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], num_dias_pred))    
