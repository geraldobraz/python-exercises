def split_odd_and_even(n):
     numeros = [int(i) for i in n]
     print(numeros)


even = []
ods = []
saida =[]
numeros = [int(i) for i in "112"]
print(numeros)
validador = False

for x in range(0,len(numeros)):
    print(numeros[x])
    if (numeros[x]%2) == 0:
        # print(numeros[x+1])
        if numeros[x+1]%2 ==0:
            even.append(numeros[x])
            validador = True
        else:
            if validador:
                saida.append(even)
                validador = False
            else:
                saida.append(numeros[x])
    else:
       saida.append(numeros[x])

print(saida)
    #     if (x+1)%2 == 0:
    #         even.append(x)
    #     else:
    #         pass
    # else:
    #     pass
        # print("Ods")
        # ods.append(x)


# even = ''.join(str(e) for e in even)
# ods = ''.join(str(e) for e in ods)
#
# saida.append(ods)
# saida.append(even)
