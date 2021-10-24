#!/usr/bin/python3
# -*- coding: utf-8 -*-
import serial  # sudo pip install pyserial should work
import datetime

serial_port = '/dev/ttyUSB0';

ID = "";

baud_rate = 9600;
ser = serial.Serial(serial_port, baud_rate)
flag = True
flag2 = True
time = ""
iden = ""
try:
    while True:
        if True:
            with open("/home/pi/Desktop/PitttChallengeVersion 2/patientID.data","r") as patID:
                redInd = patID.read()
                parsed = redInd.split(" ",1)
                parsed = parsed[1]
                #print(parsed)
                
                #iden = parsed[1]
                time = parsed[1:]
                #print(time)
                patID.close()        
        ID = ser.readline();
        ID = ID.decode("utf-8")
        ID = ID.replace("ID ", "")
        ID = ID.replace(" ", "")
        ID = ID.strip()
        #print(ID);
        
        if(ID!=""):
            with open("/home/pi/Desktop/PitttChallengeVersion 2/patientID.data","w") as patID:
                writeString = ID+" " + time
                print("\nPatient Detected! Updating Record View:")
                print("ID: "+ ID+" Time Records:" + time)
                redInd = patID.write(writeString) 
                patID.close()
            #if(flag ==True):
                      
            #if (flag2 == True):
            #    ID=""
            #    pill = "/n Pill taken at" +  str(datetime.datetime.now())
  
except:
    print ("The program has terminated unexpectedly due to errors")


