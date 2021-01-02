# importing  package 
from tkinter import *
from win32com.client import Dispatch 
from tkinter import ttk
import threading
import time
import os
import datetime
import requests
import playsound
import random
import speech_recognition as sr
from gtts import gTTS
import winsound


#variables and arrays
news=["BBC news","news","Give me the latest news","the latest news","latest news","Give me the latest news, please","the latest news, please","latest news, please","the Top news, please","Top news, please","top news in the world"]
good=["nice","good","tanks","tanks you","wow","ok","okey"]
bye=['Bye', 'bye', 'Goodbye', 'goodbye', 'Good bye' 'good bye', 'byebye', 'by by', 'By by', 'exit', 'close', 'So long', 'so long', 'okay bye', 'ok bye', 'Ok bye', 'Okay bye']
goodar=["yeah nice","yeah good and nice","tanks","tanks you","wow tanks","ok tanks","okey tanks you verry much"]
weather=["weather","coord","Weather condition","weather prediction","Please, what is the weather forecast for tomorrow","Please, weather"]
welcom=["hello","hi","hi eliza robot","hey", 'Hi', 'Hello', 'hello', 'Hey', 'hey', 'yo','salam','Salam']
robotwelcom=["hey","hello","how are you","hello my name is eliza robot","hello salah", 'Hi', 'Hello', 'hello', 'Hey', 'hey', 'salam', 'Salam']
howareyou=["how are you","are you fine"]
howareyourobot=["fine","I am fine and you","not fine","eliza robot not fine I am sad"]
wname=["your name","name please","what is your name","Who are you", 'Your name', 'What are you','what are you']
wtime=["time","what is the time now","what is the time","time please","hour","clock","clock please","what time is it"]
wdate=["dite","dete","dyte","what is the date today","what is the date","date please","dyte please","date","today date","today dite","today dyte","dite please","what date is it"]
nameoftoday=datetime.datetime.now().strftime("%A")
year=datetime.datetime.now().year
alldate=datetime.datetime.now().strftime("%x")
todayor="today is {} in year {} and complete date is {}".format(nameoftoday,year,alldate)
namerobot="my name is eliza robot made by salah"
probleme=["sorry I do not understand","I can not answer","Are you kidding me? I don't get you","Say hello first","Say hello at least","I do not want to talk now"]
nottalk="Why don't you talk to me, my friend"



def NewsFromBBC(): 
      
    # BBC news api 
    main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=e6c268c6206648e38d4a511cc701e33a"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
        
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, results[i]) 
        
        print("_"*50)
        speak = Dispatch("SAPI.Spvoice")
        speak.Speak(results[i])
        time.sleep(2)
#listen user function for listen sound
def listen_user():
  rec=sr.Recognizer()
  with sr.Microphone() as source:
    rec.adjust_for_ambient_noise(source,duration=1)
    winsound.Beep(frequency = 2500, duration = 100)
    print("robot is listening")
    
    audio=rec.listen(source,phrase_time_limit=4)
  try:
    text=rec.recognize_google(audio,language='en-US')
     
    return text
  except:
    
    return nottalk


#talk  function for make talk sound
def talk(text,file):
  tts=gTTS(text,lang="en")
  
  filename="%s.mp3"%file
  tts.save(filename)
  playsound.playsound(filename,True)

  os.remove(filename)




  

#contact  function for  talk with user
def contact():
  while True:
      
      
      global root
      result = time.localtime(1545925769)
      de=random.randint(1,300000000)
      countertime=de+result.tm_year+result.tm_mday+result.tm_hour+result.tm_min+result.tm_sec


      alltime=datetime.datetime.now().strftime("%X")
      timeor="time is {}".format(alltime)

      
      choi=random.choice(robotwelcom)
      prob=random.choice(probleme)
      how=random.choice(howareyourobot)
      go=random.choice(goodar)
      byerb=random.choice(bye)

      

  

      text_returnd=listen_user()

      if text_returnd in welcom:
        print(choi)
        talk(choi,countertime)
        
      


      elif text_returnd in wname:
        print(namerobot)
        talk(namerobot,countertime)
      


      elif text_returnd in news:
        
        talk("ok",countertime)
        time.sleep(1)
        NewsFromBBC()
        
      

      elif text_returnd in good:
        print(go)
        talk(go,countertime)
      


      elif text_returnd in bye:
        print(byerb)
        talk(byerb,countertime)
        time.sleep(1)
        exit()
        
  

        



      

      elif text_returnd == nottalk:
        print(nottalk)
        talk(nottalk,countertime)



      elif text_returnd in weather:
        talk("Well, the weather for any city",countertime)
        randomw=random.randint(1,30000)
        try:
          city=listen_user()
          api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
          url = api_address + city
          json_data = requests.get(url).json()
          format_add = json_data['weather'][0]['description']
          wrrd="Weather in a city {} it will be {}".format(city,format_add)
          talk(wrrd,randomw)
          time.sleep(2)

          
        except:
          print('Sorry, I dont know right now. Make sure to connect to the internet')
          talk('Sorry, I dont know right now. Make sure to connect to the internet',randomw)
      




      elif text_returnd in howareyou:
        print(how)
        talk(how,countertime) 
        


      elif text_returnd in wtime:
        print(timeor)
        talk(timeor,countertime) 
        


      elif text_returnd in wdate:
        print(todayor)
        talk(todayor,countertime) 

      
   


      else:
        print(prob)
        talk(prob,countertime)
      
      
      time.sleep(3)



root = Tk()

img="A.gif"
root.title("eliza robot")
root.geometry("420x220")
root.resizable(False,False)
image =PhotoImage(file=img)
Label(root, image=image).place(x=0,y=0)

threading.Thread(target=contact).start()



root.mainloop()

