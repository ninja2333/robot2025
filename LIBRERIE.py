LIBRERIE
per sensore ultrasuoni
from hcsr04sensor import sensor

per 16 canali
import time
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

per infrarossi non servono librerie si comanda con pin gpio

per Pi camera rev 1.3
from picamera2 import Picamera2
import time
oppure per sistemi legacy 
from picamera import PiCamera
from time import sleep

per tutti i servo motori dovrebbe bastare questo
from adafruit_servokit import ServoKit
import time
che sarebbe da integrare con la libreria della 16 canali 