"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from DISClib.Algorithms.Sorting.shellsort import sort
import config as cf
import model
import csv

import textwrap 
from tabulate import tabulate
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    loadArtists(catalog)
    loadArtworks(catalog)
    sortDates(catalog)



def loadArtists(catalog):
    artistFile=cf.data_dir+"Artists-utf8-small.csv"
    input_file = csv.DictReader(open(artistFile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog,artist)
        
        

def loadArtworks(catalog):
    artworkFile=cf.data_dir+"Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(artworkFile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog,artwork)


# Funciones de ordenamiento

def sortDates(catalog):
    model.sortDates(catalog)

def cronoArtist(catalog,inicio,fin):
    return model.cronoArtist(catalog,inicio,fin)

def sortArtDates(catalog):
    model.sortArtworksDates(catalog)

# Funciones de consulta sobre el catálogo

"""Esta función es para organizar el tamaño de las casillas de la tabla, 
la declaramos globalmente porque se usa en varias ocasiones
"""
def distribuir(elemento,cantidad):
    str_distribuido = '\n'.join((textwrap.wrap(elemento,cantidad)))
    return str_distribuido


def cronoArtworks(catalog,inicio,fin):
    #Ordenamos aquí y no al inicio con lo demás para no alterar el resultado del requerimiento 4.
    sortArtDates(catalog)
    data = model.cronoArtwork(catalog,inicio,fin)
    listArtworks = data[0] 
    cantPurchased = data[1]
    cantArtists = data[2]
    listReturn = []
    for position in range(1,4):
         selectInfo(position,listArtworks,listReturn,catalog)

    for position in range(lt.size(listArtworks)-3,lt.size(listArtworks)):
        selectInfo(position,listArtworks,listReturn,catalog)
    headers = ['ObjectID','Title','Artist(s)','Medium','Dimensions','Date','Department','Classification','URL']
    tabla = tabulate(listReturn,headers=headers,tablefmt='grid',numalign='center')
    return (tabla,lt.size(listArtworks),cantPurchased,cantArtists)


def nationArworks(catalog):
#       Aquí inicio declarando las variables con las que voy a trabajar, obteniendo del catálogo lo que 
#       se necesita y demás.        
        listCant = []
        listArtworks=[]
        model.ordenNacionalidad(catalog)
        nacionalidadesFull=catalog['nationalities']
        nationMajor=(lt.getElement(nacionalidadesFull,1))['artworks'] #Tomo la posición 1 porque del model ya sale ordenado de mayor a menor.

#       Este ciclo se encarga de recorrer todos los elementos de la nacionalidad con mayor cantidad de obras.        
        for position in range(1,4):
            selectInfo(position,nationMajor,listArtworks,catalog)

        for position in range(lt.size(nacionalidadesFull)-3,lt.size(nacionalidadesFull)):
            selectInfo(position,nationMajor,listArtworks,catalog)
            
#       Se hacen los headers, para ponerlos en la tabla
        headers = ['ObjectID','Title','Artist(s)','Medium','Dimensions','Date','Department','Classification','URL']
#       Se crea la tabla pasándole como parámetro la lista grande, los headers creados al final y format grid para que se vea más como una tabla.
        tabla=(tabulate(listArtworks, headers=headers, tablefmt='grid',numalign='center'))

        for position in range(1,11):
            nation = lt.getElement(nacionalidadesFull,position)
            size = lt.size(nation['artworks'])
            listCant.append([nation['nationality'],size])

        completeNationMajor = lt.getElement(nacionalidadesFull,1)
        tablaCant = tabulate(listCant,headers=['Nationality','Artworks'],tablefmt='grid',numalign='right')
        return (tablaCant,tabla,completeNationMajor['nationality'],lt.size(completeNationMajor['artworks']))

def selectInfo(position,ListArtworks,listArtworks,catalog):
#       ↓↓↓ Todo este montón de líneas se encargan de sacar la info. necesaria del diccionario grande y con textwrap lo separa en líneas de un igual tamaño.
        

        artwork = lt.getElement(ListArtworks,position)

        objectID = artwork['ObjectID']
        title=distribuir(artwork['Title'],10)
        date=distribuir(artwork['Date'],10)
        medium=distribuir(artwork['Medium'],20)
        dimensions=distribuir(artwork['Dimensions'],20)
        department=distribuir(artwork['Department'],15)
        classification=distribuir(artwork['Classification'],15)

        url = artwork['URL'] 
        if url == None or url == '': #esto de acá solo hace que se vuelva Unknown si está vacía la casilla de url
            url ='Unknown'
        url='\n'.join(((textwrap.wrap(url,15))))

#       Aquí se recorren internamente los artistas que tenga cada obra para luego buscarlos en el archivo artists y sacar sus nombres.
        artists = ""
        idArtist = artwork['ConstituentID'].replace('[','').replace(']','').split(',') #Hago lo de artwork['ConstituentID'].replace('[','').replace(']','') para quitarle los corchetes []
        for AuthorID in idArtist: 
            AuthorID=AuthorID.strip() #Strip quita espacios innecesarios
            artistPos = lt.isPresent(catalog['artists'],AuthorID)
            if artistPos != 0: 
                artist = (lt.getElement(catalog['artists'],artistPos))['DisplayName'] 

#           Este if solo es para separar por comas si hay varios artistas, para no iniciar con coma si está vacío.                
            if artists=="":
                artists+=artist
            else:
                artists+=", "+artist
#       Se vuelve a hacer lo de antes para separar con una cantidad exacta de lineas.
        artists=distribuir(artists,15)

#       Se crea una lista con todo lo que pide el requerimiento.
        artwork = [objectID,title,artists,medium,dimensions,date,
                   department,classification,url]
#       Se pone un nuevo registro con la info de cada obra en la lista grande declarada al inicio.
        listArtworks.append(artwork)


