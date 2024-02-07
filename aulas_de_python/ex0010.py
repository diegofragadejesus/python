import math
angulo = float(input('Digite o ángulo que você deseja :'))
seno = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))
con = math.cos(math.radians(angulo))
print(f'O ángulo tem o seno de {seno:.2f}')
print(f'O ángulo tem o tangent de {tan:.2f}')
print(f'O ángulo tem o cosseno de {con:.2f}')
