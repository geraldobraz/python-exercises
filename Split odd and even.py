'''
Test.assert_equals(split_odd_and_even(123), [1,2,3])
Test.assert_equals(split_odd_and_even(111),  [111])
Test.assert_equals(split_odd_and_even(223),  [22,3])
'''
def split_odd_and_even(n):
    numeros = [int(i) for i in n]
    print(numeros)


even = []
ods = []
saida = []
numeros = [int(i) for i in "113"]
# print(len(numeros))
for x in range(0,len(numeros)):

    if numeros[x]%2 == 0:
        print("Even",numeros[x])


    else:
        print("Ods",numeros[x])
        if (x+1) < len(numeros):
            if numeros[x+1]%2 != 0:
                print("Prox tmb n e' par")
                ods.append(numeros[x])
        else:
            print("NAO ok")
print(ods)












# for x in range(0,len(numeros)):
#     print(numeros[x])
#     if (numeros[x]%2) == 0:
#         # print(numeros[x+1])
#         if numeros[x+1]%2 ==0:
#             even.append(numeros[x])
#             validador = True
#         else:
#             if validador:
#                 saida.append(even)
#                 validador = False
#             else:
#                 saida.append(numeros[x])
#     else:
#         saida.append(numeros[x])
#
# print(saida)
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
