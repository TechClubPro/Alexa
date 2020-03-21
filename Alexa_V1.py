# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:29:02 2020

@author: TechClub
"""

""" Taking Text Input"""

import time
import pyttsx3

from PIL import Image 

im1=Image.open("images/CoronaSpread.jpg")
im2=Image.open("images/corona.jpg")

engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

print("Hello !! I am your assistant!!")
time.sleep(1)

while True:
# For Text"""
    
    question=input("You can ask me questions about Health and Hygine:")
    
    if "hands" in question or "Clean Hands" in question:
        print("You have to clean hands thoroughly by soap regularly")
        
    if "garbage" in question or "Garbage" in question:
        print("You have to keep seperate garbage bins for wet and dry seperately")
        
    if "sanitizer" in question or "Sanitizer" in question:
        print("Apply sanitizer to clean your hands , if soap and water is not available")
       
    
    """For Voice Output"""
    
    if "virus" in question or "Virus" in question:
        engine.say("Virus is an infective agent and it is able to multiply in living cells of host")
        engine.runAndWait() 
        
    if "antibiotics" in question or "Antibiotics" in question:
        engine.say("It is a medicine that inhibits the growth of or destroys microorganisms")
        engine.runAndWait() 
        
    if "corona" in question or "Bacteria" in question:
        engine.say("It is a deadly microorganism")
        engine.runAndWait()  
        
    if "covid" in question:
         im1.show()
            
    if "show" in question:
         im2.show()
        
    if "q" in question or "quit" in question:
        break

engine.say("I am Closing the application") 
engine.runAndWait()  
print("Closing..")
