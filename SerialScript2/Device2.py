import serial
import time
import datetime

if __name__ == '__main__':
    dir = "../SerialScript/COMdata/"
    COM21 = 11
    COM22 = 11
    COM23 = 1
    COM24 = 1
    if(COM21 == 1): ser1 = serial.Serial('COM21', 115200, timeout=0.2)
    if(COM22 == 1): ser2 = serial.Serial('COM22', 115200, timeout=0.2)
    if(COM23 == 1): ser3 = serial.Serial('COM23', 115200, timeout=0.2)
    if(COM24 == 1): ser4 = serial.Serial('COM24', 115200, timeout=0.2)
    temp = ser3.readline()
    recv1 = recv2 = recv5 = recv6 = temp
    # if(COM21): ser1.write(' '.encode())
    # if(COM22): ser2.write(' '.encode())
    # if(COM23): ser3.write(' '.encode())
    # if(COM24): ser4.write(' '.encode())
    # time.sleep(0.1)
    #
    # setTime = datetime.datetime.now().strftime('%H%M%S%d%m%Y')
    filedate = datetime.datetime.now().strftime('%m-%d %H:%M')
    # if(COM21): ser1.write(('AT+setTime=' + setTime).encode())
    # if(COM22): ser2.write(('AT+setTime=' + setTime).encode())
    # if(COM23): ser3.write(('AT+setTime=' + setTime).encode())
    # if(COM24): ser4.write(('AT+setTime=' + setTime).encode())
    # time.sleep(0.1)
    #
    # startTime = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%H%M%d%m%Y')
    # startTime = startTime[0:4] + '00' + startTime[4:]
    # #startTime = "14481012052022"
    # if(COM21): ser1.write(('AT+startTime='+ startTime).encode())
    # if(COM22): ser2.write(('AT+startTime=' + startTime).encode())
    # if(COM23): ser3.write(('AT+startTime=' + startTime).encode())
    # if(COM24): ser4.write(('AT+startTime=' + startTime).encode())
    # time.sleep(0.1)
    #
    # setCycle = '2'
    # if(COM21): ser1.write(('AT+setCycle=' + setCycle).encode())
    # if(COM22): ser2.write(('AT+setCycle=' + setCycle).encode())
    # if(COM23): ser3.write(('AT+setCycle=' + setCycle).encode())
    # if(COM24): ser4.write(('AT+setCycle=' + setCycle).encode())
    # time.sleep(0.1)
    #
    # if(COM21): ser1.write(('AT+PrimaryParaInit=' + '33').encode())
    # if(COM22): ser2.write(('AT+PrimaryParaInit=' + '55').encode())
    # if(COM23): ser3.write(('AT+PrimaryParaInit=' + '11').encode())
    # if(COM24): ser4.write(('AT+PrimaryParaInit=' + '44').encode())
    while True:
        if(COM21==1): recv1 = ser1.readline()
        if(COM22==1): recv2 = ser2.readline()
        if(COM23==1): recv5 = ser3.readline()
        if(COM24==1): recv6 = ser4.readline()
        if recv1 is not temp:
            with open(dir + filedate + " COM21" + ".txt", mode='a') as f1:
                f1.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(recv1))
                f1.write('\n')
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'COM21: ', str(recv1))
        if recv2 is not temp:
            with open(dir + filedate + " COM22" + ".txt", mode='a') as f2:
                f2.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(recv2))
                f2.write('\n')
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'COM22: ', str(recv2))
        if recv5 is not temp:
            with open(dir + filedate + " COM23" + ".txt", mode='a') as f5:
                f5.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(recv5))
                f5.write('\n')
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'COM23: ', str(recv5))
        if recv6 is not temp:
            with open(dir + filedate + " COM24" + ".txt", mode='a') as f6:
                f6.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(recv6))
                f6.write('\n')
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'COM24: ', str(recv6))