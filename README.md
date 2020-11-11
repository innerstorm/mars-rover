# mars-rover
raspberry pi driven mars rover

## software
- raspbian 
- pyton3, 
- flask based web interface **OR** socket based client/server application written in python

### libraries and must have software

we want to go headless, so we need no GUI, nothing but the basic IO port driving part, the wlan, the python, ssh, maybe samba installed 


### GPIO mapping

we use BCM mapping of the Pi's IO pins

- 2 - in1
- 3 - in2
- 6 - ground
- 12 - enable1 / pwm 
- 18 - servo pwm
...

## hardware:

- raspberry pi zero w
- camera for raspberry pi / [wide angle camera](https://www.robofun.ro/camera/modul-de-camera-cu-unghi-larg-pentru-raspberry-pi.html)
- sg90 servo motor (5V) [link](https://components101.com/servo-motor-basics-pinout-datasheet)
- simple brushed motor with transmission (5V) [link](https://www.optimusdigital.ro/en/others/139-gearmotor-with-wheel.html)
- motor driver for brushed motor [link](https://hobbielektronikabolt.blogspot.com/2017/12/DC-motor-L298N-PWM.html)
- phone charger (>=2A, >=20.000 mAh)
- cables, lots of cables
- LEGO

### hardware connections

common ground is connected to the charger's (-), the Pi, the servo motor and the L298N motor driver

#### the servo 

we are connecting the servo directly to the raspberry pi, as it's working on 5V, and uses the Pi's pwm pins. Maybe, the 5V can come from the charger (as in: always on, pwm decides moving)
the servo can turn 180 degrees, we need to calibrate it well, also there is stuttering in the pwm from the Pi.

The servo has three wires:
- orange - pwm (to Pi)
- red - 5V
- black - ground 

#### the propulsion motor:

the motor is connected to the driver's out1 and out2 connections\
the driver's connections:

- gnd
- 5v
- out1/out2 (to motor)
- enable1 (to Pi) 
- in1/in2 (to Pi)

#### connections to the Pi:

- ground
- pwm output pin for the servo
- enable/pwm output for the propulsion (enable1)
- in1/in2 simple GPIO pins for in1/in2 of propulsion driver

#### ssh deply test
