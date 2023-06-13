from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
import pandas as pd
from xgboost import XGBClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

def comparar_modelos(datos, target_column):
    y = datos[target_column]
    X = datos.drop(target_column, axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    models = [
        DecisionTreeClassifier(random_state=0),
        RandomForestClassifier(random_state=0),
        KNeighborsClassifier(),
        SVC(random_state=0),
        LogisticRegression(random_state=0),
        XGBClassifier(),
        AdaBoostClassifier(),
        GradientBoostingClassifier(),
    ]
    models_comparison = {}

    for model in models:
        print(f"Modelo: {str(model)}\n")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracies = cross_val_score(estimator=model, X=X_train, y=y_train, cv=5)
        print(classification_report(y_test, y_pred))
        print("-" * 30, "\n")
        models_comparison[f"{str(model)}"] = [
            accuracy_score(y_pred, y_test),
            f1_score(y_pred, y_test, average="macro"),
            precision_score(y_pred, y_test, average="macro"),
            recall_score(y_pred, y_test, average="macro"),
            (accuracies.mean()),
        ]

    return models_comparison
