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
    linha("+-+",20,cor="\033[1;31m")
    print("""\033[1;31m
          ERROR
        .e$$$$e.
       e$$$$$$$$$$e
      $$$$$$$$$$$$$$
     d$$$$$$$$$$$$$$b
     $$$$$$$$$$$$$$$$
    4$$$$$$$$$$$$$$$$F
    4$$$$$$$$$$$$$$$$F
     $$$" "$$$$" "$$$
     $$F   4$$F   4$$
     '$F   4$$F   4$"
      $$   $$$$   $P
      4$$$$$"^$$$$$%
       $$$$F  4$$$$
        "$$$ee$$$"
        . *$$$$F4
         $     .$
         "$$$$$$"
          ^$$$$      
    """)
    linha("+-+",20,"\033[1;31m")
    tempo(2)
    limpa()
    linha("===",20,"\033[1;31m")
    print(f"{msg.center(60)}")
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


def layoutQuadrado(msg):
    letras = ["",""]
    for i,letra in enumerate(msg):
        letras[0] = letras[0] + "  "+letra+"  "
        linha("---",21)
        print("\033[1;97m")
        print(f"{letras[0]}")
        print("\033[m")
        linha("---",21)
        tempo(0.3)
        limpa()
    telaMenu("JOGAR", "FINALIZAR JOGO", "SOBRE")


def animaQuadros(fps=5):
    layoutQuadrado("BANDERSNATCH")


animaQuadros()
