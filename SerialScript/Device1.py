import serial
import time
import datetime
import cmd
import os

if __name__ == '__main__':
    dir = "COMdata/"
    COM21 = 1
    COM22 = 1
    COM23 = 0
    COM24 = 0
    flashflag =1
    if flashflag:
        if (COM21 == 1): insturction1 = "C:/Users/zhoul/AppData/Local/Arduino15/packages/CubeCell/tools/CubeCellflash/0.0.1/CubeCellflash.exe -serial COM21 F:/MyDocument/ArduinoHex/CubeCell_HalfAA_REGION_CN470_RGB_0.cyacd"
        else: insturction1 = ""
        if (COM22 == 1): insturction2 = "C:/Users/zhoul/AppData/Local/Arduino15/packages/CubeCell/tools/CubeCellflash/0.0.1/CubeCellflash.exe -serial COM22 F:/MyDocument/ArduinoHex/CubeCell_HalfAA_REGION_CN470_RGB_0.cyacd"
        else: insturction2 = ""
        if (COM23 == 1): insturction3 = "C:/Users/zhoul/AppData/Local/Arduino15/packages/CubeCell/tools/CubeCellflash/0.0.1/CubeCellflash.exe -serial COM23 F:/MyDocument/ArduinoHex/CubeCell_HalfAA_REGION_CN470_RGB_0.cyacd"
        else: insturction3 = ""
        if (COM24 == 1): insturction4 = "C:/Users/zhoul/AppData/Local/Arduino15/packages/CubeCell/tools/CubeCellflash/0.0.1/CubeCellflash.exe -serial COM24 F:/MyDocument/ArduinoHex/CubeCell_HalfAA_REGION_CN470_RGB_0.cyacd"
        else: insturction4 = ""

        with cmd.PowerShell('GBK') as ps:
            outs, errs = ps.run(insturction1)
        print('error:', os.linesep, errs)
        print('output:', os.linesep, outs)
        with cmd.PowerShell('GBK') as ps:
            outs, errs = ps.run(insturction2)
        print('error:', os.linesep, errs)
        print('output:', os.linesep, outs)
        with cmd.PowerShell('GBK') as ps:
            outs, errs = ps.run(insturction3)
        print('error:', os.linesep, errs)
        print('output:', os.linesep, outs)
        with cmd.PowerShell('GBK') as ps:
            outs, errs = ps.run(insturction4)
        print('error:', os.linesep, errs)
        print('output:', os.linesep, outs)

    if(COM21): ser1 = serial.Serial('COM21', 115200, timeout=0.2)
    if(COM22): ser2 = serial.Serial('COM22', 115200, timeout=0.2)
    if(COM23): ser3 = serial.Serial('COM23', 115200, timeout=0.2)
    if(COM24): ser4 = serial.Serial('COM24', 115200, timeout=0.2)


    temp = b''
    recv1 = recv2 = recv5 = recv6 = temp
    if(COM21): ser1.write(' '.encode())
    if(COM22): ser2.write(' '.encode())
    if(COM23): ser3.write(' '.encode())
    if(COM24): ser4.write(' '.encode())
    time.sleep(0.1)

    setTime = datetime.datetime.now().strftime('%H%M%S%d%m%Y')
    filedate = datetime.datetime.now().strftime('%m-%d-%H-%M')
    if(COM21): ser1.write(('AT+setTime=' + setTime).encode())
    if(COM22): ser2.write(('AT+setTime=' + setTime).encode())
    if(COM23): ser3.write(('AT+setTime=' + setTime).encode())
    if(COM24): ser4.write(('AT+setTime=' + setTime).encode())
    time.sleep(0.1)
    print("settime success")
    #1 minute
    # startTime = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%H%M%d%m%Y')
    # startTime = startTime[0:4] + '00' + startTime[4:]
    #1 second
    # startTime = (datetime.datetime.now() + datetime.timedelta(seconds=2)).strftime('%H%M%S%d%m%Y')
    startTime = "10150003032023"
    if(COM21): ser1.write(('AT+startTime='+ startTime).encode())
    if(COM22): ser2.write(('AT+startTime=' + startTime).encode())
    if(COM23): ser3.write(('AT+startTime=' + startTime).encode())
    if(COM24): ser4.write(('AT+startTime=' + startTime).encode())
    time.sleep(0.1)

    setCycle = '2'
    if(COM21): ser1.write(('AT+setCycle=' + setCycle).encode())
    if(COM22): ser2.write(('AT+setCycle=' + setCycle).encode())
    if(COM23): ser3.write(('AT+setCycle=' + setCycle).encode())
    if(COM24): ser4.write(('AT+setCycle=' + setCycle).encode())
    time.sleep(0.1)

    if(COM21): ser1.write(('AT+PrimaryParaInit=' + '22').encode())
    if(COM22): ser2.write(('AT+PrimaryParaInit=' + '55').encode())
    if(COM23): ser3.write(('AT+PrimaryParaInit=' + '44').encode())
    if(COM24): ser4.write(('AT+PrimaryParaInit=' + '44').encode())
    recv1 = recv2 = recv3 = recv4 = temp
    while True:
        if(COM21):
            try:
                recv1 = ser1.readline()
            except:
                print("COM21 out!")
                COM21 = 0
        if(COM22):
            try:
                recv2 = ser2.readline()
            except:
                print("COM22 out!")
                COM22 = 0
        if(COM23):
            try:
                recv3 = ser3.readline()
            except:
                print("COM23 out!")
                COM23 = 0
        if(COM24):
            try:
                recv4 = ser4.readline()
            except:
                print("COM24 out!")
                COM24 = 0
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
        if recv3 is not temp:
            with open(dir + filedate + " COM23" + ".txt", mode='a') as f3:
                f3.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(recv3))
                f3.write('\n')
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'COM23: ', str(recv3))
        if recv4 is not temp:
            with open(dir + filedate + " COM24" + ".txt", mode='a') as f4:
                f4.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(recv4))
                f4.write('\n')
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'COM24: ', str(recv4))