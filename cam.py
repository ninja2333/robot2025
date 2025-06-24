import cv2
import numpy as np
import time
from picamera2 import Picamera
import asyncio


async def rilevamento(mask):
    soglia = 200
    area_nera = cv2.countNonZero(mask)
    if area_nera > soglia:
        return 1
    else:
        return 0

async def start_cam():
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (640, 480)
    picam2.preview_configuration.main.format = "BGR888"
    picam2.preview_configuration.controls.FrameRate = 32
    picam2.configure("preview")
    picam2.start()
    time.sleep(3.0)
    
    print("parto")

    while True:
        image = picam2.capture_array()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        nero_basso = np.array([105, 0, 105])
        nero_max = np.array([179, 255, 255])

        mask = cv2.inRange(hsv, nero_basso, nero_max)
        risultato = cv2.bitwise_and(image, image, mask=mask)
        
        cv2.imshow("Rilevamento Nero", risultato)
        area_nera2 = cv2.countNonZero(mask)

        if rilevamento(mask) == 1 :
            print("Area nera rilevata!")
            print(area_nera2)
            area_nera2 = cv2.countNonZero(mask)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    picam2.close()
    cv2.destroyAllWindows()

    return mask



   


