i = 0
def limpa():
    import os
    os.system("cls" if os.name == "nt" else "clear")
while i <= 60:
    import keyboard
    from time import sleep
    i += 1
    print(f"{'OLA':>15}",end = "")
    print(f"{'|':>5}",end = "")
    print(f"{'ola':>15}")
    sleep(0.4)
    limpa()
    if keyboard.is_pressed('1'):
        break
