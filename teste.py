import keyboard
import cv2
def tempo(seg):
    from time import sleep
    sleep(seg)

while True:
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Botão esquerdo clicado")
    if event == cv2.EVENT_RBUTTONDOWN:
        print("Botão direito clicado")


esp = " "
while True:
    if keyboard.is_pressed('w'):
        print("w")
    if keyboard.is_pressed('a'):
        print('a')
    if keyboard.is_pressed('s'):
        print('c')
    if keyboard.is_pressed('d'):
        print('d')
    if keyboard.is_pressed('b'):
        break

