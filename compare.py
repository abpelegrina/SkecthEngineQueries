#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Nombre de los ficheros a comparar
file1 = '<FICHERO 1 -> SIN FILTRAR>'
file2 = '<FICHERO 2 -> FILTRAR>'

# Nombre del fichero en el que guardar los resultados
file_res = '<FICHERO DONDE GUARDAR EL RESULTADO>'

# Cargamos los ficheros
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Restamos los datos del segundo fichero a los del primero, quitando las
# tres primeras celdas de cada fila que contienen texto
d2 = df1.iloc[:, 3:].sub(df2.iloc[:, 3:])

# Guardamos la diferencia en un fichero
d2.to_excel(file_res, index=False)

print('Diferencias calculadas con éxito')


