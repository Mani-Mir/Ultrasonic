from machine import Pin, I2C
import ssd1306
from hcsr04 import HCSR04
from time import sleep


i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = HCSR04(trigger_pin=14, echo_pin=12, echo_timeout_us=1000000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

try:
    
    while 1:
      oled.fill(0)
      distance = sensor.distance_mm()
      
      print('Distance:', distance, 'mm')
      oled.text("Distance (mm)", 0, 20)
      oled.text(str(distance), 0, 40)
      oled.show()
      sleep(.2)
except Keyboardintrrupt:
    pass

