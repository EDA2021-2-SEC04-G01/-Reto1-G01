"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import model
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar artistas cronológicamente en un rango de años")
    print("3- Listar adquisiciones cronológicamente")
    print("4- Clasificar obras de un artista por técnica")
    print("5- Clasificar obras por nacionalidad de sus creadores")
    print("6- Calcular costo de transporte de todas las obras a un departamento")
    print("7- Calcular cantidad de obras para una nueva exposición de acuerdo al periodo de tiempo y el área disponibles")
catalog = None

"""
Funciones para implementar en los requerimientos
"""
def initCatalog():
    
    return controller.initCatalog()

catalog = None
"""
Menu principal 
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        controller.loadData(catalog)
        print('Número de artistas cargados:' + str(lt.size(catalog['artists'])))
        print('Últimos 3 artistas: ') 
        for pos in range(lt.size(catalog['artists'])-2,lt.size(catalog['artists'])+1):
            print(lt.getElement(catalog['artists'],pos))

        print('Número de obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print('Últimas 3 obras: ') 
        for pos in range(lt.size(catalog['artworks'])-2,lt.size(catalog['artworks'])+1):
            print(lt.getElement(catalog['artworks'],pos))
        
        
        


    elif int(inputs[0]) == 2:
        anio_inicio=int(input("Escriba el año de inicio: "))
        anio_fin=int(input("Escriba el año final: "))
        cosa=(model.cronoArtist(catalog,anio_inicio,anio_fin))
        print(cosa)





    elif int(inputs[0]) == 3:
        fechaInicial=input("Introduzca la fecha inicial (AAAA-MM-DD): ")
        fechaFinal=str(input("Introduzca la fecha final (AAAA-MM-DD): "))

        cosa = model.cronoArtwork(catalog,fechaInicial,fechaFinal)
        print(cosa)

    elif int(inputs[0]) == 4:
        artista = input("Escriba el nombre del artista: ")

    elif int(inputs[0]) == 5:
        listaFinal= lt.newList()
        
        listadoNacionalidad=model.ordenNacionalidad(catalog)
        nacionalidadesFull=catalog['nationalities']
        nationMajor=(lt.getElement(nacionalidadesFull,1))['artworks']
        catArtists=catalog['artists']

        for position in range(lt.size(nationMajor)):
            actual = lt.getElement(nationMajor,position)
            title = (actual['Title'])
            artists = []


            idArtist = actual['ConstituentID'][1:len(actual['ConstituentID'])-1].split(',')
            for AutID in idArtist:
                AutID=AutID.strip()
                artistPos = lt.isPresent(catArtists,AutID)
                if artistPos == 0:
                    continue
                artist = (lt.getElement(catalog['artists'],artistPos))['DisplayName']
                artists.append(artist)

            date = actual['Date']
            medium = actual['Medium']
            dimensions = actual['Dimensions']

            actual = {
                'Title' : title,
                'artist(s)':artists,
                'Date':date,
                'Medium':medium,
                'Dimensions':dimensions
            }

            print(actual)
            #lt.addLast(listaFinal,actual)

       # print(listaFinal)


    elif int(inputs[0]) == 6:
        dpto=input("Escriba el departamento del museo: ")


    elif int(inputs[0]) == 7:
        inicio=int(input("Escriba el año inicial: "))
        fin=int(input("Escriba el año final: "))
        area= int(input("Escriba el área disponible en m\u00b2: "))


    else:
        sys.exit(0)
sys.exit(0)
