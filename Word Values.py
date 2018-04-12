# Código Word Values
# Disciplina de Python
# __author__ : Geraldo Braz
import string

def name_value(my_list):
    teste = {(list(string.ascii_lowercase)[i]): (i+1) for i in range(0, 26)}
    str(my_list).replace(" ", "")
    soma = 0
    for a in my_list:
        soma = teste[a] + soma
    return soma

stList = ["codewars","ada","xyz"]

for a in range(0,len(stList)):
    print((name_value(stList[a]))*(a+1))