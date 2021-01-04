import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("i am jarvish sir. please tell me how may i help you")

def takecommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smnpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('eleemthapa10@gmail.com', '9803026221')
    server.sendmail('eleemthapa10@gmail.com', to,content)
    server.close()

if __name__== "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=15)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open kickassanime' in query:
            webbrowser.open("kickassanime.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files (x86)\\Nepali Calendar\\Nepali Calendar.exe"
            os.startfile(codePath)
        elif 'open zoom' in query:
            coderun = "C:\\Users\\reeju\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(coderun)
        elif 'open powerpoint' in query:
            codedown = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codedown)
        elif 'email to eleem' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "eleemthapa10@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend eleem. i am not able to send this email")





        


   