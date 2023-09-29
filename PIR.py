import board
import digitalio
import time

# Define the pin connected to the OUT (signal) of the HC-SR501 sensor
motion_sensor_pin = board.GP5

# Initialize the pin as a digital input
pir = digitalio.DigitalInOut(motion_sensor_pin)
pir.direction = digitalio.Direction.INPUT

while True:
    if pir.value:
        print("Motion detected!")
    else:
        print("No motion detected.")
    
    # Add a delay between readings
    time.sleep(1)
