#!/usr/bin/env python

# Paquetes a importar
import requests
import pandas as pd


# Datos de acceso
USERNAME = '[USER NAME]'
API_KEY = '[API KEY]'

# Corpus en el que vamos a realizar las consultas
corpus = '[CORPUS NAME]'

# URL para las consultas ¡¡¡No modificar!!!
base_url = 'https://api.sketchengine.eu/bonito/run.cgi'
q = 'view'
url = base_url + '/' + q + '?corpname=' + corpus

# Consulta a realizar
query = '[tag!="JJ.*|N.*"][lemma="offshore"][lemma="farm"][tag!="N.*|JJ.*"] within <s/>'

# Imprimimos por pantalla la consulta
print('Ejecutando la consulta... ' + query)

# Información a enviar a SKE
data = {
 'format': 'json',
 'q': ['q'+query,'D'], # Si no quieres el parámetro
 'async': 0
}

# Realizamos la consulta
response = requests.get(url, params=data, auth=(USERNAME, API_KEY))

# Si la petición a la API ha funcionado correctamente
if response:
    # guardamos el resultado que nos ha
    d = response.json()
    
    # Mostramos el resultado por pantalla. Esto se puede borrar para que se muestre
    # solo la frecuencia
    print('Resultado de la consulta:')
    print(d)

    # Devolvemos sólo el parámetro que contiene la frecuencia de la consulta
    print('\nFrecuencia de la consulta {' + query + '}: ')
    print(d['fullsize'])

# Si se produce algún error lo mostramos
else:
    print(response.text)
    print(response.headers)







