def tempo(seg=1):
    from time import sleep
    sleep(seg)


def limpa():
    import os
    os.system('cls' if os.name == "nt"  else "clear")


def linha(tipo="=+=",tam=30):
    print("\033[1;36m")
    print(tipo*tam)


def layoutQuadrado(msg):
    letras = []
    for i,letra in enumerate(msg):
        letras.append(letra)
        linha("---",30)
        print("\033[1;97m")
        print(f"{letras}")
        print("\033[m")
        linha("---",30)
        tempo()
        limpa()


def animaQuadros(fps=5):
    layoutQuadrado("BANDERSNATCH")


animaQuadros()
