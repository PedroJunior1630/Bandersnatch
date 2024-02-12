def tempo(seg=1):
    from time import sleep
    sleep(seg)


def limpa():
    import os
    os.system('cls' if os.name == "nt"  else "clear")


def linha(tipo="=+=",tam=30,cor="\033[1;32m"):
    print(cor)
    print(tipo*tam)


def mensagemErro(msg):
    limpa()
    linha("=-=",20,cor="\033[1;31m")
    print("""\033[1;31m
           ___ _ __ _ __ ___  _ __ 
          / _ \ '__| '__/ _ \| '__|
          |  __/ |  | | | (_) | |   
          \___|_|  |_|  \___/|_|       
    """)
    linha("=-=",20,"\033[1;31m")
    tempo(2)
    limpa()
    linha("===",20,"\033[1;31m")
    print(f"\033[1;97m{msg.center(60)}\033[m")
    linha("===",20,"\033[1;31m")


def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except:
            mensagemErro("DIGITE NOVAMENTE!")
        else:
            return a



def telaMenu(*opcs):
    print(f"""
    -------------------------------------------------
    /      B  A  N  D  E  R  S  N  A  T  C  H       
    /
    /   [ 1 ] - {opcs[0]}
    /   [ 2 ] - {opcs[1]}
    /   [ 3 ] - {opcs[2]}                           
    /                                               
    -------------------------------------------------
    """)
    opc = leiaInt('Qual sua opção? ')
    return opc


def layoutGame(msg):
    letras = ["",""]
    for letra in msg:
        letras[0] = letras[0] +  "  "+letra+"  "

        linha("---",21)
        print("\033[1;97m")
        print(f"{letras[0]}")
        print("\033[m")
        linha("---",21)
        
        tempo(0.3)
        limpa()


def comecaJogo():
    pass


def finalizaJogo():
    pass


def mostraSobre():
    pass


layoutGame("BANDERSNATCH")
menu = telaMenu("JOGAR", "FINALIZAR JOGO", "SOBRE")

if menu == 1:
    comecaJogo()
elif menu == 2:
    finalizaJogo()
elif menu == 3:
    mostraSobre()
