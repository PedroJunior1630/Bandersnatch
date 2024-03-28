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

qntd = 40
while qntd > 0:
    c =  " " * qntd
    print(c,"                        __")
    print(c," .-----------------------'  |")
    print(c,"/| _ .---. .---. .---. .---.|")
    print(c,"|j||||___| |___| |___| |___||")
    print(c,"|=|||=======================|")
    print(c,"[_|j||(O)\__________|(O)\___]")
    tempo(0.1)
    limpa()
    qntd -= 1
