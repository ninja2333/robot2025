from cam import rilevamento, start_cam
import time
from adafruit_servokit import ServoKit
import asyncio


def start_ruote():
    global kit,  antdx, postdx, antsx, postsx
    kit = ServoKit(channels=16)
    antdx = kit.continuous_servo[0]
    postdx = kit.continuous_servo[15]
    antsx =  kit.continuous_servo[4]
    postsx =  kit.continuous_servo[11]

def turndx(tempo):
    antdx.throttle = -1.0
    postdx.throttle = 1.0
    antsx.throttle = 1.0
    postsx.throttle = -1.0
    time.sleep(tempo)
    antdx.throttle = 0
    postdx.throttle = 0
    antsx.throttle = 0
    postsx.throttle = 0

def turnsx(tempo):
    antsx.throttle = -1.0
    postsx.throttle = 1.0
    antdx.throttle = 1.0
    postdx.throttle = -1.0
    time.sleep(tempo)
    antdx.throttle = 0
    postdx.throttle = 0
    antsx.throttle = 0
    postsx.throttle = 0

def controllo(tempo):
    turndx(tempo)
    turnsx(tempo)

async def segui_linea():
    while True:
        if rilevamento(start_cam) == 1:
            start_ruote()
            time.sleep(0.5)
            print("mi muovo")
            antdx.throttle = 1.0
            postdx.throttle = 1.0
            antsx.throttle = 1.0
            postsx.throttle = 1.0    
        else :
    #controlla
            print("controllo")
            start_ruote()
            time.sleep(0.5)
            controllo(1)

async def main():
    task1 = asyncio.create_task(rilevamento(start_cam()))
    task2 = asyncio.create_task(start_cam())
    task3 = asyncio.create_task(segui_linea())

    await asyncio.gather(task1, task2, task3)  # Aspetta entrambe, per sempre

asyncio.run(main())