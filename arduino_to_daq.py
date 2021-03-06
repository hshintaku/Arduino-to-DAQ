# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:20:46 2019

@author: shintaku
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:01:17 2018

@author: lab
"""

import time, datetime, os, serial

ser = serial.Serial('COM3', 9600, timeout=1)


class Arduino():  
    def ArduinoAI(x,y,c):
#        import serial
        #ser = serial.Serial('COM3',9600,timeout=5)
        #ser.flushInput()
        #ser.open()
        c = []
        #配列cをclear
        ser.write(b'AI1:4')
        #time.sleep(0.01)
        ser_bytes = ser.readline().decode("utf-8")
        #decoded_bytes = ser_bytes[0:len(ser_bytes)].decode("utf-8")
        #decoded_bytes = list(map(int,str.split(decoded_bytes.strip("\r\n"),",")))
        decoded_bytes = ser_bytes.strip() # hiroyuki
        
        x.append(time.time())
        y.extend(decoded_bytes.split(","))

        c.append(time.time())
        c.extend(decoded_bytes.split(","))

        if len(c) == 2:
            c[1] = 0
            c.extend([0,0,0])
            
                       
        for i in range(5): # range(X):Xはチャンネル数
            c[i] = float(c[i]) # listをfloat形式に変換
 
        #c[1] = round(c[1]*0.1266-114.74,4)
        #c[2] = round(c[2]*0.1266-114.74,4)
        #c[3] = round(-(c[3]-204.6)/818.4*99-1,4)
        
        #print('c',c)
        
        #ser.close()
        return(x,y,c)
        
    def ArduinoDO(flag):
#        import serial
        #ser = serial.Serial('COM3',9600,timeout=1)
        #ser.flushInput()
        if flag==True:   
            ser.write(b'DO1H')
        else:
            ser.write(b'DO1L')
        #ser.close()
            
    def ArduinoAO(flag,values):
        #ser = serial.Serial('COM3',9600,timeout=1)
        #ser.flushInput()
        print(values)
        if flag == True:
        #import serial
            ser.write(b'AO6v200\n')
            ser.write(b'AO9v400\n')
            ser.write(b'AO10v600\n')
            ser.write(b'AO11v800\n')
        else:
            ser.write(b'AO6v0\n')
            ser.write(b'AO9v0\n')
            ser.write(b'AO10v0\n')
            ser.write(b'AO11v0\n')
        #print('AO6v1000')
        #ser.close()
