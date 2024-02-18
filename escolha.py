def escolha(op1="",op2=""):
    import random
    from time import sleep
    import os
    import keyboard
    qntd = 36
    esp = 1
    abso = qntd

    for c in range(0,qntd):    
        if c % 2 == 1:
            print(" " * esp, "_"*qntd)
            esp += 1
            qntd -= 1
        else:
            qntd -= 1
            print(" "*esp,"_" * qntd)

        if c == abso-1:
            r = random.randint(1,2)
            if r == 1:
                print(f"\033[1;32m{op1:>15}\033[m",end = "")
                print(f"{'|':>5}",end = "")
                print(f"{op2:>15}")
                return r
            if r == 2:
                print(f"{op1:>15}",end = "")
                print(f"{'|':>5}",end = "")
                print(f"\033[1;32m{op2:>15}\033[m")
                return r
            sleep(5)

        else:
            print(f"{op1:>15}",end = "")
            print(f"{'|':>5}",end = "")
            print(f"{op2:>15}")
            sleep(0.2)
            os.system('cls' if os.name == "nt" else "clear")
            return o
            
opcoes = escolha("SUGGAR PUFFS","SUCRILHOS")
print(f"Você esoclheu a opção: {opcoes}")
