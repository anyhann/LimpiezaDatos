from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def calcular_R2_regresion(X, y):

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)

    return r2
