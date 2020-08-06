#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Abrimos el fichero ocn pandas
file1 = '[FILE]'
df1 = pd.read_excel(file1)


# Quitamos las tres primeras celdas de cada fila que contienen texto
d2 = df1.iloc[:, 3:]

# creamos el gráfico de color
plt.pcolor(d2)

# indicamos que se muestre la escala del gráfico
plt.colorbar()

#mostramos el gráfico
plt.show()
