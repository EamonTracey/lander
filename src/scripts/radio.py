import time

import adafruit_rfm9x
import board
import busio
import digitalio

# Initialize the RFM95W to operate at 915 Hz with CRC checksum.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
reset = digitalio.DigitalInOut(board.D6)
rfm95w = adafruit_rfm9x.RFM9x(spi, cs, reset, 915)
rfm95w.enable_crc = True

count = 0
while True:
    message = b"Hello from Asteria!"
    rfm95w.send(message)
    count += 1

    print(f"Sent message {count}: {message.decode()}")

    time.sleep(1)
