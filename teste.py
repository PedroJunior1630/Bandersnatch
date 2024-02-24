i = 0


def limpa():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def tempo(seg=1):
    from time import sleep
    sleep(seg)


def linha(tipo="=+=",tam=30,cor="\033[1;32m"):
    print(cor)
    print(tipo*tam)


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

print("OLÀ")
tempo(1)
limpa()
pensamento("Acho melhor ouvir uma musica enquanto chego lá...","Stefan",2)
