import random

def escolher_palavra():
    palavras = ['python', 'estacio', 'aluno alan ',]
    return random.choice(palavras)

def exibir_palavra(palavra, acertos):
    exibicao = ''
    for letra in palavra:
        if letra in acertos:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def jogo_da_forca():
    palavra = escolher_palavra()
    tentativas = 6
    acertos = set()
    erros = set()

    print("Bem-vindo ao jogo da forca!")
    
    while tentativas > 0:
        print("\nPalavra: ", exibir_palavra(palavra, acertos))
        print("Tentativas restantes: ", tentativas)
        print("Letras erradas: ", ' '.join(erros))
        
        chute = input("Digite uma letra: ").lower()
        
        if chute in acertos or chute in erros:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if chute in palavra:
            acertos.add(chute)
            if set(palavra).issubset(acertos):
                print("\nParabéns! Você adivinhou a palavra:", palavra)
                break
        else:
            erros.add(chute)
            tentativas -= 1
            print("Letra incorreta.")
        
        if tentativas == 0:
            print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()
