print("olá mundo")
def soma(a ,b):
  return  a + b
def sub (a , b):
  return a - b
escolha = int(input(f"Escolha uma função da calculadora  \n [1] Pra SOMA \n [2] Para SUBTRAÇÂO \n Digite :"))
if escolha == 1:
    num1 = float(input("Esconlha um Numero :"))
    num2 = float(input("Escolha outro Numero :"))
    resutado =soma(num1 ,num2)
    print(f"a soma do valor {num1} + {num2} = {resutado}")
elif  escolha == 2 :
    num1 = float(input("Esconlha um Numero :"))
    num2 = float(input("Escolha outro Numero :"))
    resutado =sub(num1 ,num2)
    print(f"a subtração do valor {num1} - {num2} = {resutado :.f2}")
else: 
   print ('fim da seção')