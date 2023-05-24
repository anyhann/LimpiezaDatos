from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def calcular_R2_regresion(X, y):

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)

    return r2


def calcular_R2_regresion_multiple(X, y):
    X_train, X_train, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo.fit(X_train, y_train)
    