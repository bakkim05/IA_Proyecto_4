import time
from random import randint
from read_file import convert_F1,convert_F2,convert_F3

#Funcion de población inicial
def pobl_ini(poblacion):
    i = 0
    j = 0
    for i in range(100):
        individuo = []
        for j in range(7):
            individuo.append(randint(-10, 10))
        poblacion.append(individuo)
        j=0

#Funcion para leer el archivo de datos
def leer_csv(option):
    if option==1:
        datos = convert_F1()
    elif option==2:
        datos = convert_F2()
    elif option==3:
        datos = convert_F3()
    return datos


#Funcion para evaluar los datos en las funciones 
def eval_datos(dat, pobl):
    y = pobl[0]* dat[0]**6 + pobl[1]* dat[0]**5 + pobl[2]* dat[0]**4 + pobl[3]* dat[0]**3 + pobl[4]* dat[0]**2 +pobl[5]* dat[0] + pobl[6]
    err = (abs(y - dat[1])/dat[1])*500
    return err


#Funcion para escoger los miembros mas aptos de la poblacion (50% del total)
def selec_indi(cantidad, poblacion, errores):
    mejores_indi = []
    mejores_err = []

    temporal = errores[0]
    posicion = 0

    i = 0
    j = 0

    while i < cantidad:
        temporal = errores[0]
        posicion = 0
        for j in range(len(poblacion)):
            if errores[j] < temporal:
                temporal = errores[j]
                posicion = j
        mejores_indi.append(poblacion.pop(posicion))
        mejores_err.append(errores.pop(posicion))
        i += 1
    
    return mejores_indi, mejores_err


#Funcion para realizar el cruce de los individuos
def cruce(x,y):

    padres, madres = padres_madres(x, y)

    padre = []
    madre = []
    hijo1 = []
    hijo2 = []
    hijos = []

    if len(padres) != len(madres):
        "No hay misma cantidad de padres y madres"
    
    n = len(padres)

    for i in range(n):
        padre = padres.pop(0)
        madre = madres.pop(0)

        for j in range(len(padre)):
            if (j % 2) == 0:
                hijo1.append(padre[j])
                hijo2.append(madre[j])
                if j != 6:
                    hijo1.append(madre[j+1])
                    hijo2.append(padre[j+1])
              
        mutacion = randint(1,20)
        if mutacion > 5 and mutacion < 10:
            lugar = randint(0,6)
            hijo1[lugar] = hijo1[lugar]*-1
            hijo2[lugar] = hijo2[lugar]*2

            hijos.append(hijo1)
            hijo1 = []
            hijos.append(hijo2)
            hijo2 = []
        else:
            hijos.append(hijo1)
            hijo1 = []
            hijos.append(hijo2)
            hijo2 = []
        
    return hijos

#Funcion para separar la población en padres y madres
def padres_madres(pobla, errs):
    mejores1 = []
    mejores2 = []

    n = len(pobla)

    cont = 1

    for i in range(n):
        if (cont % 2) ==  1:
            ind = pos(errs)
            mejores1.append(pobla.pop(ind))
            errs.pop(ind)
            cont += 1
        elif (cont % 2) == 0:
            ind = pos(errs)
            mejores2.append(pobla.pop(ind))
            errs.pop(ind)
            cont += 1
    
    return mejores1, mejores2

#Función para encontrar la posicion del elemento menor en una lista
def pos(lista):
    temp = lista[0]
    sub = 0
    
    for i in range(len(lista)):
        if lista[i] < temp:
            temp = lista[i]
            sub = i    
    return sub




def main():
    timeout = time.time() + 60*5   # 5 minutos desde ahora
    #timeout = time.time() + 10   # 10 segundos desde ahora

    poblacion = []

    poblacion_anterior = []

    gen = 0
    
    #funcion para cargar los datos del excel    
    option = 1

    datos = leer_csv(option)

    errores_generales = []
    err_cinco = []
    err_gen = []

    generaciones = [[],[]]

    #llamar función poblacion inicial (crea arrelgo de arreglos)
    pobl_ini(poblacion)

    
    # Ciclo de ejecucion principal
    while True:
        error = 0   
        if time.time() > timeout: #or poblacion==poblacion_anterior:
            print("Terminado", poblacion[0], err_gen[0])
            break

        #llamar funcion para evaluar datos del excel
        i = 0
        j = 0
        errores_generales = []
        err_cinco = []
        err_gen = []
        for i in range(len(poblacion)):
            for j in range(len(datos)):
                error += eval_datos([datos[0][j], datos[1][j]], poblacion[i])
            error = error/(len(datos[0]))
            errores_generales.append(error)
        
        poblacion_anterior = list(poblacion)

        #llamar funcion para escoger 50% mejor
        cinco, err_cinco = selec_indi(5, list(poblacion), list(errores_generales))

        poblacion, err_gen = selec_indi(len(poblacion)/2, list(poblacion), list(errores_generales))

        #llamar funcion para cruzar
        poblacion += cruce(list(poblacion), list(err_gen))

        gen += 1
        

        print("Termina generacion ", gen)
        if len(generaciones[0]) == 20:
            generaciones[0].pop(0)
            generaciones[1].pop(0)
            generaciones[0].append(cinco)
            generaciones[1].append(err_cinco)
        else:
            generaciones[0].append(cinco)
            generaciones[1].append(err_cinco)

        
main()