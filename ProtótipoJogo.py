def tempo(seg=1):
    from time import sleep
    sleep(seg)


def limpa():
    import os
    os.system('cls' if os.name == "nt"  else "clear")


def linha(tipo="=+=",tam=30):
    print("\033[1;32m")
    print(tipo*tam)


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
    


def layoutQuadrado(msg):
    letras = ["",""]
    for i,letra in enumerate(msg):
        letras[0] = letras[0] + "  "+letra+"  "
        linha("---",21)
        print("\033[1;97m")
        print(f"{letras[0]}")
        print("\033[m")
        linha("---",21)
        tempo(0.5)
        limpa()
    telaMenu("JOGAR", "FINALIZAR JOGO", "SOBRE")


def animaQuadros(fps=5):
    layoutQuadrado("BANDERSNATCH")


animaQuadros()
