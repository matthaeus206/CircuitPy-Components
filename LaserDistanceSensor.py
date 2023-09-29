import board
import busio
import adafruit_vl53l0x

# Initialize I2C communication
i2c = busio.I2C(board.SCL, board.SDA)

# Create a VL53L0X object
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    try:
        # Read the distance in millimeters
        distance_mm = vl53.range
        print(f"Distance: {distance_mm}mm")
    except RuntimeError as e:
        print(f"Error: {e}")

    # Add a delay between measurements
    time.sleep(0.5)
