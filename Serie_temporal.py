import pandas as pd
from statsmodels.tsa.stattools import acf, pacf
from matplotlib import pyplot as plt
from carga_serie_temporal import auto_conversion_datetime
from descripciones import descripcion
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MaxAbsScaler
from captura_opciones import leer_opciones_pantalla
from statsmodels.tsa.stattools import adfuller, kpss
from arch.unitroot import PhillipsPerron as pprtest
from arch.unitroot import DFGLS
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA

class SerieTemporal:
    def __init__(self, dataframe, columna_temporal, columna_valores):
        self.dataframe = self.conversion_a_serie_temp(dataframe, columna_temporal)
        self.columna_valores = columna_valores
        # Normalizar los datos numéricos
        # self.dataframe["Valores_norm"] = self.dataframe[self.columna_valores]
        
    # Visualizar las series de tiempo en graficos separados
    def visualizar_serie(dataframe):
        dataframe.plot(subplots=True, figsize=(10, 6))
        plt.show()

        
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
        self.dataframe = dataframe
        return dataframe 

    def conversion_a_serie_temp(self, dataframe, columna):
        # Convertir la columna de texto a datetime
        dataframe[columna] = auto_conversion_datetime(dataframe[columna])
        dataframe.set_index(columna, inplace=True)
        dataframe = dataframe.asfreq(dataframe.index[1]-dataframe.index[0])
        print("La frecuencia de la serie temporal es:", dataframe.index.freq)
        dataframe = dataframe.sort_index()
        print(f'Número de filas con missing values: {dataframe.isnull().any(axis=1).sum()}')
        return dataframe

    def descripcion(self):
        print(descripcion(self.dataframe))
        print("La frecuencia de la serie temporal es:", self.dataframe.index.freq)
        print(f'Número de filas con missing values: {self.dataframe.isnull().any(axis=1).sum()}')

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
    
    # Analizar las autocorrelaciones y autocorrelaciones parciales
    def autocor_graficos(dataframe, columna, num_lags):
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

        
    def grafica_interactiva(self):
        # Gráfica interactiva
        df = self.dataframe
        data_columns = df.columns
        column_name = data_columns[0]
        data_sequence = df[column_name]
        layout_temp = go.Layout(title='Serie Temporal', xaxis=dict(title='Fecha'),
                                yaxis=dict(title=column_name, 
                                    color='royalblue'))
        fig = go.Figure(data=data_sequence, layout=layout_temp)
        fig.show()
    
    def verifica_nan(self):
        rango_completo = pd.date_range(
        start = self.dataframe.index.min(),
        end = self.dataframe.index.max(),
        freq = self.dataframe.index.freq)
        
        verificacion = (self.dataframe.index == rango_completo).all()
        if verificacion == True:
            print("No hay valores nulos")
        else:
            print("Hay valores nulos")
            print(f'Número de filas con missing values: {self.dataframe.isnull().any(axis=1).sum()}')
        return verificacion
    
    def __getattr__(self, attr):
        # Redirigir el acceso a los atributos al atributo 'dataframe'
        return getattr(self.dataframe, attr)

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

    def test_stationarity(dataframe, columna):
        nombre_test = ""
        estacionaria = None
        # Test de Dickey-Fuller augmenté (ADF)
        result = adfuller(dataframe[columna])
        print('Estadística de prueba ADF:', result[0])
        print('Valor p:', result[1])
        print('Valores críticos:', result[4])
        if result[1] > 0.05:
            print('La serie temporal no es estacionaria')
        else:
            print('La serie temporal es estacionaria')
            estacionaria = True
            nombre_test = "Dickey-Fuller augmenté (ADF)"

        # Test de KPSS
        if estacionaria == None:
            result = kpss(dataframe[columna])
            print('Estadística de prueba KPSS:', result[0])
            print('Valor p:', result[1])
            print('Valores críticos:', result[3])
            if result[1] > 0.05:
                print('La serie temporal no es estacionaria')
            else:
                print('La serie temporal es estacionaria')
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
            if result.pvalue > 0.05:
                print('La serie temporal no es estacionaria')
            else:
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
            if dfgls.pvalue > 0.05:
                print('La serie temporal no es estacionaria')
            else:
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
