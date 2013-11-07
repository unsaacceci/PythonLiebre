'''
Created on 22/10/2013

@author: CARLOS1
'''

#Suma de dos numeros complejos
 
#Leer dos numeros complejos
NReal1 = int(raw_input("ingresar Nro1Real: "))
NImag1 = int(raw_input("ingresar Nro1Imaginario: "))
NReal2 = int(raw_input("ingresar Nro2Real: "))
NImag2 = int(raw_input("ingresar Nro2Imaginario: "))    
#Sumar los numeros complejos
AddReal = NReal1 + NReal2
#Sumar los numeros complejos
AddImag = NImag1 + NImag2
#Escribir la suma de los numeros complejos
print "Add Real: " + str(AddReal)
print "Add Imagine: "+ str(AddImag)