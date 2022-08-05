import random





def jogar():
    abertura()
    palavra_secreta = carrega_palavra()
    lista_acertada = letras_acertada(palavra_secreta)
    print(lista_acertada)

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):
        chute = input("Chute uma letra: ").strip()

        if(chute.upper() in palavra_secreta.upper()):
            verfica_chute(chute, palavra_secreta, lista_acertada)
        else:
            erros += 1
            desenha_forca(erros)
        acertou = "_" not in lista_acertada
        enforcou = erros == 7
        print(lista_acertada)

    mensagem_final(acertou,palavra_secreta)



def abertura():
    print("************************************\n Bem vindo ao jogo da forca\n************************************ \n")

def carrega_palavra():
    arquivo = open("palavras.txt", encoding='utf-8', mode="r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))


    palavra_secreta = palavras[numero]
    return palavra_secreta

def letras_acertada(palavra):
    return  ["_" for letra in palavra]

def verfica_chute(chute, palavra_secreta, lista_acertada):
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                lista_acertada[index] = letra
                print(f"Encontrei a letra {letra} na posição {index}")
            index += 1


def mensagem_final(acertou, palavra_secreta):
    if (acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    print("Fim do jogo")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
    jogar()
