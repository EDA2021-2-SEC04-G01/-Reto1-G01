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
"""def getCronoArtists(catalog,inicio,fin):
    resultado=model.getCronoArtists(catalog,inicio,fin)
    return resultado"""

def nationArworks(catalog):
#       Aquí inicio declarando las variables con las que voy a trabajar, obteniendo del catálogo lo que 
#       se necesita y demás.        
        listRetorno=[]
        nacionalidadesCantidad=[]
        listadoNacionalidad=model.ordenNacionalidad(catalog)
        nacionalidadesFull=catalog['nationalities']
        nationMajor=(lt.getElement(nacionalidadesFull,1))['artworks'] #Tomo la posición 1 porque del model ya sale ordenado de mayor a menor.
        catArtists=catalog['artists']

#       Este ciclo se encarga de recorrer todos los elementos de la nacionalidad con mayor cantidad de obras.        
        for position in range(1,4):

            selectInfo(position,nationMajor,listRetorno,catalog)
        for position in range(lt.size(nacionalidadesFull)-3,lt.size(nacionalidadesFull)):
            selectInfo(position,nationMajor,listRetorno,catalog)
#       Se hacen los headers, para ponerlos en la tabla
        headers = ['Title','Artist(s)','Date','Medium','Dimensions','Department','Classification','URL']
#       Se crea la tabla pasándole como parámetro la lista grande, los headers creados al final y format grid para que se vea más como una tabla.
        tabla=(tabulate(listRetorno, headers=headers, tablefmt='grid',numalign='center'))


        print(lt.size(nationMajor))
        for i in range(1,lt.size(nacionalidadesFull)+1):
            nation = lt.getElement(nacionalidadesFull,i)
            print(nation['nationality'],lt.size(nation['artworks']))

        # for pos in range(1,lt.size(nacionalidadesFull)+1):
        #     nation = lt.getElement(nacionalidadesFull,pos)
        #     tamanioAniadir=[lt.size(nation)]
        #     print(nation,tamanioAniadir)

        # return(listadoNacionalidad,tabla) #Retorna las nacionalidades y la tabla generada al final
        return (listadoNacionalidad,tabla)


def selectInfo(position,nationMajor,listRetorno,catalog):
#       ↓↓↓ Todo este montón de líneas se encargan de sacar la info. necesaria del diccionario grande y con textwrap lo separa en líneas de un igual tamaño.
        
        actual = lt.getElement(nationMajor,position)

        title='\n'.join(((textwrap.wrap(actual['Title'],10))))
        
        date='\n'.join(((textwrap.wrap(actual['Date'],10))))
        
        medium='\n'.join(((textwrap.wrap(actual['Medium'],20))))

        dimensions='\n'.join(((textwrap.wrap(actual['Dimensions'],20))))

        department='\n'.join(((textwrap.wrap(actual['Department'],15))))

        classification='\n'.join(((textwrap.wrap(actual['Classification'],15))))

        url = actual['URL'] 
        if url == None or url == '': #esto de acá solo hace que se vuelva Unknown si está vacía la casilla de url
            url ='Unknown'
        url='\n'.join(((textwrap.wrap(url,15))))

#       ↑ ↑ ↑ Aquí termina lo de arriba ↑ ↑ ↑

#       Aquí se recorren internamente los artistas que tenga cada obra para luego buscarlos en el archivo artists y sacar sus nombres.
        artists = ""
        idArtist = actual['ConstituentID'][1:len(actual['ConstituentID'])-1].split(',') #Hago lo de [1:len(actual['ConstituentID'])-1] para quitarle los corchetes []
        for AutID in idArtist: 
            AutID=AutID.strip() #Strip quita espacios innecesarios
            artistPos = lt.isPresent(catalog['artists'],AutID)
            if artistPos == 0: #Si no encuentra al artista vuelve a iniciar el ciclo y no hace lo de abajo.
                continue
            artist = (lt.getElement(catalog['artists'],artistPos))['DisplayName'] #Como aquí se sabe que lo encontró, busca el nombre.

#           Este if solo es para separar por comas si hay varios artistas, para no iniciar con coma si está vacío.                
            if artists=="":
                artists+=artist
            else:
                artists+=", "+artist
#       Se vuelve a hacer lo de antes para separar con una cantidad exacta de lineas.
        artists='\n'.join(((textwrap.wrap(artists,15))))

#           Se crea una lista con todo lo que pide el requerimiento.
        actual = [
                title,
                artists,
                date,
                medium,
                dimensions,
                department,
                classification,
                url
                ]
#       Se pone un nuevo registro con la info de cada obra en la lista grande declarada al inicio.
        listRetorno.append(actual)