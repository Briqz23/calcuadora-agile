class Calculadora():
    def __init__(self,num1, num2):
        self.num1=num1
        self.num2=num2
    def adicao(self):
        return self.num1+self.num2
    def multiplicacao(self):
        return self.num1*self.num2
    def divisao(self):
        return self.num1/self.num2
    def subtracao(self):
        return self.num1-self.num2
num1=int(input("Insira o primeiro número: "))
num2=int(input("Insira o segundo número: "))
obj=Calculadora(num1,num2)
choice=1
while choice!=0:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão")
    choice=int(input("Escolha a operação: "))
    if choice==1:
        print("Resultado: ",obj.adicao())
    elif choice==2:
        print("Resultado: ",obj.subtracao())
    elif choice==3:
        print("Resultado: ",obj.multiplicacao())
    elif choice==4:
        print("Resultado: ",(obj.divisao()))
    elif choice==0:
        print("Saindo!")
    else:
        print("Escolha Inválida!!")
 
 
print()

