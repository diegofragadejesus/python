import random
numeroS =random.randint(1,10)
pontos = 10 
tentativas = 1
def soma(a , b):
    return a + b

while True:
    chute = int(input(f'Escolha um numero entre 1 a 10 :'))
    if chute == numeroS:
        print(f'voce acertor o numero secreto {numeroS} em {tentativas} tentativas')
        break

    elif chute > numeroS:
        print(f'o numero secreto é menor que {chute}')

    else:
        print(f'o numero secreto é maior que {chute}')  
    tentativas += 1
    
    
       