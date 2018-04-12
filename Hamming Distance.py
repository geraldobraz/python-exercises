# hamming_distance
def hamming_distance(a, b):
    listaS1 = [int(x) for x in a]
    listaS2 = [int(y) for y in b]
    contador = 0
    for i in range(0,len(listaS1)):
        if listaS1[i] != listaS2[i]:
            contador = contador+1
    return contador