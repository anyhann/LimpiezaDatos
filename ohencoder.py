import numpy as np
import pandas as pd

one_hot_encoded_data = pd.get_dummies(data, columns = ['columna1', 'columna2'])
print(one_hot_encoded_data)