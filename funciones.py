import json
import re 
"---------------------------------------------------------------------"
def cargar_json(texto:str):
    '''
        Extrae un archivo de texto.
        Devuelve una lista.
    '''
    with open(texto,"r") as file:
        diccio=json.load(file)
    return diccio["results"]
"---------------------------------------------------------------------"
lista_personajes=cargar_json(r"C:\Users\Ares\Cursada Lab 1\PP_STARWARS\PP_STARWARS\data.json")
"---------------------------------------------------------------------"
def exportar_csv(data:str):
    '''
    Crea un archivo de texto.
    '''
    with open("data","r") as archivo:
        archivo.write(data)
    
"---------------------------------------------------------------------"


"---------------------------------------------------------------------"
def quick_sort(lista:list,key:str)->list:
    '''
    recibe una lista y una llave.
    itera la lista ordenando de mayor a menor tomando como criterio el valor de la lalve.
    devueve una lista
    '''
    lista_copia= lista[:]
    lista_izq = []
    lista_der = []
    if (len(lista) <= 1):
        return lista
    else:
        pivot = lista_copia [0]
        for e in lista_copia[1:]:
            if e[key]<pivot[key]:
                lista_izq.append(e)
            else:              
                lista_der.append(e)
    
    lista_izq = quick_sort(lista_izq,key)
    
    lista_der = quick_sort(lista_der,key)
    lista_izq.append(pivot)
     
    return lista_izq + lista_der


"---------------------------------------------------------------------"
def mostrar(lista:list,dato:str):
    '''
    recibe una lista y un dato.
    itera e imprime un string con el nombre tipo de dato y dato
    '''
    for e in lista:
        print("Nombre: {0} || Dato {1}: {2} ".format(e["name"],dato,e[dato]))
"---------------------------------------------------------------------"
def sanitizar_datos(lista:list,key:str):
    '''
    recibe una lista y una llave 
    itera la lista y convierte los datos de la llave a entero.

    '''
    for e in lista:
        e[key]=int(e[key])
    return "datos sanitizados"
"---------------------------------------------------------------------"

def calcula_al_mas_alto(lista:list)->str:
    '''
    recibe una lista
    itera la lista calcula el maximo de altura
    devuelve un string
    '''
    maximo=lista[0]
    for e in lista:
        if maximo["height"]<e["height"]:
            maximo=e
    retorno = (maximo["name"])
    return retorno
def calcula_la_mas_alta(lista:list)->str:
    '''
    recibe una lista.
    itera la lista recibida y calcula la atura maxima
    devuelve un string
    '''
    maxima=lista[0]
    for e in lista:
        if maxima["height"]<e["height"]:
            maximo=e
    retorno=(maximo["name"])
    return retorno


def opcion2(lista:list):
    '''
    recibe una lista
    Itera la lista y usa funciones para clacular maximos de altura
    devuelve un string 
    '''
    lista_boys=[]
    lista_girsl=[]
    lista_nb=[]
    for e in lista:
        if e["gender"]=="male":
            lista_boys.append(e)
        elif e["gender"]=="female":
            lista_girsl.append(e)
        else:
            lista_nb.append(e)
    retorno="{0} , {1} , {2} ".format(calcula_la_mas_alta(lista_girsl),calcula_al_mas_alto(lista_boys),lista_boys(lista_nb))
    return retorno
