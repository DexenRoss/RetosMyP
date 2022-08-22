def bus_sub(cad):
    for i in range(len(cadenas)):
        for j in range(1,len(cadenas[i])+1):
            subfijo=cadenas[i][0:j]
            if subfijo in subfijos.keys():
                subfijos[subfijo]+=1
            else:
                subfijos[subfijo]=1
    max=5
    sub=""
    for x in subfijos:
        if subfijos[x]>=max:
            sub = x
            max = subfijos[x]
    print("Subcadena: ",sub) 




if __name__=="__main__":
    subfijos={}
    cadenas=[]
    n=0
    while n<5:
        cad = input("Escribe una cadena: ")
        cadenas.append(cad)
        n+=1
    bus_sub(cadenas)