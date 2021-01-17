from tkinter import Tk, Label, Button, Text
import time
from random import randint
from read_file import convert_F1,convert_F2,convert_F3

class GUI:
    def __init__(self,master):
        self.master = master
        self.state = 0
        self.generation =  [[1, 2, 3, 4, 5, 6, 7],
                            [1, 2, 3, 4, 5, 6, 7],
                            [1, 2, 3, 4, 5, 6, 7],
                            [1, 2, 3, 4, 5, 6, 7],
                            [1, 2, 3, 4, 5, 6, 7]]
        self.last20 = [[],[]]
        self.porcentaje = [100, 90, 80, 70, 60]
        master.title("Proyecto 5")
        master.geometry("550x360")

        #####################################CONTAINTER DIMENSIONS#############################################################

        #Heights
        self.height = 2

        #Tamaño de los Botones
        self.buttonWidth = 14
        self.buttonHeight = self.height

        #Tamaño de los Labels
        self.labelWidth = 8
        self.labelHeight = self.height

        #Tamaño de los Fillers
        self.fillerWidth = 2
        self.fillerHeight = self.height

        #Tamaño del Funcion Label 
        self.funcionWidth = 20
        self.funcionHeight = self.height



        ######################################OBJECTS############################################################################

        #Funcion Label
        self.labelFuncion = Label(master, width = self.funcionWidth, height = self.funcionHeight)

        #Buttons
        self.button1 = Button(master, text = "Función 1", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.funcion1_pressed())
        self.button2 = Button(master, text = "Función 2", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.funcion2_pressed())
        self.button3 = Button(master, text = "Función 3", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.funcion3_pressed())

        #Labels
        self.labelx0 = Label(master, text = "x_0", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx1 = Label(master, text = "x_1", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx2 = Label(master, text = "x_2", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx3 = Label(master, text = "x_3", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx4 = Label(master, text = "x_4", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx5 = Label(master, text = "x_5", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx6 = Label(master, text = "x_6", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        
        self.porcentajeLabel = Label(master, text= "Porcentaje", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.porcentaje0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.porcentaje1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.porcentaje2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.porcentaje3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.porcentaje4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)


        self.labelv0b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        self.labelv0b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        self.labelv0b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        self.labelv0b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        self.labelv0b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        #Playback buttons
        self.startButton = Button(master, text = "COMENZAR", background = "red", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.comenzar())
        self.genText = Text(master, background = "white", width = self.buttonWidth, height = self.buttonHeight)
        self.searchButton = Button(master, text = "BUSCAR", background = "white", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.buscar())
        self.bestButton = Button(master, text = "MEJOR", background = "yellow", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.mejor())

        #Filler
        self.filler0 = Label(master, width = self.fillerWidth, height = self.fillerHeight)


        #################################DISPLAY###########################################################################

        #Display Buttons
        self.labelFuncion.grid(row = 0, column = 0)
        self.button1.grid(row = 1, column = 0)
        self.button2.grid(row = 2, column = 0)
        self.button3.grid(row = 3, column = 0)

        #Playback
        self.startButton.grid(row = 4, column = 0)

        self.genText.grid(row = 6, column = 0)
        self.searchButton.grid(row = 7, column = 0)
        self.bestButton.grid(row = 8, column = 0)


        #Display Filler
        self.filler0.grid(row = 1, column = 1)

        #Display Labels
        self.labelx0.grid(row = 1, column = 2)
        self.labelx1.grid(row = 2, column = 2)
        self.labelx2.grid(row = 3, column = 2)
        self.labelx3.grid(row = 4, column = 2)
        self.labelx4.grid(row = 5, column = 2)
        self.labelx5.grid(row = 6, column = 2)
        self.labelx6.grid(row = 7, column = 2)

        self.porcentajeLabel.grid(row = 8, column = 2)
        self.porcentaje0.grid(row = 8, column = 3)
        self.porcentaje1.grid(row = 8, column = 4)
        self.porcentaje2.grid(row = 8, column = 5)
        self.porcentaje3.grid(row = 8, column = 6)
        self.porcentaje4.grid(row = 8, column = 7)

        self.labelv0b0.grid(row = 1, column = 3)
        self.labelv1b0.grid(row = 2, column = 3)
        self.labelv2b0.grid(row = 3, column = 3)
        self.labelv3b0.grid(row = 4, column = 3)
        self.labelv4b0.grid(row = 5, column = 3)
        self.labelv5b0.grid(row = 6, column = 3)
        self.labelv6b0.grid(row = 7, column = 3)

        self.labelv0b1.grid(row = 1, column = 4)
        self.labelv1b1.grid(row = 2, column = 4)
        self.labelv2b1.grid(row = 3, column = 4)
        self.labelv3b1.grid(row = 4, column = 4)
        self.labelv4b1.grid(row = 5, column = 4)
        self.labelv5b1.grid(row = 6, column = 4)
        self.labelv6b1.grid(row = 7, column = 4)

        self.labelv0b2.grid(row = 1, column = 5)
        self.labelv1b2.grid(row = 2, column = 5)
        self.labelv2b2.grid(row = 3, column = 5)
        self.labelv3b2.grid(row = 4, column = 5)
        self.labelv4b2.grid(row = 5, column = 5)
        self.labelv5b2.grid(row = 6, column = 5)
        self.labelv6b2.grid(row = 7, column = 5)
        
        self.labelv0b3.grid(row = 1, column = 6)
        self.labelv1b3.grid(row = 2, column = 6)
        self.labelv2b3.grid(row = 3, column = 6)
        self.labelv3b3.grid(row = 4, column = 6)
        self.labelv4b3.grid(row = 5, column = 6)
        self.labelv5b3.grid(row = 6, column = 6)
        self.labelv6b3.grid(row = 7, column = 6)

        self.labelv0b4.grid(row = 1, column = 7)
        self.labelv1b4.grid(row = 2, column = 7)
        self.labelv2b4.grid(row = 3, column = 7)
        self.labelv3b4.grid(row = 4, column = 7)
        self.labelv4b4.grid(row = 5, column = 7)
        self.labelv5b4.grid(row = 6, column = 7)
        self.labelv6b4.grid(row = 7, column = 7)


    #############################FUNTIONS#######################################################

    def funcion1_pressed(self):
        self.state = 1
        self.labelFuncion["text"] = "Función 1 selecionado"
        return

    def funcion2_pressed(self):
        self.labelFuncion["text"] = "Función 2 selecionado"
        self.state = 2
        return

    def funcion3_pressed(self):
        self.labelFuncion["text"] = "Función 3 selecionado"
        self.state = 3
        return




    def buscar(self):
        if (self.genText.get("1.0", "end-1c") == ""):
            return

        if (int(self.genText.get("1.0", "end-1c")) < 0):
            return

        if (int(self.genText.get("1.0", "end-1c")) >= 20):
            return

        generacion = int(self.genText.get("1.0", "end-1c"))

        #Insertar funcion de buscar generacion utilizando var [generacion]

        self.labelv0b0["background"] = "white"
        self.labelv1b0["background"] = "white"
        self.labelv2b0["background"] = "white"
        self.labelv3b0["background"] = "white"
        self.labelv4b0["background"] = "white"
        self.labelv5b0["background"] = "white"
        self.labelv6b0["background"] = "white"
        self.porcentaje0["background"] = "white"

        self.labelv0b0["text"] = str(self.last20[0][generacion][0][0])
        self.labelv1b0["text"] = str(self.last20[0][generacion][0][1])
        self.labelv2b0["text"] = str(self.last20[0][generacion][0][2])
        self.labelv3b0["text"] = str(self.last20[0][generacion][0][3])
        self.labelv4b0["text"] = str(self.last20[0][generacion][0][4])
        self.labelv5b0["text"] = str(self.last20[0][generacion][0][5])
        self.labelv6b0["text"] = str(self.last20[0][generacion][0][6])

        self.labelv0b1["text"] = str(self.last20[0][generacion][1][0])
        self.labelv1b1["text"] = str(self.last20[0][generacion][1][1])
        self.labelv2b1["text"] = str(self.last20[0][generacion][1][2])
        self.labelv3b1["text"] = str(self.last20[0][generacion][1][3])
        self.labelv4b1["text"] = str(self.last20[0][generacion][1][4])
        self.labelv5b1["text"] = str(self.last20[0][generacion][1][5])
        self.labelv6b1["text"] = str(self.last20[0][generacion][1][6])

        self.labelv0b2["text"] = str(self.last20[0][generacion][2][0])
        self.labelv1b2["text"] = str(self.last20[0][generacion][2][1])
        self.labelv2b2["text"] = str(self.last20[0][generacion][2][2])
        self.labelv3b2["text"] = str(self.last20[0][generacion][2][3])
        self.labelv4b2["text"] = str(self.last20[0][generacion][2][4])
        self.labelv5b2["text"] = str(self.last20[0][generacion][2][5])
        self.labelv6b2["text"] = str(self.last20[0][generacion][2][6])

        self.labelv0b3["text"] = str(self.last20[0][generacion][3][0])
        self.labelv1b3["text"] = str(self.last20[0][generacion][3][1])
        self.labelv2b3["text"] = str(self.last20[0][generacion][3][2])
        self.labelv3b3["text"] = str(self.last20[0][generacion][3][3])
        self.labelv4b3["text"] = str(self.last20[0][generacion][3][4])
        self.labelv5b3["text"] = str(self.last20[0][generacion][3][5])
        self.labelv6b3["text"] = str(self.last20[0][generacion][3][6])

        self.labelv0b4["text"] = str(self.last20[0][generacion][4][0])
        self.labelv1b4["text"] = str(self.last20[0][generacion][4][1])
        self.labelv2b4["text"] = str(self.last20[0][generacion][4][2])
        self.labelv3b4["text"] = str(self.last20[0][generacion][4][3])
        self.labelv4b4["text"] = str(self.last20[0][generacion][4][4])
        self.labelv5b4["text"] = str(self.last20[0][generacion][4][5])
        self.labelv6b4["text"] = str(self.last20[0][generacion][4][6])

        self.porcentaje0["text"] = str(self.last20[1][generacion][0])
        self.porcentaje1["text"] = str(self.last20[1][generacion][1])
        self.porcentaje2["text"] = str(self.last20[1][generacion][2])
        self.porcentaje3["text"] = str(self.last20[1][generacion][3])
        self.porcentaje4["text"] = str(self.last20[1][generacion][4])

        return
    
    def mejor(self):

        #Insertar funcion de buscar generacion

        self.labelv0b0["background"] = "yellow"
        self.labelv1b0["background"] = "yellow"
        self.labelv2b0["background"] = "yellow"
        self.labelv3b0["background"] = "yellow"
        self.labelv4b0["background"] = "yellow"
        self.labelv5b0["background"] = "yellow"
        self.labelv6b0["background"] = "yellow"
        self.porcentaje0["background"] = "yellow"

        self.labelv0b1["text"] = ""
        self.labelv1b1["text"] = ""
        self.labelv2b1["text"] = ""
        self.labelv3b1["text"] = ""
        self.labelv4b1["text"] = ""
        self.labelv5b1["text"] = ""
        self.labelv6b1["text"] = ""

        self.labelv0b2["text"] = ""
        self.labelv1b2["text"] = ""
        self.labelv2b2["text"] = ""
        self.labelv3b2["text"] = ""
        self.labelv4b2["text"] = ""
        self.labelv5b2["text"] = ""
        self.labelv6b2["text"] = ""

        self.labelv0b3["text"] = ""
        self.labelv1b3["text"] = ""
        self.labelv2b3["text"] = ""
        self.labelv3b3["text"] = ""
        self.labelv4b3["text"] = ""
        self.labelv5b3["text"] = ""
        self.labelv6b3["text"] = ""

        self.labelv0b4["text"] = ""
        self.labelv1b4["text"] = ""
        self.labelv2b4["text"] = ""
        self.labelv3b4["text"] = ""
        self.labelv4b4["text"] = ""
        self.labelv5b4["text"] = ""
        self.labelv6b4["text"] = ""

        self.porcentaje1["text"] = ""
        self.porcentaje2["text"] = ""
        self.porcentaje3["text"] = ""
        self.porcentaje4["text"] = ""

        self.labelv0b0["text"] = str(self.generation[0][0])
        self.labelv1b0["text"] = str(self.generation[0][1])
        self.labelv2b0["text"] = str(self.generation[0][2])
        self.labelv3b0["text"] = str(self.generation[0][3])
        self.labelv4b0["text"] = str(self.generation[0][4])
        self.labelv5b0["text"] = str(self.generation[0][5])
        self.labelv6b0["text"] = str(self.generation[0][6])
        self.porcentaje0["text"] = str(self.porcentaje[0])

        return

    #Funcion de poblacion inicial
    def pobl_ini(self, poblacion):
        i = 0
        j = 0
        for i in range(100):
            individuo = []
            for j in range(7):
                individuo.append(randint(-10, 10))
            poblacion.append(individuo)
            j=0

    #Funcion para leer el archivo de datos
    def leer_csv(self):
        if self.state == 1:
            datos = convert_F1()
        elif self.state == 2:
            datos = convert_F2()
        elif self.state == 3:
            datos = convert_F3()
        return datos

    #Funcion para evaluar los datos en las funciones 
    def eval_datos(self, dat, pobl):
        y = pobl[0]* dat[0]**6 + pobl[1]* dat[0]**5 + pobl[2]* dat[0]**4 + pobl[3]* dat[0]**3 + pobl[4]* dat[0]**2 +pobl[5]* dat[0] + pobl[6]
        err = (abs(y - dat[1])/dat[1])*500
        return err


    #Funcion para escoger los miembros mas aptos de la poblacion (50% del total)
    def selec_indi(slef, cantidad, poblacion, errores):
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
    def cruce(self,x,y):

        padres, madres = self.padres_madres(x, y)

        padre = []
        madre = []
        hijo1 = []
        hijo2 = []
        hijos = []

        if len(padres) != len(madres):
            print("No hay misma cantidad de padres y madres")
        
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
    def padres_madres(self, pobla, errs):
        mejores1 = []
        mejores2 = []

        n = len(pobla)

        cont = 1

        for i in range(n):
            if (cont % 2) ==  1:
                ind = self.pos(errs)
                mejores1.append(pobla.pop(ind))
                errs.pop(ind)
                cont += 1
            elif (cont % 2) == 0:
                ind = self.pos(errs)
                mejores2.append(pobla.pop(ind))
                errs.pop(ind)
                cont += 1
        
        return mejores1, mejores2

    #Función para encontrar la posicion del elemento menor en una lista
    def pos(self, lista):
        temp = lista[0]
        sub = 0
        
        for i in range(len(lista)):
            if lista[i] < temp:
                temp = lista[i]
                sub = i    
        return sub

    def comenzar(self):
        if (self.state == 0):
            return 

        #timeout = time.time() + 60*5   # 5 minutos desde ahora
        timeout = time.time() + 2   # 10 segundos desde ahora

        poblacion = []

        poblacion_anterior = []

        gen = 0
        
        #funcion para cargar los datos del excel    
        option = 1

        datos = self.leer_csv()

        errores_generales = []
        err_cinco = []
        err_gen = []
        
        self.last20 = [[],[]]

        #llamar función poblacion inicial (crea arrelgo de arreglos)
        self.pobl_ini(poblacion)

        
        # Ciclo de ejecucion principal
        while True:
            error = 0   
            if gen > 21: #time.time() > timeout: #or poblacion==poblacion_anterior:
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
                    error += self.eval_datos([datos[0][j], datos[1][j]], poblacion[i])
                error = error/(len(datos[0]))
                errores_generales.append(round(error,3))
            
            poblacion_anterior = list(poblacion)

            #llamar funcion para escoger 50% mejor
            self.generation, self.porcentaje = self.selec_indi(5, list(poblacion), list(errores_generales))

            poblacion, err_gen = self.selec_indi(len(poblacion)/2, list(poblacion), list(errores_generales))

            #llamar funcion para cruzar
            poblacion += self.cruce(list(poblacion), list(err_gen))

            gen += 1
            

            print("Termina generacion ", gen)
            if len(self.last20[0]) == 20:
                self.last20[0].pop(0)
                self.last20[1].pop(0)
                self.last20[0].append(self.generation)
                self.last20[1].append(self.porcentaje)
                
            else:
                self.last20[0].append(self.generation)
                self.last20[1].append(self.porcentaje)
        
        return


if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()
    