# hamming_distance
# TODO: pegar uma das strings como ref dps comparar elemento por elemento com a segunda string se for dif contar no contador

s1 ="1010"
s2 = "0101"

ls1 = list(s1)
ls2 = list(s2)
contador = 0
for i in ls1:
    for x in range(0,len(ls2)):
        if i != ls2[x]:
            contador = 1 + contador
        else:
            pass
print(contador)