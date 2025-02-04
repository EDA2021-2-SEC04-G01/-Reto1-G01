﻿"""
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
import time
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

"""
IMPORTANTE:
Puede que haya algunas diferencias con los resultados mostrados en el ejemplo, sin embargo es
debido a que se usaron array list, lo que hace que funcione diferente el ordenamiento. Las cantidades, sin embargo son las mismas.
"""

#TODO ¿mover la creación de la tabla para aquí?

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
def initCatalog(tipo_lista):
    
    return controller.initCatalog(tipo_lista)

catalog = None
"""
Menu principal 
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
#Carga de datos
    if int(inputs[0]) == 1:
        a=True
        while a==True:
            tipo_lista=int(input("Seleccione el tipo de lista que quiere usar.\n1. ARRAY_LIST \n2. para LINKED_LIST: \n"))
            if tipo_lista==1: 
                tipo_lista='ARRAY_LIST'
                a=False
            elif tipo_lista==2: 
                tipo_lista = 'SINGLE_LINKED'
                a=False
            else:
                 print("por favor escriba información válida")
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo_lista)
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
        
        start_time = time.process_time()
        inicio=int(input("Escriba el año de inicio: "))
        fin=int(input("Escriba el año final: "))
        print("================= Req No. 1 Inputs ==================")
        print("\nArtist born between {} and {}.\n".format(inicio,fin))
        resultados= controller.cronoArtist(catalog,inicio,fin)
        if  "No hay" in resultados :
            print(resultados+"\n")
            break
        tabla=resultados[0]
        cantArtists = resultados[1]
        print("================= Req No. 1 Answer ==================\n")
        print("There are {0} artist born between {1} and {2}\n\n".format(cantArtists,inicio,fin))
        print("The first and last 3 artists in range are...\n")
        print(tabla)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)

##Requerimiento 2
    elif int(inputs[0]) == 3:
        start_time = time.process_time()
        inicio=(input("Escriba la fecha de inicio: "))
        fin=(input("Escriba la fecha final: "))
        activo = True
        while activo:
            opcion=int(input(("Seleccione el método de ordenamiento: \n1. insertion\n2. shellsort\n3. quicksort\n4. merge: \n")))
            if opcion ==1: 
                method='insert'
                activo = False
            elif opcion ==2:
                 method = 'sa'
                 activo = False
            elif opcion ==3: 
                method = 'qsort'
                activo = False
            elif opcion == 4:
                 method = 'msort'
                 activo = False
            else: print("Por favor seleccione una opción válida. \n")
        
        activoSize=True
        while activoSize:
            size=int(input(("Escriba el número del tamaño de la sublista, escriba 0 si quiere la lista completa: ")))
            if size==0:
                subsize=lt.size(catalog['artworks'])
                activoSize=False
            elif size<=lt.size(catalog['artworks']):
                subsize=size
                activoSize=False
            else:
                "Por favor inserte un número válido"
        
        tiempo = controller.cronoArtworks(catalog,inicio,fin,subsize,method)[1]
        resultado = controller.cronoArtworks(catalog,inicio,fin,subsize,method)[0]
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
        print("El tiempo gastado fue {}".format(tiempo))

        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("El tiempo usado completo fue"+str(elapsed_time_mseg))

#Requerimiento 3
    elif int(inputs[0]) == 4:
        start_time = time.process_time()
        artista = input("Escriba el nombre del artista: ")
        ReturnModel=controller.artworkPorTecnica(artista, catalog)
        if type(ReturnModel) is dict:            
            print('Para el artista '+str(artista)+' hay:\n'+ '-' + str(ReturnModel['TotalObras'])+'\n'+ '-Con las siguientes tecnicas'+str(ReturnModel['Tecnicas'])+'\n'+ '-La tecnica más utilizada es ' +str(ReturnModel['Tecnica mayor'])+'\n'+'-Las obras con la tecnica más utilizada son: '+str(ReturnModel['ObrasMayor']))
        elif type(ReturnModel) is str:
            print(ReturnModel)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
    


#Requerimiento 4
    elif int(inputs[0]) == 5:
        start_time = time.process_time()
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
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
        
  

#Requrimiento 5
    elif int(inputs[0]) == 6:
        start_time = time.process_time()
        dpto=input("Escriba el departamento del museo: ")
        print("\n=================Req No. 5 Inputs ====================\n ")
        print("Estimate the cost to transport all artifacts in {} MoMA's Departament . . .\n".format(dpto))
        rta=controller.precioTransporte(catalog,dpto)
        print("================ Req No. 5 Answer ================\n")
        print("The MoMA is going to transport {0} artifacts from the {1} department. ".format(rta[0],dpto))
        print("REMEMBER!, NOT all MoMA's data is complete! ! !... These are estimates.  ")
        print("Estimated cargo weight (kg): "+str(rta[1]))
        print("Estimated cargo cost (USD): "+str(rta[2]))
        print("\nThe TOP 5 most expensive items to transport are:")
        print(controller.precioTransporte(catalog,dpto)[3])
        print("\nThe TOP 5 oldest items to tranport are: ")
        print(controller.precioTransporte(catalog,dpto)[4])
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
#Requirimiento 6
    elif int(inputs[0]) == 7:
        start_time = time.process_time()
        inicio=int(input("Escriba el año inicial: "))
        fin=int(input("Escriba el año final: "))
        area= float(input("Escriba el área disponible en m\u00b2: "))
        print("\n=================Req No. 6 (BONUS) Inputs ====================\n ")
        print("Searching artworks between {0} to {1}".format(inicio,fin))
        print("With an available area of:{} m\u00b2 \n".format(area))
        #Se ordena la lista por fecha de adquisición. 
        lista=(controller.sortArtDates(catalog,lt.size(catalog['artworks']),'msort'))[0]
        rta=controller.newExpo(lista,inicio,fin,area,catalog)
        print("================ Req No. 6 (BONUS) Answer ================\n")
        print("The MoMA is going to exhibit pieces from {0} to {1}".format(inicio,fin)) 
        print("There are {} possible items in an available area of: {} m\u00b2".format(rta[0],area))
        print("The possible exhibit has {} items.".format(rta[1]))
        print("Filling {0} m\u00b2 of the {1} m\u00b2 available.".format(rta[2],area))
        print("The first and last 3 objects in the American artwork list are: \n")
        print(rta[3])

        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)        



    else:
        sys.exit(0)
sys.exit(0)
