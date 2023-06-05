def rellenar_nulos_bool(columna):
    for i in range(len(columna)):
        if columna[i] is None:
            if i > 0 and columna[i-1] is not None and columna[i+1] is not None:
                if columna[i-1] == columna[i+1]:
                    columna[i] = columna[i-1]
            elif columna[i+1] is not None:
                columna[i] = columna[i+1]
    return columna
