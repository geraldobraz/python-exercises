# Geraldo Braz - 8 Linhas
# *** Codigo 1: 8 linhas
while True:
    cpf = [int(s) for s in list(input("Digite o cpf:\n>> ")) if s.isdigit()]
    if len(cpf) == 11:
        break
f = ((sum([n * (10 - i) for i, n in enumerate(cpf[0:9])]) * 10) % 11)
f = 0 if f == 10 else f
s = ((sum([n * (11 - i) for i, n in enumerate(cpf[0:10])]) * 10) % 11)
print(f == cpf[-2] and s == cpf[-1])

'''
# *** Codigo 2:
def Validador_Cpf(cpf_):
    cpf = [int(s) for s in list(cpf_) if s.isdigit()]
    if len(cpf) != 11:
        return False
    else:
        f = ((sum([n * (10 - i) for i, n in enumerate(cpf[0:9])]) * 10) % 11)
        f = 0 if f == 10 else f
        s = ((sum([n * (11 - i) for i, n in enumerate(cpf[0:10])]) * 10) % 11)
        return (f == cpf[-2] and s == cpf[-1])

print(Validador_Cpf(input("Digite seu cpf:\n>> ")))
'''