import board
import neopixel
import time

plate_1_pin = board.D18 # (pin 12)
plate_2_pin = board.D19 # (pin 35)
num_pixels = 96

plate_1 = neopixel.NeoPixel(
    plate_1_pin, num_pixels, brightness=0.1, auto_write=False
)
plate_2 = neopixel.NeoPixel(
    plate_2_pin, num_pixels, brightness=0.1, auto_write=False
)

while True:
    plate_1.fill((255, 0, 0))  # set plate 1 to red
    plate_1.show()

    plate_2.fill((255, 0, 0))  # set plate 2 to red
    plate_2.show()

    time.sleep(1)

    plate_1.fill((0, 255, 0))  # set plate 1 to green
    plate_1.show()

    plate_2.fill((0, 255, 0))  # set plate 2 to green
    plate_2.show()

    time.sleep(1)

    plate_1.fill((0, 0, 255))  # set plate 1 to blue
    plate_1.show()

    plate_2.fill((0, 0, 255))  # set plate 2 to blue
    plate_2.show()

    time.sleep(1)

