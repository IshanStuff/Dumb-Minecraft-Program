import os
import sys
import random
from playsound import playsound
import time
#module for locating images on screen
import pyautogui
#this is a basic program pls don't @ me, I suck at coding
#copy paste the path of the folder where you put the mp3 files,like the one below
path="D:\\Insults\\"
files=os.listdir(path)
#Function that checks if the respawn button is present on the screen
while True:
#save a picture of the respawn button as a png in this program's folder and pass it's name as a parameter
        c=pyautogui.locateOnScreen('respawn.png')
        #if c is not nothing, meaning that the button is present,play a random audio
        if(c is not None):
            #randomimizing the audio files the specified path
            d=random.choice(files)
            playsound("D:\\Insults\\" + d)
            time.sleep(2)
         #if c is nothing, it'll just pass and not play anything
        elif(c is None):
                pass       
    
    
    

    
