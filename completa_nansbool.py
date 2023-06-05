def rellenar_nulos_bool(self, columna):
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