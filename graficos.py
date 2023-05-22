import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(data):
    f, ax = plt.subplots(figsize=(10, 8))
    corr = data.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
                cmap=sns.diverging_palette(220, 10, as_cmap=True), square=True, ax=ax)
    plt.show()

# Ejemplo de uso
data = ...  # Aquí debes proporcionar tus datos
plot_correlation_heatmap(data)
