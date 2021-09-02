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
        'technique':lt.newList('SINGLE_LINKED')
        # 'dates':lt.newList('SINGLE_LINKED',cmpfunction=compareDates),
        # 'artworksDates':lt.newList('SINGLE_LINKED',cmpfunction=compareArtworkDates)
    }   
    return catalog
# Funciones para agregar informacion al catalogo

def addArtist(catalog,artist):
    lt.addLast(catalog['artists'],artist)
    dates= artist['BeginDate'].split(',')

"""    for date in dates:

        # hola(catalog,date,artist)
        addArtistDate(catalog,date,artist)"""

    # for date in dates:
    #       addArtistDate(catalog,date.strip(),artist)

def addArtwork(catalog,artwork):
    lt.addLast(catalog['artworks'],artwork)
    dates = artwork['DateAcquired'].split(',')

"""    for date in dates:
        addArtworkDate(catalog,date,artwork)
"""



"""def addArtistDate(catalog,date,artist):
    data=catalog['dates']

    posDate=lt.isPresent(data,date)
    if posDate>0:
        fecha=lt.getElement(data,posDate)
    else:
        fecha = newDate(date)
        lt.addLast(data,fecha)
    lt.addLast(fecha['artists'],artist)"""

"""def addArtworkDate(catalog,date,artwork):
    data=catalog['artworksDates']

    posDate = lt.isPresent(data,date)
    if posDate>0:
        fecha=lt.getElement(data,posDate)
    else:
        fecha=newArtworkDate(date)
        lt.addLast(data,fecha)
    lt.addLast(fecha['artworks'],artwork)"""



# def addArtWorks(catalog,Artworks,artw)

# Funciones para creacion de datos

"""def newDate(datee):

    date = {'artistDate': '', "artists": None}
    date['artistDate'] = datee
    date['artists'] = lt.newList('SINGLE_LINKED')
    return date

def newArtworkDate(datee):
    date = {'artworksDate': '', "artworks": None}
    date['artworksDate'] = datee
    date['artworks'] = lt.newList('SINGLE_LINKED')
    return date

# Funciones de consulta
def getCronoArtists(catalog,inicio,fin):
    fechas=catalog['dates']
    resultado=lt.newList()

    for cont in range(inicio,fin):
 
        artists = lt.getElement(fechas,cont)
        lt.addLast(resultado,artists['artists'])


    return resultado"""
# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtists(artist1,artist):
    if(artist1.lower() in artist['DisplayName']):
        return 0
    return -1

"""def compareDates(fecha1,artist):
    if(fecha1 in artist['artistDate']):
        return 0
    return -1"""

"""def compareArtworkDates(fechaArt,artwork):
    if(fechaArt in artwork['artworksDate']):
        return 0
    return -1"""

def compareFechas(fecha1,fecha2):
    return (fecha1['artistDate']<fecha2['artistDate'])
# Funciones de ordenamiento

"""def sortDates(catalog):
    sa.sort(catalog['dates'],compareFechas)"""
