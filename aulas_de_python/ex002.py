def pct(a):
    return (5 * a) / 100
preco = float(input('Qual é ovalor do produto ? :'))
r =pct(preco)
novo = preco - pct(preco)
print(f'o valor do prodoto antes : R${preco:.2f}  o valor do produto com 5% de desconto R${novo:.2f}  valor do desconto {r:.2f}')