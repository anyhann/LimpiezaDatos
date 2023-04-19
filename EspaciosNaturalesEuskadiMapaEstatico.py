# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:49:58 2023

@author: Usuario
"""

import pandas as pd
import os
import requests
import json
import math
from distancias import geo_dist
from mapquest import coordenadas_mapquest
import folium
from IPython.display import display
import matplotlib.pyplot as plt
from io import BytesIO


def pregunta_ubicacion():
    while True:
        calle = input("Ingrese el nombre de la calle: ")
        poblacion = input("Ingrese el nombre de la población: ")
        provincia = input("Ingrese el nombre de la provincia: ")

        if calle.strip() and poblacion.strip() and provincia.strip():
            break

        print("Por favor, ingrese todos los datos requeridos.")

    return coordenadas_mapquest(calle, poblacion, provincia)


lat_usuario, long_usuario = pregunta_ubicacion()


def carga_playas():
    # carga los datos
    url = "https://opendata.euskadi.eus/contenidos/ds_recursos_turisticos/playas_de_euskadi/opendata/espacios-naturales.geojson"
    json_data = requests.get(url).json()
    marca = []
    coordenadas = []
    poblacion = []
    provincia = []

    for valor in json_data['features']:
        coordenadas.append(valor["geometry"]["coordinates"])
        marca.append(valor["properties"]["marks"])
        poblacion.append(valor["properties"]["municipality"])
        provincia.append(valor["properties"]["territory"])

    datos = {"coordinates": coordenadas, "marks": marca,
             "municipality": poblacion, "territory": provincia}
    dataframe = pd.DataFrame(data=datos)

    dataframe[['longitud', 'latitud']] = pd.DataFrame(
        dataframe['coordinates'].to_list(), columns=['longitud', 'latitud'])
    # Eliminar la columna "coordinates" original
    dataframe.drop('coordinates', axis=1, inplace=True)
    # dataframe.rename(columns={'municipaly': 'Municipio'}, inplace=True)

    return dataframe


espacios_naturales = carga_playas()


def anade_distancia(espacios_naturales, lat_usuario, long_usuario):
    # añade columna distancia en el dataframe
    espacios_naturales['distancia'] = espacios_naturales.apply(lambda row: geo_dist(
        row['latitud'], row['longitud'], lat_usuario, long_usuario), axis=1)
    return espacios_naturales


espacios_naturales = anade_distancia(
    espacios_naturales, lat_usuario, long_usuario)


def selecciona_distancia(espacios_naturales):
    kilometros = int(
        input("Distancia máxima de los espacios naturales en km: "))
    filtrado2 = espacios_naturales[espacios_naturales["distancia"] < kilometros]
    return filtrado2


espacios_cercanos = selecciona_distancia(espacios_naturales)


def imprime_dato(espacios_cercanos):
    for index, row in espacios_cercanos.iterrows():
        print(index, "\t", row["marks"], "\t", row['territory'],
              "\t", row['municipality'], "\t", row['distancia'], "kilometros de distancia")


def mostrar_mapa(espacios_cercanos):
    # Convertir la columna latitud y longitud a tipo numérico
    espacios_cercanos["latitud"] = pd.to_numeric(espacios_cercanos["latitud"])
    espacios_cercanos["longitud"] = pd.to_numeric(
        espacios_cercanos["longitud"])

    centro_lat = (espacios_cercanos["latitud"].max(
    ) + espacios_cercanos["latitud"].min())/2
    centro_long = (espacios_cercanos["longitud"].max(
    ) + espacios_cercanos["longitud"].min())/2

    # Construir la URL de la API de MapQuest
    url = "https://www.mapquestapi.com/staticmap/v5/map?"
    url += f"center={centro_lat},{centro_long}&locations="
    for index, row in espacios_cercanos.iterrows():
        # Agregar la ubicación al parámetro "locations"

        url += f"{row['latitud']},{row['longitud']}||"

    # Agregar los demás parámetros

    url += f"&zoom=13&size400=,400@2x&key=ck2OXUAJsF0iz999XGQ62jyXo8AXOVp7"

    print("URL:", url)  # DEBUGGING

   # Realizar una solicitud HTTP a la API de MapQuest
    response = requests.get(url)
    # print(response.content)

    # Verificar si la respuesta es una imagen válida
    if response.headers['Content-Type'] == 'image/jpeg':
        # Convertir la respuesta a una imagen de mapa
        img = plt.imread(BytesIO(response.content), format='jpg')

        # Mostrar la imagen del mapa en el plot y la consola
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    else:
        print("No se pudo mostrar el mapa.")


mostrar_mapa(espacios_cercanos)
