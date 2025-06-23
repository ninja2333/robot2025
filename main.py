import RPi.GPIO as GPIO
import time
import threading
import cam 
from seguilinea import controllo, segui_linea, turndx, turnsx


GPIO.setmode(GPIO.BCM) #numero pin virtuale 
BUTTON_PIN = 17 
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #istruzione pud down integra una restistenza

running = False 
thread = None

def main():
    print("ciao")
    segui_linea()

try: 
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW and not running: # se il bottone è in posizione on allora and not running verifica che il codice non stia già girando
            running = True 
            thread = threading.Thread(target=main) #crea un thread con la funzione main per eseguire si il check del bottone che la funzione nello stesso tempo
            thread.start() # inizia il thread

        elif GPIO.input(BUTTON_PIN) == GPIO.HIGH and running:
            running = False
            thread.join() # aspetta che il thread finisce

except KeyboardInterrupt:
    print("Interrotto da tastiera.")

finally:
    running = False
    if thread and thread.is_alive():
        thread.join()
    GPIO.cleanup() 