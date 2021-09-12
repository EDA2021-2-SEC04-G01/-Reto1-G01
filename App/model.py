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

import textwrap
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
        'artworks':lt.newList('ARRAY_LIST'),
        'artists':lt.newList('ARRAY_LIST',cmpfunction=compareArtists),
        'technique':lt.newList('ARRAY_LIST'),
        'nationalities': lt.newList('ARRAY_LIST',cmpfunction=compareNation)
    }   
    return catalog
# Funciones para agregar informacion al catalogo


def addArtist(catalog,artist):
    lt.addLast(catalog['artists'],artist)
    dates= artist['BeginDate'].split(',')


def addArtwork(catalog,artwork):
    lt.addLast(catalog['artworks'],artwork)
    dates = artwork['DateAcquired'].split(',')


# Funciones para creacion de datos


# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtists(artistid,artist):
    if(str(artistid) == str(artist['ConstituentID'])):
        return 0
    return -1

def compareArtworks(artwork1,artwork):
    if (str(artwork1) == str(artwork['ObjectID'])):
        return 0
    return -1



def compareFechas(artist1,artist2):
    return (artist1['BeginDate']<artist2['BeginDate'])

def compareArtDates(art1,art2):
    return (art1['DateAcquired']<art2['DateAcquired'])

# Funciones de ordenamiento

def sortDates(catalog):
    sa.sort(catalog['artists'],compareFechas)

def sortArtworksDates(catalog):
    sa.sort(catalog['artworks'],compareArtDates)

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


def cronoArtwork(catalog, inicio, fin):
    purchasedCant=0
    inicio=int(inicio.replace('-',''))
    fin=int(fin.replace('-',''))
    artists = catalog['artists']
    artistList=[]
    FiltredList=lt.newList()
    for artwork in lt.iterator(catalog['artworks']):
           
        if artwork["DateAcquired"] != '':
            if int(artwork["DateAcquired"].replace('-','')) in range(inicio,fin+1):

#               Esto de aquí es para sacar los artistas únicos y luego contarlos, al final.
                idArtist = artwork['ConstituentID'].replace('[','').replace(']','').split(',')
        
                for id in idArtist:
                    id=id.strip()
                    pos = lt.isPresent(artists,id)
                    
                    if pos!=0:
                        artist =(lt.getElement(artists,pos))['DisplayName']
                        #En esta linea nos aseguramos de que no hayan artistas repetidos
                        if artist not in artistList: artistList.append(artist)
                     
                
                lt.addLast(FiltredList,artwork)
                
                if ('purchase' in artwork['CreditLine'].lower()):
                    purchasedCant+=1
#           Aquí hacemos que el ciclo se rompa porque ya está ordenado, así que es mejor detener el ciclo si se sabe que no hay más después        
            elif int(artwork["DateAcquired"].replace('-','')) > fin: 
                break
    
    if lt.isEmpty(FiltredList):
        return "No hay obras de arte en el rango indicado"
    else:
        return (FiltredList,purchasedCant,len(artistList))        


def ordenNacionalidad(catalog):
    listado=[]
    artists = catalog['artists']
    for artwork in lt.iterator(catalog['artworks']):
        
        idArtist = artwork['ConstituentID'].replace('[','').replace(']','').split(',')
        
        for id in idArtist:

            id=id.strip()

            pos = lt.isPresent(artists,id)
            artist = lt.getElement(artists,pos)
            nation = artist['Nationality']

            addNation(catalog,nation,artwork)
  
    sortNation(catalog['nationalities'])

    for nacionalidad in lt.iterator(catalog['nationalities']):

        if nacionalidad not in listado:
            listado.append(nacionalidad)

    return listado


def newNation(nationality):
    nation = {'nationality':nationality,'artworks':lt.newList('ARRAY_LIST',compareArtworks)}
    return nation

def compareQuantity(nation1,nation2):
    return lt.size(nation1['artworks'])>lt.size(nation2['artworks'])

def sortNation(nationality):
    sa.sort(nationality,compareQuantity)


def addNation(catalog,nation_original,artwork):
    if nation_original=="":
        nation_original="Nationality unknown"

    posnation = lt.isPresent(catalog['nationalities'], nation_original)
    if posnation > 0:
        nation = lt.getElement(catalog['nationalities'], posnation)

    else:
        nation = newNation(nation_original)
        lt.addLast(catalog['nationalities'], nation)
  
    lt.addLast(nation['artworks'], artwork)

    
