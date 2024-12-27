import RPi.GPIO as GPIO
import time

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
TRIG = 17  # Pin GPIO untuk Trigger
ECHO = 27  # Pin GPIO untuk Echo

# Setup pin GPIO
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Fungsi untuk mengukur jarak
def get_distance():
    # Pastikan Trigger dalam keadaan LOW
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.5)
    
    # Mengirimkan trigger pulse
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)  # Pulse selama 10 mikro detik
    GPIO.output(TRIG, GPIO.LOW)
    
    # Mengukur waktu untuk gelombang kembali
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()
    
    # Menghitung waktu pulse
    pulse_duration = pulse_end - pulse_start
    
    # Kecepatan suara di udara adalah 34300 cm/s
    # Jarak dalam cm = (kecepatan suara * waktu) / 2 (kembali ke sensor)
    distance = pulse_duration * 17150  # Konversi waktu menjadi jarak
    distance = round(distance, 2)  # Pembulatan hingga 2 desimal
    
    return distance

try:
    while True:
        distance = get_distance()
        print(f"Jarak: {distance} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program dihentikan.")
    GPIO.cleanup()
