# Importaciones básicas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler

# Importaciones para Series Temporales
from statsmodels.tsa.seasonal import seasonal_decompose
from arch.unitroot import PhillipsPerron as pprtest
from arch.unitroot import DFGLS
from statsmodels.tsa.stattools import adfuller, kpss, acf, pacf
from statsmodels.tsa.arima.model import ARIMA

# Gráficos
import plotly.graph_objects as go

# Importaciones locales
from captura_opciones import leer_opciones_pantalla
from carga_serie_temporal import auto_conversion_datetime
from descripciones import descripcion

class SerieTemporal:
    def __init__(self, dataframe, columna_temporal, columna_valores):
        self.dataframe = self.__conversion_a_serie_temp(dataframe, columna_temporal)
        self.columna_valores = columna_valores
        
    def __conversion_a_serie_temp(self, dataframe, columna):
        # Convertir la columna de texto a datetime
        dataframe[columna] = auto_conversion_datetime(dataframe[columna])
        dataframe.set_index(columna, inplace=True)
        dataframe = dataframe.asfreq(dataframe.index[1]-dataframe.index[0])
        print("La frecuencia de la serie temporal es:", dataframe.index.freq)
        dataframe = dataframe.sort_index()
        print(f'Número de filas con missing values: {dataframe.isnull().any(axis=1).sum()}')
        return dataframe

    # Exploraciones y Visualizaciones previas
    def descripcion(self):
        print(descripcion(self.dataframe))
        print("La frecuencia de la serie temporal es:", self.dataframe.index.freq)
        print(f'Número de filas con missing values: {self.dataframe.isnull().any(axis=1).sum()}')

    def visualizar_serie(self):
        """
        Visualizar las columnas de la serie de tiempo en gráficos separados. 
        No interactivo.
        """
        self.dataframe.plot(subplots=True, figsize=(10, 6))
        plt.show()

    def grafica_interactiva(self):
        """
        Gráfica interactiva de la columna que contiene la serie a estudiar (endógena)
        """
        secuencia_temporal = self.dataframe[self.columna_valores]
        serie_objetivo = go.Scatter(x=secuencia_temporal.index, 
                                    y=secuencia_temporal.values, 
                                    name = self.columna_valores, 
                                    line=dict(color='red', width=0.7), 
                                    yaxis='y2')

        titulo_grafico = f"Serie temporal de la columna {self.columna_valores}"
        layout_temp = go.Layout(title=titulo_grafico, 
                                xaxis=dict(title='Referencia temporal'),
                                yaxis=dict(title = self.columna_valores, color='royalblue'))
        fig = go.Figure(data=[serie_objetivo], layout=layout_temp)
        fig.show()

        print("Añade otra columna al gráfico")
        opciones = dict((str(num), columna) for num, columna in enumerate(self.dataframe.columns))
        decision = leer_opciones_pantalla(opciones)
        columna_adyacente = opciones[decision]
        print(columna_adyacente)
        
        serie_adyacente = go.Scatter(x=secuencia_temporal.index, 
                                    y=self.dataframe[columna_adyacente].values, 
                                    name = columna_adyacente, 
                                    line=dict(color='blue', width=0.7), 
                                    yaxis='y')
        
        titulo_grafico = f'Gráfico de {self.columna_valores} y {columna_adyacente}'
        layout_temp = go.Layout(title=titulo_grafico, xaxis=dict(title='Fecha'),
                    yaxis=dict(title=self.columna_valores, color='royalblue', overlaying='y2'),
                    yaxis2=dict(title=columna_adyacente, color='purple', side='right')    )
        
        fig = go.Figure(data=[serie_objetivo, serie_adyacente], layout=layout_temp)
        fig.show()

    # Transformaciones
    def normalizador(self):
        """
        Normaliza los datos preguntando por el algoritmo de normalización más conveniente
        """
        dataframe = self.dataframe
        # Obtener solo las columnas numéricas
        datos_num = dataframe.select_dtypes(include=['int64', 'float64'])
        print(f"Las columnas que se van a normalizar son: {datos_num.columns}")
        print("""Normalizadores disponibles:""")
        opciones = {"1": "min-max scaler",
        "2": "Standard scaler",
        "3": "max- abs scaler",
        "q": "Salir"}
        eleccion = leer_opciones_pantalla(opciones)
        if eleccion == "1":
            scaler = MinMaxScaler()
        elif eleccion == "2":
            scaler = StandardScaler()
        elif eleccion == "3":
            scaler = MaxAbsScaler()
        else:
            print("Los datos no se han normalizado")
        
        normalized_data_array = scaler.fit_transform(datos_num)
        normalized_data = pd.DataFrame(normalized_data_array, columns = datos_num.columns)
        
        #Actualizamos el dataframe original con los datos numericos normalizados
        for columna in normalized_data.columns:
            dataframe[columna] = normalized_data[columna].tolist() 

        # Actualizamos el objeto serie
        self.dataframe_normalizado = dataframe
        return dataframe 

    def plot_boxplots(dataframe):
        # Obtener la lista de columnas del DataFrame
        columns = dataframe.columns

        # Crear una figura y ejes para los boxplots
        fig, axes = plt.subplots(nrows=len(columns), figsize=(12, 6 * len(columns)))

        # Iterar sobre cada columna y crear el boxplot correspondiente
        for i, column in enumerate(columns):
            ax = axes[i]
            ax.boxplot(dataframe[column])
            ax.set_title(f"Boxplot de {column}")
            ax.set_ylabel("Valores")

        # Ajustar el espaciado entre subplots
        plt.tight_layout()

        # Mostrar los boxplots
        plt.show()

    def eliminar_outliers(dataframe):
        # Imprimir la forma (número de filas y columnas) del dataframe original
        print(f'dataframe original: {dataframe.shape}')

        # Crear una lista para almacenar los índices de las filas sin valores atípicos
        filas_filtradas = []

        # Iterar sobre cada fila del DataFrame
        for fila in dataframe.index:
            # Verificar si hay valores atípicos en alguna de las columnas de la fila actual
            if not any(
                (dataframe.loc[fila, columna] < dataframe[columna].quantile(0.25) - 1.5 * (dataframe[columna].quantile(0.75) - dataframe[columna].quantile(0.25))) or
                (dataframe.loc[fila, columna] > dataframe[columna].quantile(0.75) + 1.5 * (dataframe[columna].quantile(0.75) - dataframe[columna].quantile(0.25)))
                for columna in dataframe.columns
            ):
                # Agregar el índice de la fila a la lista de filas filtradas
                filas_filtradas.append(fila)

        # Crear un nuevo DataFrame con las filas filtradas
        dataframe = dataframe.loc[filas_filtradas]

        # Imprimir la forma del dataframe filtrado
        print(f'dataframe filtrado: {dataframe.shape}')

        # Devolver el DataFrame filtrado
        return dataframe

    # Descomponer las series de tiempo en tendencia, estacionalidad y residuos
    def seasonal_decompose_func(dataframe, num_period):
        modelo = int(input("Qué tipo de modelo quieres aplicar? (1/multiplicative, 2/additive): "))
        if modelo == 1:
            model = 'multiplicative'
        elif modelo == 2:
            model = 'additive'
        else:
            print("Opción no válida. Se utilizará el modelo 'additive' por defecto.")
            model = 'additive'
        
        result = seasonal_decompose(dataframe, model=model, period=num_period)
        
        trend = result.trend
        seasonal = result.seasonal
        residual = result.resid
        
        plt.figure(figsize=(10, 8))

        # Componente de tendencia
        plt.subplot(3, 1, 1)
        plt.plot(trend)
        plt.title('Componente de Tendencia')

        # Componente estacional
        plt.subplot(3, 1, 2)
        plt.plot(seasonal)
        plt.title('Componente Estacional')

        # Componente de residuos
        plt.subplot(3, 1, 3)
        plt.plot(residual)
        plt.title('Componente de Residuos')

        plt.tight_layout()
        plt.show()


    def autocor_graficos(self, num_lags):
        """
        Analizar las autocorrelaciones y autocorrelaciones parciales
        Muestra los gráficos
        """
        dataframe = self.dataframe
        columna = self.columna_valores
        for columna in dataframe.columns:
            print(f"ACF y PACF para {columna}:")
            lag_acf = acf(dataframe[columna], nlags=num_lags)
            lag_pacf = pacf(dataframe[columna], nlags=num_lags)

            plt.subplot(121)
            plt.stem(lag_acf)
            plt.title('Función de Autocorrelación')

            plt.subplot(122)
            plt.stem(lag_pacf)
            plt.title('Función de Autocorrelación Parcial')
            plt.show()

    def verifica_index_nan(self):
        """
        Función que verifica si faltan intervalos en el índice temporal
        """
        rango_completo = pd.date_range(
        start = self.dataframe.index.min(),
        end = self.dataframe.index.max(),
        freq = self.dataframe.index.freq)
        
        verificacion = (self.dataframe.index == rango_completo).all()
        if verificacion == True:
            print("No hay valores nulos en el índice")
        else:
            print("Hay valores nulos")
            print(f'Número de filas con missing values en el índice: {self.dataframe.isnull().any(axis=1).sum()}')
        return verificacion
    
    def __getattr__(self, attr):
        # Redirigir el acceso a los atributos al atributo 'dataframe'
        return getattr(self.dataframe, attr)

    def __rellenar_nulos_bool(self, columna):
        columna_sin_nans = self.dataframe[columna].tolist()
        for i in range(len(columna_sin_nans)):
            if columna_sin_nans[i] is None:
                if i > 0 and columna_sin_nans[i-1] is not None and columna[i+1] is not None:
                    if columna_sin_nans[i-1] == columna_sin_nans[i+1]:
                        columna_sin_nans[i] = columna_sin_nans[i-1]
                elif columna_sin_nans[i+1] is not None:
                    columna_sin_nans[i] = columna_sin_nans[i-1]
        self.dataframe[columna] = columna_sin_nans
        return self.dataframe
    
    def __rellena_aislados(self, columna):
        """
        Rellena valores nulos aislados, es decir, que tengan valor no nulo antes y después
        """
        filled_column = self.dataframe[columna].copy()
        # Si el primer valor es nulo, toma el segundo
        if pd.isnull(filled_column[0]):
            filled_column[0] = filled_column[1]
        # Si el último valor es nulo toma el penúltimo
        if pd.isnull(filled_column[-1]):
            filled_column[-1] = filled_column[-2]
        # En los nulos intermedios hace la media
        for i in range(1, len(filled_column) - 1):
            if pd.isnull(filled_column[i]):
                upper_value = filled_column[i - 1]
                lower_value = filled_column[i + 1]
                if pd.notnull(upper_value) and pd.notnull(lower_value):
                    filled_column[i] = (upper_value + lower_value) / 2
        self.dataframe[columna] = filled_column
        return self.dataframe
    
    def __rellena_consecutivos(self, sin_aislados, columna):
        sin_nans = sin_aislados[columna].copy()
        sin_nans = sin_nans.interpolate(method='linear') 
        sin_aislados[columna] = sin_nans
        return sin_aislados

    def completa_nans(self, columna):
        if self.dataframe[columna].dtype == bool:
            nans_bool = self.__rellenar_nulos_bool(columna)
        sin_aislados = self.__rellena_aislados(columna)
        if sin_aislados[columna].isnull().any():
            print("Hay nulos consecutivos")
            sin_nans = self.__rellena_consecutivos(sin_aislados, columna)
        else:
            sin_nans = sin_aislados
        self.dataframe = sin_nans
        return sin_nans
    

    def test_stationarity(dataframe, columna):
        """
        Comprueba la estacionariedad de la serie temporal
        """
        nombre_test = ""
        estacionaria = None
        # Test de Dickey-Fuller augmenté (ADF)
        result = adfuller(dataframe[columna])
        print('Estadística de prueba ADF:', result[0])
        print('Valor p:', result[1])
        print('Valores críticos:', result[4])
        if result[1] < 0.05:
            print('La serie temporal es estacionaria')
            estacionaria = True
            nombre_test = "Dickey-Fuller augmenté (ADF)"

        # Test de KPSS
        if estacionaria == None:
            result = kpss(dataframe[columna])
            print('Estadística de prueba KPSS:', result[0])
            print('Valor p:', result[1])
            print('Valores críticos:', result[3])
            if result[1] < 0.05:
                print('La serie temporal no es estacionaria')
                estacionaria = False
                nombre_test = "KPSS"

        # Test de Phillips Perron
        if estacionaria == None:
            result = pprtest(dataframe[columna])
            print('Estadística de prueba:', result.stat)
            print('Valor p:', result.pvalue)
            print('Valores críticos:')
            for key, value in result.critical_values.items():
                print('\t{}: {}'.format(key, value))
            if result.pvalue < 0.05:
                print('La serie temporal es estacionaria')
                estacionaria = True
                nombre_test = "Phillips Perron"

        # Test de Dickey-Fuller généralisé à moindres carrés (GLS)
        if estacionaria == None:
            dfgls = DFGLS(dataframe[columna], lags=10)
            print('Estadística de prueba:', dfgls.stat)
            print('Valor p:', dfgls.pvalue)
            print('Valores críticos:')
            for key, value in dfgls.critical_values.items():
                print('\t{}: {}'.format(key, value))
            if dfgls.pvalue < 0.05:
                print('La serie temporal es estacionaria')
                estacionaria = True
                nombre_test = "DFGLS"

        valor = "" if estacionaria == True else "no "
        mensaje = f"La serie temporal {valor}es estacionaria según el test de {nombre_test} con valor p= {result[1]}"
        return mensaje
    
        # Separación datos train-val-test

    def separacion_datos (dataframe, fin_train, fin_validacion):
        dataframe_train = dataframe.loc[: fin_train, :]
        dataframe_val   = dataframe.loc[fin_train:fin_validacion, :]
        dataframe_test  = dataframe.loc[fin_validacion:, :]
        
        print(f"Fechas train      : {dataframe_train.index.min()} --- {dataframe_train.index.max()}  (n={len(dataframe_train)})")
        print(f"Fechas validacion : {dataframe_val.index.min()} --- {dataframe_val.index.max()}  (n={len(dataframe_val)})")
        print(f"Fechas test       : {dataframe_test.index.min()} --- {dataframe_test.index.max()}  (n={len(dataframe_test)})")

    def modelo_arima(dataframe, order_pdq):
        for columna in dataframe.columns:
            print(f"Modelo ARIMA para {columna}:")
            p = int(input("¿Cuál es el valor de p?: "))
            d = int(input("¿Cuál es el valor de d?: "))
            q = int(input("¿Cuál es el valor de q?: "))
            order_pdq = [p, d, q]

            modelo = ARIMA(dataframe[columna], order=order_pdq)
            resultado = modelo.fit()
            print(resultado.summary())

            # Gráfico de los datos originales y los valores ajustados
            plt.plot(dataframe[columna])
            plt.plot(resultado.fittedvalues, color='red')
            plt.title(f"Modelo ARIMA para {columna}")
            plt.show()

    def __preguntas_red_neuronal(self):
        self.num_dias_pred = int(input("Ingrese el número de días de predicción: "))
        self.time_step = int(input("Ingrese el número de días históricos para la predicción: "))
        

    def generar_datos_entrenamiento(self):
        self.__preguntas_red_neuronal()
        columna = self.dataframe[self.columna_valores].tolist()
        self.X_train_long_term = []
        self.Y_train_long_term = []
        num_dias_pred = self.num_dias_pred
        time_step = self.time_step
        for j in range(0, num_dias_pred):
            X_train = []
            Y_train = []
            for i in range(0, len(columna) - num_dias_pred - time_step):
                X_train.append(columna[i:i+time_step])
                indice = i + time_step + j
                Y_train.append(columna[indice:indice+1][0])
            self.X_train_long_term.append(X_train)
            self.Y_train_long_term.append(Y_train)
            
        X_train, Y_train = np.array(self.X_train_long_term), np.array(self.Y_train_long_term)
        print(f"Dimensiones de X_train: {X_train.shape[1]} muestras, {X_train.shape[2]} características, {X_train.shape[0]} días de predicción")
        print(f"Dimensiones de Y_train: {Y_train.shape[1]} muestras, {Y_train.shape[0]} días de predicción")

            
        return X_train, Y_train
