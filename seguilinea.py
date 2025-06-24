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
    antdx.throttle = -0.8
    postdx.throttle = -0.8
    antsx.throttle = -0.2
    postsx.throttle = -0.2
    time.sleep(tempo)
    antdx.throttle = 0
    postdx.throttle = 0
    antsx.throttle = 0
    postsx.throttle = 0

def turnsx(tempo):
    antsx.throttle = -0.8
    postsx.throttle = -0.8
    antdx.throttle = -0.2
    postdx.throttle = -0.2
    time.sleep(tempo)
    antdx.throttle = 0
    postdx.throttle = 0
    antsx.throttle = 0
    postsx.throttle = 0

def controllo(tempo):
    turndx(tempo)
    turnsx(tempo)

async def segui_linea():
    #async for mask in start_cam():
        start_ruote()
        while True:
            async for mask in start_cam():
                if await rilevamento(mask) == 1:
                    await asyncio.sleep(0.5)
                    print("mi muovo")
                    antdx.throttle = -1.0
                    postdx.throttle = -1.0
                    antsx.throttle = -1.0
                    postsx.throttle = -1.0
                else:
                    print("controllo")
                    time.sleep(0.5)
                    controllo(1)
                    await asyncio.sleep(0.1)
async def main():
     await segui_linea()

asyncio.run(main())