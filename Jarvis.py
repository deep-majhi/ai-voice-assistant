import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import wolframalpha
import json
import requests
from urllib.request import urlopen
import time

engine= pyttsx3.init()
wolframalpha_app_id= 'wolf fram alpha id will go here'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time= datetime.datetime.now().strftime("%H:%M:%S")
    speak('the time is')
    speak(Time)

def date_():
    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    date= datetime.datetime.now().day
    speak('the current date is ')
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak('Hi There Ben!')
    date_()
    time_()
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good afternoon')
    elif hour>=18 and hour<20:
        speak('Good evening')
    else:
        speak('Good Night')

    speak('Jarvis at your service..How can I help you')



def Take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
 
        print('Listening..')
        r.pause_threshold=1
        audio = r.listen(source)
 
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(query)
        speak( "You said"+query)
 
    except Exception as e:
        print(e)
        print('say it again')
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def screenshot():
    img= pyautogui.screenshot()
    img.save('C:/Users/Public/screenshot.png')
    speak('Screenshot taken')

def cpu():
    usage= str(psutil.cpu_percent())
    speak('CPU is at '+usage)
    battery= psutil.sensors_battery()
    speak(battery.percent)
  
def joke():
    speak(pyjokes.get_joke())

 
if __name__ == "__main__":
   
   wishme()
   
   while True:
 
       query = Take_command().lower()
 
       if 'time' in query:
           time_()
 
       elif 'date' in query:
           date_()

       elif 'wikipedia' in query:
           speak("Searching...")
           speak('What To search?')
           f=Take_command()
           query=query.replace('wikipedia',f)
           result=wikipedia.summary(query,sentences=6)
           speak('According to Wikipedia ')
           print(result)
           speak(result)
       elif 'send email' in query:
           try:

             speak("What should i speak? ")
             content= Take_command()
             speak("Who is the reciever? ")
             reciever= input('Enter Reciever: ')
             to= reciever
             sendEmail(to,content)
             speak(content)
             speak('Email has been sent..')

           except Exception as e:
               print(e)
               speak('Unable to send email')

       elif 'search in chrome' in query or 'chrome' in query:
           speak('What to search')
           search=Take_command().lower()
           wb.open('https://www.'+search+'.com/')
       
       elif 'search youtube' in query or 'youtube' in query:
           speak('What to search')
           search_term= Take_command().lower()
           speak('Here we go to youtube..')
           wb.open('https://www.youtube.com/results?search_query='+search_term)
       elif 'google' in query or 'search google' in query:
           speak('what should we search ')
           search_term= Take_command().lower()
           speak('Here we go to google..')
           wb.open('https://www.google.com/search?q='+search_term)
       elif 'cpu' in query:
           cpu()
       elif 'joke' in query:
           joke()                   
       elif 'go offline' in query:
           speak('Going Offline sir')
           quit()
       elif 'word' in query:
           speak('Opening MS Word')
           ms_word= r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010'
           os.startfile(ms_word)
       elif 'powerpoint' in query or 'presentation' in query:
           speak('Opening MS Powerpoint')
           ms_power= r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Powerpoint 2010'
           os.startfile(ms_power)
       elif 'excel' in query or 'worksheet' in query or 'stats' in query:
           speak('Opening MS Excel')
           ms_excel= r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Excel 2010'
           os.startfile(ms_excel)
       elif 'access' in query or 'database' in query:
           speak('Opening MS Access')
           ms_access= r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Access 2010'
           os.startfile(ms_access)
       elif 'outlook' in query:
           speak('Opening MS Outlook')
           ms_outlook= r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Outlook 2010'
           os.startfile(ms_outlook)
       elif 'notepad' in query:
           speak('Opening Notepad')
           notepad= r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad'
           os.startfile(notepad)
       elif 'paint' in query:
           speak('Opening Paint')
           paint= r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint'
           os.startfile(paint)
       elif 'telegram' in query:
           speak('Opening Telegram')
           telegram= r'C:\Users\YOGA 11E\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram'
           os.startfile(telegram)
       elif 'write a note' in query:
           speak('What should i write?')
           notes= Take_command()
           file= open('adi.txt','w')
           speak('Sir should I include Date and Time?')
           ans= Take_command()
           if 'yes' in ans or 'sure' in ans:
                strTime= datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes ')
           else:
               file.write(notes)
       elif 'screenshot' in query:
           screenshot()
       elif 'play music' in query:
           songs_dir= 'D:/Songs'
           music= os.listdir(songs_dir)
           speak('What should I play?')
           speak('select a number ...')
           ans=Take_command().lower()
           while('number' not in ans and ans != 'random' and ans !='you choose'):
               speak('could not understand please try again!')
               ans=Take_command().lower() 
           if 'number' in ans:
             no= int(ans.replace('number',' '))
           if 'random' or 'you choose' in ans:
               no=random.randint(1,100)
           os.startfile(os.path.join(songs_dir,music[no]))
       
       elif 'remember that' in query:
           speak('What should I remember?')
           memory= Take_command()
           speak('You asked me to remember that '+memory)
           remember= open('adi.txt','w')
           remember.write(memory)
           remember.close()

       elif 'do you remember anything' in query:
           remember= open('adi.txt','r')
           speak('You asked me to remember that '+remember.read())
       elif 'where is ' in query:
           query=query.replace("where is"," ")
           location= query
           speak('user asked to locate '+location)
           wb.open_new_tab('https://www.google.com/maps/search/'+location+'/@22.50477,88.3306153,12z/data=!3m1!4b1')
       elif 'calculate' in query:
           client= wolframalpha.client(wolframalpha_app_id)
           indx= query.lower().split().index('calculate')
           query= query.split()[indx +1:]
           res= client.query(' '.join(query))
           answer= next(res.results).text
           print('The answer is : '+answer)
           speak('The answer is : '+answer)
       elif 'news' in query:
           try:
               jsonObj= urlopen('https://www.thestatesman.com/')
               data= json.load(jsonObj)
               i=1
               speak('Here are the the top headlines of todays news')
               print('********TOP HEADLINES*******')
               for item in data['articles']:
                   print(str+'. '+item['title']+'\n')
                   print(item['description']+'\n')
                   speak(item['title'])
                   i+= 1
           except Exception as e:
               print(str(e))
       
       elif 'stop listening' in query:
           speak('For how many seconds')
           ans= int(Take_command())
           time.sleep(ans)
           print(ans)
       elif 'log out' in query:
           os.system('shutdown -1')

       elif 'restart' in query:
           os.system('shutdown /r /t 1')

       elif 'shutdown' in query:
           os.system('shutdown /s /t 1')
        
    