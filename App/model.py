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
import math as m
import textwrap
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as insert
from DISClib.Algorithms.Sorting import quicksort as qsort
from DISClib.Algorithms.Sorting import mergesort as msort
assert cf
from tabulate import tabulate
import textwrap 
import time
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
"""
IMPORTANTE:
Puede que haya algunas diferencias con los resultados mostrados en el ejemplo, sin embargo es
debido a que se usaron array list, lo que hace que funcione diferente el ordenamiento. Las cantidades, sin embargo son las mismas.
"""
# Construccion de modelos

def newCatalog(tipo_lista):
    catalog = {
        'artworks':lt.newList(tipo_lista),
        'artists':lt.newList(tipo_lista,cmpfunction=compareArtists),
        'technique':lt.newList(tipo_lista),
        'nationalities': lt.newList(tipo_lista,cmpfunction=compareNation)
    }   
    return catalog
# Funciones para agregar informacion al  catalogo


def addArtist(catalog,artist):
    lt.addLast(catalog['artists'],artist)



def addArtwork(catalog,artwork):
    lt.addLast(catalog['artworks'],artwork)
    


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

def sortArtworksDates(catalog,cant,method):

    list_sort=lt.subList(catalog['artworks'],1,cant)
    start_time = time.process_time()
    eval(method).sort(list_sort,compareArtDates)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return (list_sort,elapsed_time_mseg)

def sortArtSize(catalog):
    sa.sort(catalog['artists'],compareSize)

def compareSize(art1,art2):
    if art1['Height (cm)']!=None and art1['Height (cm)']!='' and art1['Width (cm)']!=None and art1['Width (cm)']!='':
        if art2['Height (cm)']!=None and art2['Height (cm)']!='' and art2['Width (cm)']!=None and art2['Width (cm)']!='':
            if float(art1['Height (cm)'])+float(art1['Width (cm)']) <  float(art2['Height (cm)'])+float(art2['Width (cm)']):
                return 0
            return -1
        return -1
    return -1   
def compareNation(nation1,nation):
    if(nation1 == nation['nationality']):
        return 0
    return -1

def cronoArtist(catalog, inicio, fin):

    FiltredList=lt.newList()
    for artist in lt.iterator(catalog['artists']):
        
        if int(artist["BeginDate"]) in range(inicio,fin+1):
    
            lt.addLast(FiltredList,artist)
        elif int(artist["BeginDate"]) > fin:
            break
    
    if lt.isEmpty(FiltredList):

        return "No hay artistas en el rango indicado"
    else:
        artistCant = lt.size(FiltredList)
        lstArtist=[]
        for position in range(1,4):
            selectArtist(position,FiltredList,lstArtist,catalog)
        for position in range(lt.size(FiltredList)-2,lt.size(FiltredList)+1):
            selectArtist(position,FiltredList,lstArtist,catalog)
        headers = ['ConstituentID','DisplayName','BeginDate','Nationality','Gender','ArtistBio','Wiki QID','ULAN']
        tabla = tabulate(lstArtist,headers=headers,tablefmt='grid')
    return (tabla,artistCant)


def cronoArtwork(catalog,sublista, inicio, fin):
    purchasedCant=0
    inicio=int(inicio.replace('-',''))
    fin=int(fin.replace('-',''))
    artists = catalog['artists']
    artistList=lt.newList()
    FiltredList=lt.newList()
    for artwork in lt.iterator(sublista):
        #RECORRER EL RANGO MEJOR, LUEGO USAR ISPRESENT. ASÍ SE EVITA RECORRER TOODA LA LISTA.
        # SE COMIENZA A BUSCAR DESDE EL PRIMER NÚMERO DEL RANGO. HAY MENOR COMPLEJIDAD.   
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
                        if lt.isPresent(artistList,artist)==0: lt.addLast(artistList,artist)
                     
                
                lt.addLast(FiltredList,artwork)
                
                if ('purchase' in artwork['CreditLine'].lower()):
                    purchasedCant+=1
#           Aquí hacemos que el ciclo se rompa porque ya está ordenado, así que es mejor detener el ciclo si se sabe que no hay más después        
        # elif int((artwork['DateAcquired'].replace('-','')).strip()) > fin: 
        #     break   
    
    if lt.isEmpty(FiltredList):
        return "No hay obras de arte en el rango indicado"
    else:

        cantArtists = lt.size(artistList)
        listReturn = []
        for position in range(1,4):
            selectInfo(position,FiltredList,listReturn,catalog)

        for position in range(lt.size(FiltredList)-2,lt.size(FiltredList)+1):
            selectInfo(position,FiltredList,listReturn,catalog)
        headers = ['ObjectID','Title','Artist(s)','Medium','Dimensions','Date','Department','Classification','URL']
        tabla = tabulate(listReturn,headers=headers,tablefmt='grid',numalign='center')
        return (tabla,lt.size(FiltredList),purchasedCant,cantArtists)

def ordenNacionalidad(catalog):
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

def nationArworks(catalog):
#       Aquí inicio declarando las variables con las que voy a trabajar, obteniendo del catálogo lo que 
#       se necesita y demás.        
        listCant = []
        listArtworksEnd=[]
        ordenNacionalidad(catalog)
        nacionalidadesFull=catalog['nationalities']
        nationMajor=(lt.getElement(nacionalidadesFull,1))['artworks'] #Tomo la posición 1 porque del model ya sale ordenado de mayor a menor.

#       Este ciclo se encarga de recorrer todos los elementos de la nacionalidad con mayor cantidad de obras.        
        for position in range(1,4):
            selectInfo(position,nationMajor,listArtworksEnd,catalog)

        for position in range(lt.size(nacionalidadesFull)-3,lt.size(nacionalidadesFull)):
            selectInfo(position,nationMajor,listArtworksEnd,catalog)
            
#       Se hacen los headers, para ponerlos en la tabla
        headers = ['ObjectID','Title','Artist(s)','Medium','Dimensions','Date','Department','Classification','URL']
#       Se crea la tabla pasándole como parámetro la lista grande, los headers creados al final y format grid para que se vea más como una tabla.
        tabla=(tabulate(listArtworksEnd, headers=headers, tablefmt='grid',numalign='center'))

        for position in range(1,11):
            nation = lt.getElement(nacionalidadesFull,position)
            size = lt.size(nation['artworks'])
            listCant.append([nation['nationality'],size])

        completeNationMajor = lt.getElement(nacionalidadesFull,1)
        tablaCant = tabulate(listCant,headers=['Nationality','Artworks'],tablefmt='grid',numalign='right')
        return (tablaCant,tabla,completeNationMajor['nationality'],lt.size(completeNationMajor['artworks']))


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

def newExpo(artworks,begin,end,area):
   # artworks = catalog['artworks']
    actual_area=0
    list_artworks=lt.newList()
    for artwork in lt.iterator(artworks):
        fecha=artwork['Date']
        if fecha!='' and fecha!=None:
            if int(fecha) in range(begin,end+1):
                if artwork['Department']=='Drawings & Prints' or artwork['Department']=='Photography':
                    if artwork['Height (cm)']!=None and artwork['Height (cm)']!='' and artwork['Width (cm)']!=None and artwork['Width (cm)']!='':
                        a_sumar=((float(artwork['Height (cm)'])/100)*(float(artwork['Width (cm)'])/100))  
                        if actual_area+a_sumar<=area:
                            actual_area+=a_sumar
                            lt.addLast(list_artworks,artwork)
                        else:
                            break
    return (lt.size(list_artworks),actual_area)


# Req 5

def check_none(artwork,clave):
    if artwork[clave]!='' and artwork[clave]!=None:
        return float(artwork[clave])/100
    else:
        return 0
def cambiar_uno(variable):
    if variable==0:
        return 1
    else:
        return variable
def precioTransporte(catalog,department):
    artworks = catalog['artworks']
    obTransporte = lt.newList()
    precio = 0
    estimado_peso=0
    for artwork in lt.iterator(artworks):
        dep = artwork['Department']
        rad=0
        if department.lower() == dep.lower():
            op1=0
            op2=0
            op3=0
            lt.addLast(obTransporte,artwork)
            no_ceros=0
            circ = check_none(artwork,'Circumference (cm)')
            diam = check_none(artwork,'Diameter (cm)')
            prof =  check_none(artwork,'Depth (cm)')
            height =  check_none(artwork,'Height (cm)')
            leng =  check_none(artwork,'Length (cm)')
            width =  check_none(artwork,'Width (cm)')
            peso=0
            if artwork['Weight (kg)']!='' and artwork['Weight (kg)']!=None: 
                peso =  float(artwork['Weight (kg)'])
                estimado_peso+=peso

            lista = [prof,height,leng,width]
            for dato in lista:
                if dato!=0:
                    no_ceros+=1
            if no_ceros>=2 or circ!=0 or peso!=0:
                
                prof = cambiar_uno(prof)
                height = cambiar_uno(height)
                leng = cambiar_uno(leng)
                width = cambiar_uno(width)
                if circ!=0:
                    rad = circ/2*m.pi
                elif diam!=0:
                    rad = diam/2
                    
                if rad != 0:
                    op1 = m.pow(rad,2)*m.pi*height*72

                else:
                    op2 = prof*height*leng*width*72

                op3 = peso*72
                actual_precio = max([op1,op2,op3])
                precio += actual_precio
            else:
                precio+=48
                
    return (lt.size(obTransporte),round(estimado_peso,3),round(precio,3))

def distribuir(elemento,cantidad):
    str_distribuido = '\n'.join((textwrap.wrap(elemento,cantidad)))
    return str_distribuido


def selectArtist(position,ArtistList,lstArtistEnd,catalog):
    artist = lt.getElement(ArtistList,position)
    ConstID = artist['ConstituentID']
    name=distribuir(artist['DisplayName'],15)
    bgndate=artist['BeginDate']
    nationality=artist['Nationality']
    gender=artist['Gender']
    bio=artist['ArtistBio']
    qid=artist['Wiki QID']
    ulan = artist['ULAN']

    if qid == None or qid == '': qid='Unknown'
    if ulan == None or ulan == '': ulan='Unknown'
    if nationality == None or nationality == '': nationality='Unknown'
    if gender == None or gender == '': gender='Unknown'
    if bgndate == None or bgndate == '': bgndate='Unknown'
    if bio == None or bio == '': bio='Unknown'

    artistInfo=[ConstID,name,bgndate,nationality,gender,bio,qid,ulan]
    lstArtistEnd.append(artistInfo)

def selectInfo(position,ListArtworks,FiltredList,catalog):
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
        FiltredList.append(artwork)