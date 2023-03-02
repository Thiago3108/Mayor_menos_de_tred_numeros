# programa para identificar el mayor de tres numeros 

print("---------------------------------")
print("------IDENTIFICAR EL MAYOR-------")
print("---------------------------------")

# input 
n1 = int(input("inserte el primer numero: "))
n2 = int(input("inserte el segundo numero: "))
n3 = int(input("inserte el tercer numero: "))

#procesing 

s = n1 < n2
a = n2 < n3
n = n1 < n3 

# output
 ## para n3
if (s == True):
    if (a == True):
        print("El numero mayor es: " + str(n3))
if (s == False):
    if (n == True):    
        print("El numero mayor es: " + str(n3))
 ## para n2 
if (s == True):
    if (a == False):
        print("El numero mayor es: " + str(n2))
 ## para n1
else:
    print("El numero mayor es: " + str(n1)) 

