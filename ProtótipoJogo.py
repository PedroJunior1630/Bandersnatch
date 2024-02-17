def tempo(seg=1):
    from time import sleep
    sleep(seg)


def limpa():
    import os
    os.system('cls' if os.name == "nt"  else "clear")


def linha(tipo="=+=",tam=30,cor="\033[1;32m"):
    print(cor)
    print(tipo*tam)


def introGame():
    tempo(1)
    limpa()
    print("\033[1;32m")
    print("(c) PedroHDev Productions...")
    tempo(2)
    limpa()
    print("Inspirado no filme Black Mirror Bandersnatch da Netflix.\033[m")
    tempo(4)
    limpa()


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
        linha("---",30)
        print("\033[1;97m")
        print(f"{letras[0]}")
        print("\033[m")
        linha("---",30)
        
        tempo(0.5)
        limpa()


def tocaMusica(nome):
    from pygame import mixer
    
    mixer.init()

    mixer.music.load('C:/Users/ph751/OneDrive/Documentos/MeusProjetos/Bandersnatch/Musicas/'+nome)

    mixer.music.play()


def comentario(msg,temp=1):
    tam = len(msg) + 4
    linha("=",tam)
    print(f'{msg.center(tam)}  ')
    linha("=",tam)
    tempo(temp)
    limpa()


def fala(msg,pessoa,cor="\033[1;97m"):
    print(cor)
    print(f"{pessoa}: ",end="")
    for letra in msg:
        print(f"{letra}",end="")
        tempo(0.08)
    print("\033[m")


def escolha(op1="",op2=""):
    esp
    
    


def comecaJogo():
    tocaMusica("Relax.mp3")
    # Data 9/07/1984
    # Quarto do stefan
    # Exbir um relógio
    comentario("Stefan acorda as 08:30 e se dirige ao banheiro para tomar seu remédio.",8)
    tempo(5)
    limpa()
    # Remédio(Pilulas)
    comentario("Stefan tome suas pilulas e lva seu rosto.")
    tempo(3)
    limpa()
    # Exbir corredor 
    # Exibir o pai do Stefan
    fala("Café da manhã?","Pai","\033[1;33m")
    #exibir o stefan
    fala("Hum","Stefan","\033[1;32m")
    # Exibir uma mesa
    # Exibir o chá
    fala("Obrigado Pai...","Pai","\033[1;33m")
    #exbir a mesa
       


def finalizaJogo():
    pass


def mostraSobre():
    pass



tocaMusica("Intro8.mp3")
introGame()
layoutGame("BANDERSNATCH")
menu = telaMenu("JOGAR", "SOBRE", "FINALIZAR GAME")


if menu == 1:
    comecaJogo()

elif menu == 2:
    mostraSobre()

elif menu == 3:
    finalizaJogo()

