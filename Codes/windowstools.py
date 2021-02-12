#This code is a try to bring for operational system Windows, some tools from "xdotools" from Linux distribuitions.

#Name: Vitor de Almeida Recoaro.
#Date: 12/02/2021.
#Version: 1.0.
#Updates:
#    - 1.0: Created a function to shutdown the computer in determined horary.


#Function to shutdown the computer in determined horary, the horary is like "0:30"
import os
import sys
from datetime import datetime, date

def shutdown(sht_horary):
    str(sht_horary)
    if(len(sht_horary)>5 or len(sht_horary)<4 or sht_horary.find(":")==-1):
        print("ERROR - Invalid time argument")
    else:
        sht_horary = sht_horary.split(":")
        hour = int(sht_horary[0])
        minutes = int(sht_horary[1])
        if(hour>=24 or hour<0 or minutes>=60 or minutes<0):
            print("ERROR - Invalid time argument")
        else:
            #Cancel the system shutdown
            os.system("shutdown -a")
            os.system("cls")
            #Get the current horary from computer
            horary = datetime.now()
            # If the shutdown horary is bigger than current hour, so the computer just will shutdown in an another day
            if(hour<horary.hour):
                sht_horary = datetime(horary.year,horary.month,horary.day+1,hour,minutes,0,0)
            else:
                sht_horary = datetime(horary.year,horary.month,horary.day,hour,minutes,0,0)
            dif_seconds = (sht_horary - horary).seconds
            print("Your computer will be shutdown on: "+ str(sht_horary)+"\nWARNING!!\nSAVE ALL YOUR WORKS")
            os.system("shutdown -s -t "+ str(dif_seconds))

def main():
    arguments = sys.argv
    #If user don't use any arguments, the "help" option will appear
    if(len(sys.argv)==1):
        print("To use this command you can use this arguments:")
        print("shutdown - The computer will be turned off in the horary that you specified. Exemple: shutdown 11:30")
    elif(str(arguments[1])=="shutdown"):
        shutdown(str(arguments[2]))

main()