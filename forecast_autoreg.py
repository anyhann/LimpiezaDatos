
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.preprocessing import StandardScaler

def crear_entrenar_ForecasterAutoreg(self, datos, tipo_regresor, num_lags,fin_validacion, columna_objetivo):
    forecaster = ForecasterAutoreg()
    tipo_regresor= input("indique el tipo de regresor (R: Ridge/ L: Lasso)")
    if tipo_regresor== "R":
        from sklearn.linear_model import Ridge
    if tipo_regresor== "L":
        from sklearn.linear_model import Lasso
    regressor     = tipo_regresor,
    lags          = num_lags,
    transformer_y = StandardScaler()
    forecaster.fit(y=datos.loc[:fin_validacion, columna_objetivo])
    forecaster