# -*- coding: utf-8 -*-

# importamos la librería tiempo para usar parones, y la de wiringpi

import time
import wiringpi2

# creamos una variable inicializada con la nomenclatura de Wiring pi

io=wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

# establecemos el modo de operacion del pin, en este caso es de salida
# hay que utilizar la nomenclatura de Wiring pi, es MUY IMPORTANTE

io.pinMode(7,io.OUTPUT)

# Creamos el bucle de actuación

for x in range (0,3):
     io.digitalWrite(7,io.HIGH)
     time.sleep(5)
     io.digitalWrite(7,io.LOW)
     time.sleep(5)
