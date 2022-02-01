
import gpio
from gpio import GPIO
import time
import logging
logging.basicConfig(format='%(asctime)s  %(message)s',level=logging.DEBUG)



def parse_user_input(string_from_user):
    splited = string_from_user.split(' ')
    enable_log = False
    pinX = 2
    pinY = 3
    for index, value in enumerate(splited):
        if "-i" in value:
            pinY= int(splited[index + 1])
        elif "-o" in value:
            pinX = int(splited[index + 1])

        elif "--log" in value:
            enable_log = True
    return pinX,pinY,enable_log

def run_toggele(gpioX,gpioY,enable_log):
    gpioY.high()

    while True:
        gpioX.low()
        time.sleep(1)
        if gpioY.get_value() ==1:
            gpioX.high()
            time.sleep(1)

        if enable_log:
            logging.debug(f' gpio{gpioY.pin_number} value: {gpioY.get_value()} and gpio{gpioX.pin_number}  value {gpioX.get_value()}')


if __name__ == '__main__':

    string_from_user=input("Enter your gpio number with input and output mode i.e. -i 23 -o 21. Here 23 gpio mode set "
                           "as input and 21 gpio mode set as output. (optional) --log for enable log: ")
    pin_x,pin_y,enable_log=parse_user_input(string_from_user)


    gpioX=GPIO(pin_x,gpio.output)
    gpioY=GPIO(pin_y,gpio.output)
    run_toggele(gpioX,gpioY,enable_log)

