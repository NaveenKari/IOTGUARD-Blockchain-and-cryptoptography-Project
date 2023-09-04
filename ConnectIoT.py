import serial
import time

def call(v):
    serialcommunication = serial.Serial('COM3', 9600)
    serialcommunication.timeout = 1
    while True:
        
        inputvar = v
    

        serialcommunication.write(inputvar.encode())

        break

    print(serialcommunication.readline().decode('ascii'))

    serialcommunication.close()

