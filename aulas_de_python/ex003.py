def sla(a):
    return 15 * a /100
salario = float(input('Qual é o Salário atual dofncionario ?:R$'))
r =sla(salario)
novo = salario + sla(salario)
print(f'O salário do funcionario era :R${salario:.2f} ,com um almento de 15% ficou :R${novo:.2f} , e o total do almento foi de :R${r:.2f}')