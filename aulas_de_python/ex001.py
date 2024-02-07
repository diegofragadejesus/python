def area(a ,b):
    return a * b
def sub(a,b):
    return a / b
auta_p = float(input('Qual é a altura da parede ? :'))
larguta_p = float(input('Qual é a largura da parede ? :'))
r = area(auta_p , larguta_p)
r2 =sub(auta_p ,larguta_p)
print(f'sua parede tem a dimenção de {auta_p} x {larguta_p} sua area é de {r:.2f}m² \n e você vai precisar de {r2:.2f}Litros de tinta para pitar')