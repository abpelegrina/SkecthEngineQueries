#!/usr/bin/env python
import requests
import pandas as pd
import time
import datetime

# Datos de acceso
USERNAME = '[USERNAME]'
API_KEY = '[API-KEY]'

# Corpus en el que vamos a realizar las consultas
corpus = '[CORPUS NAME]'

# URL para las consultas ¡¡¡No modificar!!!
base_url = 'https://api.sketchengine.eu/bonito/run.cgi'
q = 'view'
url = base_url + '/' + q + '?corpname=' + corpus

# Tiempo en segundos que hay que esperar entre consultas para no agotar la cuota diaria
# ¡¡CAMBIAR SI VE VAN A HACER MUCHAS CONSULTAS!! Seguir esta guía:
#   - if you want to make fewer than 50 requests, time_to_sleep = 0
#   - if you want to make up to 900 requests, time_to_sleep = 4
#   - if you want to make more than 2000 requests, time_to_sleep = 44
time_to_sleep = 4

# Ficheros de origen y destino, puede ser el mismo
file = '[SOURCE FILE]'
file_res = '[DEST FILE]'

# Función que realiza la consuta a SKE
def getFrequency(query):

    # Imprimimos por pantalla la consulta
    print(query)
    
    # Información a enviar a SKE
    data = {
     'format': 'json',
     # Eliminar ", 'D'" si no se quiere usar el parámtro filter_hits
     'q': ['q'+query,'D'],
     'async': 0
    }
    
    # Imprimimos el tiempo en el que se realiza la consulta
    print(datetime.datetime.now().time())
    
    # Realizamos la consulta
    response = requests.get(url, params=data, auth=(USERNAME, API_KEY))
    
    # Si la consulta a SKE se ha realizado con éxito
    if response:
            # Obtenemos el tiempo de consulta
            elapsed = response.elapsed.total_seconds()
            
            # guardamos el resultado que nos ha
            d = response.json()
            
            # Si la consulta ha durado menos que el tiempo de espera entre consultas "dormimos" la diferencia
            if elapsed < time_to_sleep:
                time.sleep(time_to_sleep-elapsed)
                
            # Devolvemos sólo el parámetro que contiene la frecuencia de la consulta
            return d['fullsize']
            
    # Si se produce algún error devolvemos la consulta para que se mantenga la consulta
    # en la celda
    else:
        print(response.text) # mostramos el error
        print(response.headers) # mostramos el error
        return query

# leemos el fichero de origen
df = pd.read_excel(file)

# Empezamos las consultas desde la primera fila
start = 0

# Terminamos con la última fila
end = df.shape[0]

# Recorremos cada fila del fichero
for index in range(start, end):
    # Imprimimos por pantalla el número de la fila
    print('Row Number : ', index)
    
    # Para cada celda de la fila (excluyendo las tres primeras que tienen sólo los términos)
    # calculamos la frecuencia de la consulta y la guardamos
    df.iloc[index, 3:] = df.iloc[index, 3:].apply(lambda x: getFrequency(x))
    
    # Guardamos los cambios en el fichero
    df.to_excel(file_res, index=False)





