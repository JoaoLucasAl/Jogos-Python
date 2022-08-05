import forca
import adivinhacao

def escolha_jogo():
    jogo = int(input("************************************\n Escolha seu jogo\n************************************ \n(1) Advinhação (2) Forca\n"))
    if(jogo == 1):
        print("Jogando advinhação \n")
        adivinhacao.jogar()
    if(jogo == 2):
        print("Jogando forca \n")
        forca.jogar()
if(__name__ == '__main__'):
    escolha_jogo()