print("CALCULADORA")
def soma(a ,b):
  return  a + b
def sub (a , b):
  return a - b
def mut(a, b):
   return a * b
def dvs(a ,b):
   return a / b
def por(a,b):
   return (a * b) /100
escolha = int(input(f"Escolha uma função da calculadora  \n [1] Pra SOMA \n [2] Para SUBTRAÇÂO \n [3] Pra MUTIPLICAÇÃO \n [4] Pra DIVISÃO \n [5] Pra PORSENTAGEM \n Digite :"))
if escolha == 1:
    print('você escolheu ADIÇÃO')
    num1 = float(input("Esconlha um Numero :"))
    num2 = float(input("Escolha outro Numero :"))
    resutado =soma(num1 ,num2)
    print(f"a soma do valor {num1} + {num2} = {resutado}")
elif  escolha == 2 :
    print('Você escolheu SUBTRAÇÃO')
    num1 = int(input("Esconlha um Numero :"))
    num2 = int(input("Escolha outro Numero :"))
    resutado =sub(num1 ,num2)
    print(f"a subtração do valor {num1} - {num2} = {resutado}")
elif  escolha == 3 :
    print('Você escolheu MUTIPLICAÇÃO')
    num1 = int(input("Esconlha um Numero :"))
    num2 = int(input("Escolha outro Numero :"))
    resutado =mut(num1 ,num2)
    print(f"a mutiplicação do valor {num1} X {num2} = {resutado}")
elif  escolha == 4 :
    print('Você escolheu DIVISÃO')
    num1 = int(input("Esconlha um Numero :"))
    num2 = int(input("Escolha outro Numero :"))
    resutado =dvs(num1 ,num2)
    print(f"a divisão do valor {num1} / {num2} = {resutado}")
elif  escolha == 5 :
    print('Você escolheu PORSENTAGEM')
    num1 = int(input("Esconlha um Numero :"))
    num2 = int(input("Escolha outro Numero :"))
    resutado =por(num1 ,num2)
    print(f"a porsentagem do valor {resutado}%")
else: 
   print ('fim da seção')
   