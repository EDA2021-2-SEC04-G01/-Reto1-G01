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
from time import sleep as s
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
#Carga de datos
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

        
        

#Requerimiento 1
    elif int(inputs[0]) == 2:
        anio_inicio=int(input("Escriba el año de inicio: "))
        anio_fin=int(input("Escriba el año final: "))
        cosa=(model.cronoArtist(catalog,anio_inicio,anio_fin))
        
        
        if lt.size(cosa)>=3:
            
            print('Primeros 3 artistas: ')
            for pos in range(3):
                print((lt.getElement(cosa,pos))['DisplayName'])

            print('Últimos 3 artistas: ')
            for pos in range(lt.size(cosa)-3,lt.size(cosa)):
                print((lt.getElement(cosa,pos))['DisplayName'])
        else:
            print('Primeros y últimos 1 o 2 artistas: ')
            for pos in range(lt.size(cosa)):
                print((lt.getElement(cosa,pos))['DisplayName'])

        
        
        #print(cosa)




##Requerimiento 2
    elif int(inputs[0]) == 3:
        inicio=(input("Escriba el año de inicio: "))
        fin=(input("Escriba el año final: "))

        resultado = controller.cronoArtworks(catalog,inicio,fin)
        tabla = resultado[0]
        cantObras = resultado[1]
        cantCompradas = resultado[2]
        cantArtists = resultado[3]
        print("=================== Req No. 2 Inputs =====================\n")
        print("Artworks acquired between {0} and {1}".format(inicio,fin))
        print("=================== Req No. 2 Answer =====================\n\n")
        print("The MoMA acquired {0} unique pieces between {1} and {2}\n".format(str(cantObras),inicio,fin))
        print("With {0} different artists and purchased {1} of them.\n\nThe first and last 3 artworks in the range are... ".format(cantArtists,cantCompradas))
        print(tabla)

#Requerimiento 3
    elif int(inputs[0]) == 4:
        artista = input("Escriba el nombre del artista: ")


#Requerimiento 4
    elif int(inputs[0]) == 5:
        print("=================Req No. 4 Inputs ====================\n ")
        print("Ranking countries by their number of Artworks in the MoMA...\n")
        resultados = controller.nationArworks(catalog)
        print("\n--------------- Req No. 4 Answer -----------------\n")
        print("The TOP 10 Countries in the MoMA are: ")
        topNation=(resultados[0])
        tablaOrden = resultados[1]
        nameMajor = resultados[2]
        cantMajor = resultados[3]
        print(topNation)
        s(2) #### Aquí lo pongo a esperar 2 segundos, únicamente es para que se pueda ver que está pasando con más calma
        print("The TOP nacionality in the museum is: {0} with {1} unique pieces.\nThe first and last 3 objects in the {0} artwork list are: ".format(nameMajor,str(cantMajor)))
        print(tablaOrden)

        
  

#Requrimiento 5
    elif int(inputs[0]) == 6:
        dpto=input("Escriba el departamento del museo: ")

#Requirimiento 6
    elif int(inputs[0]) == 7:
        inicio=int(input("Escriba el año inicial: "))
        fin=int(input("Escriba el año final: "))
        area= int(input("Escriba el área disponible en m\u00b2: "))


    else:
        sys.exit(0)
sys.exit(0)
