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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {
        'artworks':lt.newList('SINGLE_LINKED',cmpfunction=None),
        'artists':lt.newList('SINGLE_LINKED',cmpfunction=compareArtists),
        'dates':lt.newList('SINGLE_LINKED'),
        'artworksDates':lt.newList('SINGLE_LINKED')
    }   
    return catalog
# Funciones para agregar informacion al catalogo

def addArtist(catalog,artist):
    lt.addLast(catalog['artists'],artist)

    dates= artist['BeginDate'].split(',')

    for date in dates:
         addArtistDate(catalog,date.strip(),artist)

def addArtwork(catalog,artwork):
    lt.addLast(catalog['artworks'],artwork)


def addArtistDate(catalog, Artistdate,artist):
    dates=catalog['dates']
    posDate=lt.isPresent(dates, Artistdate)

    if posDate>0:
        date = lt.getElement(dates,posDate)
    else:
        date = newDate(Artistdate)
        lt.addLast(dates,date)
    lt.addLast(date['artist'],artist)

# def addArtWorks(catalog,Artworks,artw)

# Funciones para creacion de datos

def newArtist(artistName):
    artist = {'name': "", "dates": None}
    artist['name'] = artistName
    return artist


def newDate(date):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    date = {'date': None, "artist": None,  "artwork": None}
    date['name'] = date
    date['artist'] = lt.newList('SINGLE_LINKED')
    date['artwork'] = lt.newList('SINGLE_LINKED')
    return date
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def compareArtists(artist1,artist):
    if(artist1.lower() in artist['DisplayName']):
        return 0
    return -1

# Funciones de ordenamiento