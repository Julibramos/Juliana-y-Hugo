n=int(input("ingrese el numero: \n"))
div=0
for i in range(1,n+1,1):
    if n%i==0:
        div=div+1

if div==2:
    print("primo")
else:
    print("no es primo")

