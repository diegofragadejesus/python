texto = input('Escreva algo e veja os os valores primitivos ')

    
if texto.isdecimal()== True: 
   print(f'essa caracteres é um numero "{texto}"')
   texto =int
   print(texto)

elif texto.islower()== True :
   print(f'essas caracteres contem minúsculas "{texto}"')
   print(type(texto))

elif texto.isupper()== True :
   print(f'essas caracteres contem maiúsculas "{texto}"')
   print(type(texto))

else: 
   print('erro')