import random
import string

def gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais):
    caracteres = ""
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation
    
    if not caracteres:
        print("Erro: Nenhuma opção selecionada para geração da senha.")
        return
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    comprimento = int(input("Digite o comprimento desejado da senha: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)

    if senha_gerada:
        print(f"\nSenha gerada: {senha_gerada}")
    else:
        print("Nenhuma senha gerada.")

if __name__ == "__main__":
    main()
