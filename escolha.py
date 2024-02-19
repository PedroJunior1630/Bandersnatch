def tempo(seg=1):
    from time import sleep
    sleep(seg)


def limpa():
    import os
    os.system('cls' if os.name == "nt"  else "clear")


def relogio():
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
relogio()
