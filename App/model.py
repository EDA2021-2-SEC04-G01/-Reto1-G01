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
        'artworks':lt.newList('SINGLE_LINKED',cmpfunction=compareArtworks),
        'artists':lt.newList('SINGLE_LINKED',cmpfunction=compareArtists),
        'technique':lt.newList('SINGLE_LINKED'),
        'nationalities': lt.newList('SINGLE_LINKED',cmpfunction=compareNation)
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




# Funciones para creacion de datos


# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtists(artistid,artist):
    if(artistid.lower() in artist['ConstituentID']):
        return 0
    return -1

def compareArtworks(artwork1,artwork):
    artId= artwork['ConstituentID']
    if (artwork1.lower() in artId.lower()):
        return 0
    return -1



def compareFechas(artist1,artist2):
    return (artist1['BeginDate']<artist2['BeginDate'])
# Funciones de ordenamiento

def sortDates(catalog):
    sa.sort(catalog['artists'],compareFechas)

def compareNation(nation1,nation):
    if(nation1 in nation['nationality']):
        return 0
    return -1

def cronoArtist(catalog, inicio, fin):

    FiltredList=lt.newList()
    for cont in range(lt.size(catalog['artists'])):
        artist=(lt.getElement(catalog['artists'],cont))       
 
        if int(artist["BeginDate"]) in range(inicio,fin+1):
    
            lt.addLast(FiltredList,artist)
        elif int(artist["BeginDate"]) > fin:
            break
    
    if lt.isEmpty(FiltredList):
        return "No hay artistas en el rango indicado"
    else:
        return FiltredList

def ordenNacionalidad(catalog):
    listado=[]
    artists = catalog['artists']
    for cont in range(lt.size(catalog['artworks'])+1):
   
        artwork = lt.getElement(catalog['artworks'],cont)
        idArtist = artwork['ConstituentID'][1:len(artwork['ConstituentID'])-1].split(',')

        for id in idArtist:
            id=id.strip()
            pos = lt.isPresent(artists,id)
            
            if pos==0:
                continue

            artist = lt.getElement(artists,pos)
            nation = artist['Nationality']

            addNation(catalog,nation,artwork)

    sortNation(catalog['nationalities'])
    
    for pos in range(lt.size(catalog['nationalities'])):
        nacionalidad=(lt.getElement(catalog['nationalities'],pos)['nationality'])
        if nacionalidad not in listado:
            listado.append(nacionalidad)

    return listado


def newNation(nationality):
    nation = {'nationality':nationality,'artworks':lt.newList('SINGLE_LINKED',compareArtworks)}
    return nation

def compareQuantity(nation1,nation2):
    return lt.size(nation1['artworks'])>lt.size(nation2['artworks'])

def sortNation(nationality):
    sa.sort(nationality,compareQuantity)


def addNation(catalog,nation_original,artwork):

    if nation_original=="":
        nation_original="Nationality unknown"
    added=[]
    nationalities = catalog['nationalities']
    posnation = lt.isPresent(nationalities, nation_original)
    if posnation > 0:
        nation = lt.getElement(nationalities, posnation)

    else:
        nation = newNation(nation_original)
        lt.addLast(nationalities, nation)
    
        
    if artwork['ObjectID'] not in added:
        # print(artwork['ObjectID'])
        lt.addLast(nation['artworks'], artwork)
        added.append(artwork['ObjectID'])
