import RPi.GPIO as GPIO
import time
import asyncio
import cam 
from seguilinea import controllo, segui_linea, turndx, turnsx


GPIO.setmode(GPIO.BCM) #numero pin virtuale 
BUTTON_PIN = 17 
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) #istruzione pud down integra una restistenza

running = False 
thread = None

async def main():
    print("ciao")
    await segui_linea()

async def monitor_button():
    global running, task
    try:
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW and not running:
                print("Bottone premuto, avvio task...")
                running = True
                task = asyncio.create_task(main())
            elif GPIO.input(BUTTON_PIN) == GPIO.HIGH and running:
                print("Bottone rilasciato, fermo task...")
                running = False
                if task:
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        print("Task annullato.")
                    task = None
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        print("Monitor interrotto.")

async def main():
    try:
        await monitor_button()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Interrotto da tastiera.")

            
