# a,b = 100, 0
# try:
#     print(a/b)
# except (ZeroDivisionError, TypeError , SyntaxError): # solo está capturando un error
#     print("División por Cero")
# else:
#     print("esto está dentro de else")
# finally:
#     print("esto está dentro de finally")


a = input ("Ingrese su edad: ")
    
try:
    int(a)
    print("Esta bien ingresado")
except (TypeError, ValueError):
    print("no es un número")