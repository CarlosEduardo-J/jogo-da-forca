import random

# Lista de palavras
palavras = ["python", "programacao", "computador", "desenvolvedor", "dados"]

# Escolhe palavra aleatória
palavra = random.choice(palavras)
tentativas = 6
letras_descobertas = ["_" for _ in palavra]

print("=== JOGO DA FORCA ===")

while tentativas > 0 and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    print(f"Tentativas restantes: {tentativas}")
    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                letras_descobertas[i] = letra
        print("Acertou!")
    else:
        tentativas -= 1
        print("Errou!")

if "_" not in letras_descobertas:
    print(f"\nParabéns! Você ganhou! A palavra era '{palavra}'.")
else:
    print(f"\nFim de jogo! A palavra era '{palavra}'.")

print("Obrigado por jogar!")