'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json(r"C:\Users\Ares\Cursada Lab 1\PP_STARWARS\PP_STARWARS\data.json")
    funciones.sanitizar_datos(lista_personajes,"height")
    funciones.sanitizar_datos(lista_personajes,"mass")
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            variable=funciones.quick_sort(lista_personajes,"height")
            funciones.mostrar(variable,"height")
        elif(respuesta=="2"):
            funciones.opcion2(lista_personajes)
        elif(respuesta=="3"):
            variable=funciones.quick_sort(lista_personajes,"mass")
            funciones.mostrar(variable,"mass")
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")
        elif(respuesta=="5"):
            ans=input("que opcion?")
            if ans=="1":
                funciones.exportar_csv(funciones.mostrar(variable,"height"))
            elif ans=="2":
                funciones.exportar_csv(funciones.mostrar(variable,"mass"))
            elif ans=="3":
                funciones.exportar_csv()
            elif ans=="4":
                funciones.exportar_csv()
            
        elif(respuesta=="6"):
            break


starwars_app()

