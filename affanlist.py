from machine import Pin
from time import sleep

turning = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
led1= Pin(4,Pin.OUT)
led2= Pin(5,Pin.OUT)
led3= Pin(19,Pin.OUT)
led4= Pin(21,Pin.OUT)

for i in turning:
    led1.value(i[0])
    led2.value(i[1])
    led3.value(i[2])
    led4.value(i[3])
    sleep(0.5)



