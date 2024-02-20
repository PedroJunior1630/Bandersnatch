def tempo(seg=1):
    from time import sleep
    sleep(seg)


def limpa():
    import os
    os.system('cls' if os.name == "nt"  else "clear")


def relogio():
    print("""
            ____
           /    |
          /----/
         / ++ /
        /----/
       /    /
       \___/
    """)
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
relogio()
