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

