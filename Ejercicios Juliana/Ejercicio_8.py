#Ejercicio 8- suma de dígitos
digitos = input("Ingresar numero: ")
sum = 0

for numero in digitos:
    sum += int(numero)
print(sum) 

if sum % 2 == 0:
    print ("La suma es par") 
else:
    print ("La suma es impar")
