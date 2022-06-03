from pyfirmata import Arduino, SERVO

port='/dev/tty/ACM0'

pin=3

board=Arduino(Port)

board.digital[pin].mode=SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)

def doorAutomate(val):
    if val==0:
        rotateServo(pin, 180)
    elif val==1:
        rotateServo(pin, 40)
