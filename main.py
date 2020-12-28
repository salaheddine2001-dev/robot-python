from tkinter import *
from tkinter import ttk
import  os
import time
import playsound
import random
import speech_recognition as sr
from gtts import gTTS

def listen_user():
  rec=sr.Recognizer()
  with sr.Microphone() as source:
    rec.adjust_for_ambient_noise(source,duration=1)
    print("mr robot is listening")
    
    audio=rec.listen(source,phrase_time_limit=2)
  try:
    text=rec.recognize_google(audio,language='en-US')
     
    return text
  except:
    text="sorry i have a proplem"
    print("sorry i have a proplem")
    return text

def talk(text,file):
  tts=gTTS(text,lang="en")
  
  filename="%s.mp3"%file
  tts.save(filename)
  playsound.playsound(filename,True)
  os.remove(filename)
  



  
welcom=["hello","hi","hi eliza robot","hey"]
robotwelcom=["hey","hello","how are you","hello my name is eliza robot","hello salah"]
howareyou=["how are you","are you fine"]
howareyourobot=["fine","hi","I am fine and you","not fine","eliza robot not fine I am sad"]
wname=["your name","name please","what is your name"]
namerobot="my name is eliza robot made by salah"
probleme=["sorry I do not understand","I can not answer","Are you kidding me? I don't get you","Say hello first","Say hello at least","I do not want to talk now"]


def contact():
  while True:
      result = time.localtime(1545925769)
      
      de=random.randint(1,30000)
      choi=random.choice(robotwelcom)
      prob=random.choice(probleme)
      how=random.choice(howareyourobot)
      text_returnd=listen_user()
      if text_returnd in welcom:
        print(choi)

        talk(choi,de+result.tm_year+result.tm_mday+result.tm_hour+result.tm_min+result.tm_sec)
        time.sleep(2)
      elif text_returnd in wname:
        print(namerobot)
        talk(namerobot,de+result.tm_year+result.tm_mday+result.tm_hour+result.tm_min+result.tm_sec) 
        time.sleep(2)
      elif text_returnd in howareyou:
        print(how)
        talk(how,de+result.tm_year+result.tm_mday+result.tm_hour+result.tm_min+result.tm_sec) 
        time.sleep(2)
      else:
        print("sorry I do not understand")

        talk(prob,de+result.tm_year+result.tm_mday+result.tm_hour+result.tm_min+result.tm_sec)
        time.sleep(2) 
        
        

   
      
     
root = Tk()

root.title("eliza robot")
root.geometry("520x600")
root.resizable(False,False)
image =PhotoImage(file="as.gif")
Label(root, image=image).place(x=0,y=0)

ttk.Button(root,text="start Talk with me",command=lambda:contact()).grid(column=0,row=0,padx=40,pady=15,ipadx=2,ipady=2)
root.mainloop()