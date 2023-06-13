
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.preprocessing import StandardScaler

def crear_entrenar_ForecasterAutoreg(datos, num_lags, fin_validacion, columna_objetivo):
    """
    Crea y entrena un forecaster.
    num_lags
    fin_validacion
    columna_objetivo
    """
    tipo_regresor= input("indique el tipo de regresor (R: Ridge/ L: Lasso)")
    if tipo_regresor== "R":
        from sklearn.linear_model import Ridge
        regresor = Ridge()
    if tipo_regresor== "L":
        from sklearn.linear_model import Lasso
        regresor = Lasso()
    forecaster = ForecasterAutoreg(
        regressor     = regresor,
        lags          = num_lags,
        transformer_y = StandardScaler())
    forecaster.fit(y=datos.loc[:fin_validacion, columna_objetivo])
    forecaster

if __name__ == "__main__":
    from Serie_temporal import SerieTemporal
    from carga_datos import cargador
    import os

    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "opsd_germany_daily.csv"))
    datos= datos.iloc[2193:,:]
    datos.drop("Wind+Solar", axis=1, inplace=True)
    print(datos.head(10))
    print(datos.tail(10))
    serie = SerieTemporal(datos, "Date", "Consumption")
    serie.descripcion()
