import random

def jogo_numero_misterioso():
    numero_misterioso = random.randint(1, 10)
    tentativas = 0
    pontos = 0

    print("Bem-vindo ao Jogo do Número Misterioso!")
    print("Tente adivinhar o número entre 1 e 10.")

    while True:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        if tentativa == numero_misterioso:
            print(f"Parabéns! Você acertou o número misterioso em {tentativas} tentativas.")
            pontos += 1
            break
        elif tentativa < numero_misterioso:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    return pontos

def main():
    total_pontos = 0
    num_rodadas = 3  # Você pode ajustar o número de rodadas conforme necessário

    for rodada in range(1, num_rodadas + 1):
        print(f"\nRodada {rodada}:")
        pontos_rodada = jogo_numero_misterioso()
        total_pontos += pontos_rodada
        print(f"Pontos da Rodada {rodada}: {pontos_rodada}")

    print("\nTotal de Pontos: ", total_pontos)

if __name__ == "__main__":
    main()

    
