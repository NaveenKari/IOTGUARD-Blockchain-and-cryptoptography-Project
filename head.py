import ECDSA as e
import datetime
import math
import random as r


def Head(T,reqId,time,ID,H,M):
    curTime=datetime.datetime.now()
    preTimeH=curTime.hour
    preTimeM=curTime.minute
    deltaT=5
    if preTimeH==H:
        diff=preTimeM-M
    elif preTimeH-H==1:
        diff=preTimeM-M
    else: 
        print("request expired")
    if diff>deltaT:
        print("request expired")
    else:
        #Ts=reqId|time
        #T1=str(curTime.hour)+str(curTime.minute)
        #T1=int(time)
        CKpub=e.generateKey()
        return CKpub   
