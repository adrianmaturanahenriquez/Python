
from random import randint
gana=0
a=0
b=0
c=0
d=0
e=0 
z=int (input ("Cuantas veces lanzaras el dado? "))

for j in range(z):
    x= randint(1,6)
    print ("Dado",x,)
    if x==6:
        gana=gana+600
        a=a+1
    elif x==3:
        gana+gana +300
        b=b+1
    elif x==1:
        print ("sigue jugando")
        
        c=c+1
    else:
        gana=gana-50
        e=e+1
print ("si Entra al 6 ",a,)
print ("si Entra al 3 ",b,)
print ("si Entra al 1 ",c,)
print ("si Entra al resto ",e,)
print ("La ganancia total es: ",gana)


