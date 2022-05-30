
# funcion que sume dos números

# a = 89
# b = 65

# print(F"La Suma es {a+b}")


# def adicion (numero1,numero2):    # tienes dos paramentros
#     """ESTA ES LA DOCUMENTACION:
#         Esta función suma dos números solo enteros"""
#     num3=numero1+numero2
#     print("La suma es:" +str(num3))
#     return



'''separar un string ingresado por teclado'''

# var1= input("Ingrese un texto: ")  #tiene un solo parametro
def separar (string1):
    '''Separar string de un arreglo en lista'''
    list1 = list()
    for i in string1:
        list1.append(i)
    return list1
# resultado = separar(var1)
# print(resultado)



# funcion que permita dividir dos números

def dvd (param1, param2=1):   # así se puede agreagar con unargumento por defecto
    '''Separar string de un arreglo en lista'''
    if param2 == 0:
        print("División por cero")
        return
    else:
        return param1/param2



#que muestre en pantalla cada uno de los elementos de esa lista

def mostrarlst(*list1): #para argumentos variables, no se separaan - los vuelve multiples
    ''''#que muestre en pantalla cada uno de los elementos de esa lista'''
    for i in list1:
        print(i)
    return