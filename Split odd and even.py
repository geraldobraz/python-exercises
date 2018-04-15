def isEven(n):
    return True if int(n)%2 == 0 else False
def split_odd_and_even(n):

    numeros = str(n)
    size = 0
    last = int(numeros[0])
    i = 1
    out = []
    tamanho_numeros = len(numeros)
    while size < tamanho_numeros:
        num = int(numeros[:i])
        if isEven(num):
            if not isEven(last):
                out.append(last)
                size += len(str(last))
                numeros = numeros[i - 1:]
                i = 1
            else:
                i += 1
        else:
            if isEven(last):
                out.append(last)
                size += len(str(last))
                numeros = numeros[i - 1:]
                i = 1
            else:
                i += 1

        if i > len(numeros[:i]):
            out.append(num)
            break

        last = num
    return out



