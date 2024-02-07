import math
co = float(input('Comprimento do cateto oposto :'))
cn = float(input('Comprimento do cateto adiacente :'))
h1 = math.hypot(co ,cn)
print(f'A hipotenusa vai medir {h1:.2f}')