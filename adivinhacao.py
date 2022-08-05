import random

def jogar():
    print("************************************\n Bem vindo ao jogo da advinhação\n************************************ \n")
    num_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    nivel = int(input(f"Qual o nível de dificuldade? \n(1) Fácil (2) Médio (3) Difícil\n"))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        chute_input = input(f"\nTentativa {rodada} de {tentativas}\nDigite um valor entre 1 e 100: ")
        print(f"Você digitou: {chute_input}")

        chute_input = int(chute_input)

        if(chute_input < 1 or chute_input > 100):
            print(f"Você digitou {chute_input}, deve digitar um número entre 1 e 100")
            continue

        acertou = chute_input == num_secreto
        maior = chute_input > num_secreto
        menor = chute_input < num_secreto

        if (acertou):
            print(f"Você acertou o número secreto que era {num_secreto} e fez {pontos} pontos")
            break
        else:

            if (maior):
                print(f"Você errou, {chute_input} é maior que o número secreto")
            elif (menor):
                print(f"Você errou, {chute_input} é menor que o número secreto")
            pontos_perdidos = abs(num_secreto - chute_input)
            pontos = pontos - pontos_perdidos

    print(f"Fim do jogo, o número era {num_secreto}")
if(__name__ == '__main__'):
    jogar()