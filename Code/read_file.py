import csv
def read_F1():
    data_X = []
    data_Y = []
    with open('Datos_Funcion1.csv', newline='') as myFile:
        reader = csv.reader(myFile)
        
        #leemos valores en X
        for column in reader:
            result = column[0].split(";")
            data = result[0]
            data_X.append(data)
            
        #leemos valores en Y
            data2 = result[1]
            data_Y.append(data2)
    data_X = data_X[2:]
    data_Y = data_Y[2:]
    array = [data_X, data_Y]
    return array

def read_F2():
    data_X = []
    data_Y = []
    with open('Datos_Funcion2.csv', newline='') as myFile:
        reader = csv.reader(myFile)
        
        #leemos valores en X
        for column in reader:
            result = column[0].split(";")
            data = result[0]
            data_X.append(data)
            
        #leemos valores en Y
            data2 = result[1]
            data_Y.append(data2)
    data_X = data_X[2:]
    data_Y = data_Y[2:]
    array = [data_X, data_Y]
    return array

def read_F3():
    data_X = []
    data_Y = []
    with open('Datos_Funcion3.csv', newline='') as myFile:
        reader = csv.reader(myFile)
        
        #leemos valores en X
        for column in reader:
            result = column[0].split(";")
            data = result[0]
            data_X.append(data)
            
        #leemos valores en Y
            data2 = result[1]
            data_Y.append(data2)
    data_X = data_X[2:]
    data_Y = data_Y[2:]
    array = [data_X, data_Y]
    return array


def convert_F1():
    new_X = []
    new_Y = []
    array = read_F1()
    array_X = array[0]
    array_Y = array[1]
    
    for column in array_X:
        new_X.append(float(column))
    for column in array_Y:
        new_Y.append(float(column))
    
    new_array = [new_X, new_Y]
    return new_array

def convert_F2():
    new_X = []
    new_Y = []
    array = read_F2()
    array_X = array[0]
    array_Y = array[1]
    
    for column in array_X:
        new_X.append(float(column))
    for column in array_Y:
        new_Y.append(float(column))
    
    new_array = [new_X, new_Y]
    return new_array

def convert_F3():
    new_X = []
    new_Y = []
    array = read_F3()
    array_X = array[0]
    array_Y = array[1]
    
    for column in array_X:
        new_X.append(float(column))
    for column in array_Y:
        new_Y.append(float(column))
    
    new_array = [new_X, new_Y]

    return new_array