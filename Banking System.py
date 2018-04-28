class User():
    def __init__(self, nome,saldo_atual,cheking_account):
        self.name = nome
        self.balance = saldo_atual
        self.cheking_account = cheking_account
    def getsaldo(self):
        return self.balance
    def getcheck(self):
        return self.cheking_account
    def withdraw(self,qtde):
        self.balance = self.balance - qtde
        if self.balance >= 0:
            return str(self.name)+ " has "+ str(self.balance)+"."
        else:
            raise ValueError("Error")
    def check(self,pessoa,qtde):
        if pessoa.getsaldo() < qtde:
            raise ValueError("Saldo Insuficiente")
        if not pessoa.getcheck():
            raise ValueError("Error Check")

        self.saldo_atual = qtde + self.saldo_atual
        pessoa.saldo_atual -= qtde
        return str(self.name)+ " has " + str(self.balance)+" and "\
               + str(pessoa.nome) + " has " + str(pessoa.balance)+"."
    def add_cash(self,qtde):
        self.saldo_atual +=qtde
        return str(self.name)+ " has "+ str(self.balance)+"."


