#ejercicios while and for


# control = 0

# while control<=20:
#     print("estructura while", control)
#     control +=1


# variable = 0  # porque isempre empieza en 0
# while variable <= 40:
#     print(f"Este número {variable} es par")
#     variable = variable+2



# while True: # para no limitar con un número
#     resul = input ("Bienvenido, si desea seguir viendo este mensaje \ introduzca cualquiera cosa.Si desea salir  esribe 'NO' " )
#     if resul.lower()=="no":
#         break # break se utiliza através de una condición if


# escribir una applicación qu emuestre lo snúmeros en pantalla del 1 al 10 debe saltarse el num 6
 #  variable=1 # afuera para que no se reemplace
 # while True:  
 #     print ("este número es", num)
 #     variable +=1
 #     if variable ==11:
 #         break
    

# contador =1
# while contador<=10:
#     if contador==6:
#         contador +=1
#         print (contador)
#         contador +=1


# contador= 1
# while contador <=10:
#     if contador==6:
#         contador+=1
#         continue
#     print(contador)
#     contador+=1

#____________________________________________
# for - logica de repetición



# for i in [40, 52, 78, 89, 756]:  # con for podemos controlar las repeticiones
#     print(i)


# for i in "texto-prueba":
#     if i=="-":
#     break
#     print(i)
    
    
   # for i in "texto-prueba":
   #     if i=="o":
   #   continue
   #     print(i)  
  
   
  
    
# for var2 in range (10):  # siquiero tener 10 repeticiones  en el parentesis la cantidad de repeticiones
#     print(var2)
    


# for var2 in range(10,100,5):
#     print(var2)



altura = 12
ancho = 2
for i in range (ancho):  # 2 repeticiones
    for dos in range (altura):  # 12 repeticiones
        print("*",end="")





# string1 = input("Ingrese una frase o palabra")
# if string == string1 [::-1]:
#     print ("La frase es un palíndromo")
#   else:
#     print ("No es un palíndromo")



# edad = int(input ("Ingrese su edad como un número entero"))
# if edad<= 15:
#     print ("es un adolecente")    
# else:
#     if edad > 15 and  edad <25:
#         print("es un adulto jovén")
#     else:
#         print("Es un adulto")


# edad = int(input ("Ingrese su edad como un número entero"))
# if edad<15:
#     print("Es un adolescente")
# elif edad >=15 and edad<25:
#     print("Es un adulto jóven")
# else :
#     print("Es una adulto")



# edad = int(input ("Ingrese su edad como un número entero"))
# if edad<15:
#     print("Es un adolescente")
# elif edad >25:
#     print("Es un adulto")
# else :
#     print("Es una jovén adulto")

# edad = int(input ("Ingrese su edad como un número entero"))
# if edad<=10:
#     print("NIÑO")
# elif edad >=11 and edad<=20:
#     print("ADOLESCENTE")
# elif edad >=21 and edad<=35:
#     print("Es un jovén adulto")
# elif edad >=21 and edad<=35:
#     print("Es un jovén adulto")
# else:
#     print("ES UN ADULTO MAYOR")
    


# edad = int(input ("Ingrese su edad como un número entero"))
# if edad<=10:
#     print("NIÑO")
# elif edad<=20:
#     print("ADOLESCENTE")
# elif edad<=35:
#     print("jovén adulto")
# elif edad<=50:
#     print("adulto")
# else:
#     print("ES UN ADULTO MAYOR")


# num1= int(input ("Ingrese un primer número:"))
# num2= int(input ("Ingrese un segundo número:"))
# num3= int(input ("Ingrese un segundo número:"))
#  if num1<num2<num3:
#      print(num1,"Es menor")
# elif num3<num2<num1:
#     print(num3,"es menor")
#  else: 
#      print(num2,"es menor")


# num1= int(input ("Ingrese un primer número:"))
# num2= int(input ("Ingrese un segundo número:"))
# num3= int(input ("Ingrese un segundo número:"))

# if num1<=num2 and num1 <=num3:
#     print(num1, "Es el menor")
# elif num2 <=num1 and num2<=num3:
#     print(num2, "Es el menor")
# else:
#     print(num3, "es el menor")
