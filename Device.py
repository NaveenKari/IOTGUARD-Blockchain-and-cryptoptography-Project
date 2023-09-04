import ECDSA as e
import datetime
import MineBlock as p
import IoTid_check as c
import location as l
import math
import random as r
import head as h


def Device():
    print("Select one of the below options")
    print("1.Enroll Device")
    print("2.Communicate")
    option=int(input())
    if option==1:
        ip=input()
        
        d=l.checkLocation(ip)
        if d>=0:
            p.Mine()
            AM=c.deviceid
            with open('blockData.txt', 'w') as f:
                f.write(str(AM))
            print("Block Enrolled Successfully") 
        else:
            print("Incorrect ip-address or Device Out of Range")       
    else:
        with open('blockData.txt', 'r') as f:
            for line in f:
                ID=line.strip()
        if c.checkId(ID):
            ip=input()
            d=l.checkLocation(ip)
            if d>=0:
                print("Authentication Successful")
                n1=math.floor(r.random()*100)
                Id=ID
                my_bytes = ID.encode('utf-8')
                my_bytearray = bytearray(my_bytes)
                ID=my_bytearray
                n1=n1.to_bytes(len(ID), byteorder='big')

                reqId = bytes([b1 ^ b2 for b1, b2 in zip(ID, n1)])


                curTime=datetime.datetime.now()
                H=curTime.hour
                M=curTime.minute
                time=str(curTime.hour)+str(curTime.minute)
                time=int(time)
                time1=str(time)
                time=time.to_bytes(len(reqId), byteorder='big')

                reqId= bytearray(reqId)
                time = bytearray(time)

                # Perform bitwise OR operation on the two bytearray objects
                T = bytes(reqId[i] | time[i] for i in range(len(reqId)))
                pk,prk=h.Head(T,reqId,time1,Id,H,M)    
                e.ecdsa(pk,prk)
            else:
                print("Device Out Of Range")
        else:
            print("Deviece not Enrolled")        
Device()
        


    
    