import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import cv2
import random

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# print(voices[1].id)

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else: 
        speak("Good evening")
    
    speak("Hello Anushka! I am Jarvis, how can i help you")

def takeCommand():
    # it takes microphone input from and the user and produces string text output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        print(e)

        print("I can't understand you, please say that again...")
        return "None"
    return query 

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        # logic for executing tasks based on queryy

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")

        elif 'open moodle' in query:
            webbrowser.open("http://120.72.92.242:8080/moodle/my/")

        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/") 

        elif 'play music' in query :
            music_dir = 'C:\\Users\\Anushka\\Desktop\\songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd)

        elif 'open chrome' in query:
            chromepath = "C:\\Users\\Anushka\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open visual code' in query:
            vspath ="C:\\Users\\Anushka\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)
        
        elif 'open atom' in query:
            atompath ="C:\\Users\\Anushka\\AppData\\Local\\atom\\atom.exe"
            os.startfile(atompath)
        
        elif 'open kali' in query:
            vmpath ="C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(vmpath)

        elif 'open notepad' in query:
            notepath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(notepath)

        elif 'open adobe reader' in query:
            adbrpath = "C:\\Program Files (x86)\\Adobe\\Reader 9.0\\Reader\\AcroRd32.exe"
            os.startfile(adbrpath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")


        elif  'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()


     # do this for sending email
    def sendEmail(to, conten):
      elif 'send mail to mamma' in query:
            try:
                speak('What should I say ?')
                content = takecommand()
                to = "aranushka2019@gmail.com"
                sendemail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry I was unable to send the mail") 
                
    



        



        




        
       

          

        














