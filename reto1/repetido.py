#Autor: @EmilioCaballero99

#Pequeño programa que te dice el primer caracter de una cadena que no se repite
cadena= input("Escriba una frase o palabra: ")
pos=0
aux =0
car= " "
for i in cadena:
    cont =0
    car = i
    if i == " ":
        continue
    else:
        for j in cadena:
            if i==j:
                cont+=1           
        if(cont==1):
            aux = cont
            break
    pos+=1
    
if aux== 1:
    print(car, "en la posicion ",pos)
else:
    print(-1)

