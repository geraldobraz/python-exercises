# Código Word Values
import string
def name_value(my_list):
    resp = []
    for a in range(0,len(my_list)):
        teste = {(list(string.ascii_lowercase)[i]): (i+1) for i in range(0, 26)}
        my_list[a]= str(my_list[a]).replace(" ", "")
        soma = 0
        for i in my_list[a]:
            soma = teste[i] + soma
        resp.append(soma*(a+1))
    return resp

stList = ["abc abc","abc abc","abc","abc"]

print(name_value(stList))
