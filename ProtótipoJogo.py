def tempo(seg=1):
    from time import sleep
    sleep(seg)


def limpa():
    import os
    os.system("cls" if os.name == "nt" else "clear")


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
    print("Aperte 'Enter' para pular abertura e começar o jogo")


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


def aviso():
    linha("=-=",30,"\033[1;33m")
    print("ESTEJA PREPARADO PARA PRESSIONAR '1' OU '2' NO TECLADO PARA ESCOLHER AS OPÇÕES")
    linha("=-=",30,"\033[1;33m")
    print("\033[m")
    tempo(3)


def telaMenu(*opcs):
    import keyboard
    print(f"""
    -------------------------------------------------
    /      B  A  N  D  E  R  S  N  A  T  C  H       
    /           ___________________
    /   [ 1 ] - | {opcs[0]}           |
    /           -------------------
    /           ___________________
    /   [ 2 ] - | {opcs[1]}           |
    /           -------------------
    /           ___________________
    /   [ 3 ] - | {opcs[2]}  |                          
    /           -------------------
    -------------------------------------------------
    """)
    print("Clique no teclado númerico de acordo com as opções.")
    while True:
        if keyboard.is_pressed('1'):
            return 1
        if keyboard.is_pressed('2'):
            return 2
        if keyboard.is_pressed('3'):
            return 3


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
    print("  ",end = "")
    for letra in msg:
        print(f'{letra}',end = "")
        tempo(0.08)
    print("  ")
    linha("=",tam)
    tempo(temp)
    print("")


def fala(msg,pessoa,temp=1.5):
    print(f"\033[1;97m{pessoa}: \033[m",end="")
    if pessoa.upper() == "PAI":
        cor = "\033[1;33m"
    elif pessoa.upper() == "STEFAN":
        cor = "\033[1;32m"

    print(cor,end= "")
    for letra in msg:
        print(f"{letra}",end="")
        tempo(0.06)
    print("\033[m")
    tempo(temp)
    print("")


def pensamento(msg,pessoa,temp=1.5):
    linha("~~",40,"\033[1;97m")
    print(f"\033[1;97m{pessoa}: \033[m",end="")
    for letra in msg:
        print(f"{letra}",end="")
        tempo(0.06)
    print("\033[m")
    tempo(temp)
    linha("~~",40,"\033[1;97m")
    print("\033[m")


def escolha(op1="",op2="",tipo1="nda",tipo2="nda"):
    import random
    import keyboard
    qntd = 36
    esp = 1
    
    for c in range(0,qntd):
        if c % 2 == 1:
            print(" " * esp, "_"*qntd)
            esp += 1
            qntd -= 1
        else:
            qntd -= 1
            print(" "*esp,"_" * qntd)

        if c == 35:
            r = random.randint(1,2)
            if r == 1:
                print(f"\033[1;32m{op1:>15}\033[m",end = "")
                print(f"{'|':>5}",end = "")
                print(f"{op2:>15}")
                anima(tipo1)
                
            else:
                print(f"{op1:>15}",end = "")
                print(f"{'|':>5}",end = "")
                print(f"\033[1;32m{op2:>15}\033[m")
                anima(tipo2)
            tempo(5)

        else:
            print(f"{op1:>15}",end = "")
            print(f"{'|':>5}",end = "")
            print(f"{op2:>15}")
            tempo(0.2)
            limpa()
            if keyboard.is_pressed('1'):
                return 1
            if keyboard.is_pressed('2'):
                return 2


def carregando():
    s = ">"
    linha("=-=",10)
    for c in range(10,110,10):
        print("Carregando: ",end = "")
        print(s,end ="",flush="True")
        print(f" {c}%")
        tempo(0.5)
        limpa()
        s = s + ">"
        linha("=-=",10)
    print("CARREGADO COM SUCESSO!")
    tempo(4)
    limpa()



def anima(tipo):
    print("\033[1;97m")
    if tipo == "relogio":
        m =  2
        s =  0
        while True:
            if s == 10:
                s = 0
                m = 3
            print(f"""
            ______________
            /____________/
            | 0 8 : {m} {s} |
            -------------/
            """)
            tempo(0.5)
            limpa()
            s = s + 1
            if m == 3:
                print("BIIIPP!!!!")
                tempo(3)
                break

    elif tipo == "pilula":
        print("""
           ________
          /        \ 
          | PILLS  |
           \______/
            |    |
            |    |
            |    |
            |    |
            \____/
        """)
        tempo(1.5)
        limpa()
        print("""
            ____
           /    |
          /----/
         / ++ /
        /----/
       /    /
       \___/
        """)
        tempo(1.5)

        
    elif tipo == "livro":
        print("""
      ______________________
     / \____________________/ 
     |  |                   |
     |  |                   |
     |  |                   |
     |  |                   |
     |  |   BANDERSNATCH    |
     |  |                   |
     |  |                   |
     |  |                   |
     |  | ~Jerome F Davies  |
      \ |                   |
       \--------------------|
    """)
        
    elif tipo == "cereais":
       print("""
     _______________     
    /______________/|
    |              ||
    |              ||
    |              ||
    | SUGAR PUFFS  ||
    |              ||
    |              ||
    |______________|/
                        OU       _______________     
                                /______________/|           
                                |              ||
                                |              ||
                                |              ||
                                |   FROSTIES   ||
                                |              ||
                                |              ||
                                |______________|/ 
             
    """)
    elif tipo == "cereal1":
        print("""
        _______________     
        /______________/|
        |              ||
        |              ||
        |              ||
        | SUGAR PUFFS  ||
        |              ||
        |              ||
        |______________|/
        """)

    elif tipo == "cereal2":
        print("""
         _______________     
        /______________/|           
        |              ||
        |              ||
        |              ||
        |   FROSTIES   ||
        |              ||
        |              ||
        |______________|/ 
        """)

    elif tipo == "fitas":
        print("""
        .------------------------.
        |  ////////       NOW 2  |
        | //  __  ______  __     |
        |    /  \|\.....|/  \    |
        |    \__/|/_____|\__/    |                                                
        |                        |                                                
        |    ________________    |                                                
        |___/_._o________o_._\___| 
        """)
        print("""
                    .------------------------.
                    |  ////////  THOMPSON T  |
                    | //  __  ______  __     |
                    |    /  \|\.....|/  \    |
                    |    \__/|/_____|\__/    |                                                
                    |                        |                                                
                    |    ________________    |                                                
                    |___/_._o________o_._\___| 
        """)

    elif tipo == "predio":
        print("""
             ________________________________________
            /_____________________________________/ |
            |             TUCKERSOFT              | |
            |-------------------------------------| |
            |                                     | |
            |  []      []       []      []        | |
            |                                     | |
            |  []      []       []      []        | |
            |                                     | |
            |                                     |/
        """)
    elif tipo == "cha":
        print("""
            ~~~~~~~~~
           /___________\ 
           |           |>
           \   CHÁ    /
            \________/   
        """)
    print("\033[m")


def comecaJogo():
    tempo(1)
    limpa()
    carregando()
    tocaMusica("relax.mp3")
    anima("relogio")
    comentario("9 de Julho de 1984",2)
    # Data 9/07/1984
    # Quarto do stefan
    # Exbir um relógio
    comentario("Stefan acorda as 08:30 e se dirige ao banheiro para tomar seu remédio.",5)
    limpa()
    # Remédio(Pilulas)
    comentario("Stefan toma suas pilulas e lava seu rosto.",5)
    anima("pilula")
    
    limpa()
    # Exbir corredor 
    # Exibir o pai do Stefan
    comentario("Ele encontra seu pai ao sair do banheiro.",3)
    limpa()

    fala("Café da manhã?","Pai",2)
    #exibir o stefan
    fala("Hum","Stefan",1)
    limpa()
    # Exibir uma mesa
    # Exibir o chá
    comentario("Stefan está lendo seu livro sentado na mesa da cozinha.")

    fala("Aqui está seu chá...","Pai",1)
    anima("cha")

    comentario("...",1)
    fala("Obrigado Pai...","Pai",1)

    fala("Desculpa, eu tava distraído, eu preciso arrumar tudo pra hoje","Stefan")

    fala("O pessoal que trabalha com computadores?","Pai")

    fala("É...","Stefan",1)

    fala("Da Tuckersoft, fazem os jogos do Colin Ritman","Stefan")

    fala("Ah não! aquele Colin Ritman?! :O","Pai",1)

    comentario("...",1)

    fala("O Sr Thakur, o dono, disse que eu podia mostrar minha demo de Bandersnatch","Stefan")

    fala("Bander-o quê?","Pai",1)

    fala("Bandersnatch... É baseado nesse livro.","Stefan",2)

    comentario('Stefan mostra o livro "Bandersnatch" para o pai')

    anima("livro")

    fala("Era da sua mãe?","Pai",1)

    fala("Estava nas coisas dela... :|","Stefan",1)

    fala("Mas eu não acho que ela leu :|","Stefan",2)

    fala("Eu acho que não... <:|","Pai",1)
    
    comentario("Seu pai olha pro livro....")
    anima("livro")

    fala('"Jerome F Davies"... não deve ser muito bom escritor, você sempre está avançando e voltando este livro O-O',"Pai")

    fala("Não é isso... É por que é interativo, estilo escolha sua aventura :|","Stefan",1)

    fala("Ham?","Pai",0.5)

    fala("Você decide o que o personagem faz, tipo um jogo... :P","Stefan",1)

    fala("Parece emocionante...","Pai",1)

    fala("Que tal decidir o que quer de café da manhã?","Pai",1)

    comentario("Seu pai abre o armário e te mostra duas caixas de cereais...",1)

    anima("cereais")

    fala("Os dois são infantis, mas você insiste...","Pai",1)

    aviso()

    opc1 = escolha("SUGAR PUFFS","SUCRILHOS","cereal1","cereal2")

    comentario("Seu pai coloca o cereal na mesa",1)

    anima(f"cereal{opc1}")
    tempo(3)

    limpa()

    #anima("Janela")
    #tocaMusica("TocToc.mp3")
    
    print("TOC TOC!!!")
    tempo(0.2)

    comentario("SEU PAI BATE NA JANELA E MANDA O CACHORRO SAIR DO QUINTAL")

    fala("VAI PRA SUA CASA!!!","Pai",1)

    fala("É aquele maldito cachorro do vizinho!... >:|","Pai",1)

    fala("Ele vai acabar com a gente... :|","Pai",1)

    comentario("Stefan se dirige ao ponto de ônibus para ir a sede da Tuckersoft")
    #anima parada
    limpa()

    comentario("Stefan pega o ônibus")
    print("                        __")
    print(" .-----------------------'  |")
    print("/| _ .---. .---. .---. .---.|")
    print("|j||||___| |___| |___| |___||")
    print("|=|||=======================|")
    print("[_|j||(O)\__________|(O)\___]")
    
    pensamento("Acho melhor ouvir uma musica enquanto chego lá...","Stefan",2)
    anima("fitas")
    tempo(3)
    comentario("Mas qual....")
    tempo(2)

    opc2 = escolha("Thompson T","NOW 2","msc1","mcs2")

    if opc2 == 1:
        print("""
        .------------------------.
        |  ////////  THOMPSON T  |
        | //  __  ______  __     |
        |    /  \|\.....|/  \    |
        |    \__/|/_____|\__/    |                                                
        |                        |                                                
        |    ________________    |                                                
        |___/_._o________o_._\___| 
        """)
        tempo(2)
        limpa()
        tocaMusica("thompson.mp3")
        

        
    else:
        print("""
        .------------------------.
        |  ////////       NOW 2  |
        | //  __  ______  __     |
        |    /  \|\.....|/  \    |
        |    \__/|/_____|\__/    |                                                
        |                        |                                                
        |    ________________    |                                                
        |___/_._o________o_._\___| 
        """)
        tempo(2)
        limpa()
        tocaMusica("Now2.mp3")
        

    qntd = 40

    while qntd > 0:
        c =  " " * qntd
        print(c,"                        __")
        print(c," .-----------------------'  |")
        print(c,"/| _ .---. .---. .---. .---.|")
        print(c,"|j||||___| |___| |___| |___||")
        print(c,"|=|||=======================|")
        print(c,"[_|j||(O)\__________|(O)\___]")
        tempo(0.2)
        limpa()
        qntd -= 1

    limpa()
    tempo(1)
    comentario("Stefan chega ao prédio da Tuckersoft")
    tempo(2)
    anima("predio")

    
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

