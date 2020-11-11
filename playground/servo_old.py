import RPi.GPIO as  GPIO
import time

pin = 14
duty_c = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

servo = GPIO.PWM(pin, 50)
servo.start(duty_c)

try:
	while True:
		duty_c = float(input('ENTER:'))
		servo.ChangeDutyCycle(duty_c)
		#time.sleep(.5)
		#servo.ChangeDutyCycle(0)


except KeyboardInterrupt:
	print('GTFO')

finally:
	print('ceanup')
	GPIO.cleanup()





