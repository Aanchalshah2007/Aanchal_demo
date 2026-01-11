from dotenv import load_dotenv
load_dotenv()

import speech_recognition as sr #ALlows jarvis to listen to your voice using the microphone
import webbrowser #Allows jarvis to open websites(Google)
import pyttsx4 #Allows jarvis to speak using text-to-speech
import time
import musiclib
import requests
import os
from client import ai_response


r = sr.Recognizer() #This creates a recognize  #object that can convert speech to text
engine = pyttsx4.init() #This starts the TTS engine, which converts text into spoken audio

newsapi = os.getenv("NEWS_API_KEY")


#This function makes jarvis talk
def speak(text):
    engine.say(text) #looks the text into the speech engine
    engine.runAndWait() #actually speaks the text out loud

    

def processCommand(c):
    print("Command Received:",c)

    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        song = " ".join(song.split())  # remove extra spaces

        print("Song:", song)

        found = False
        for key in musiclib.music:
            if key in song or song in key:  # flexible match
                webbrowser.open(musiclib.music[key])
                found = True
                break

        if not found:
            print("Song not found in library:", song)


    elif ("news") in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        data = r.json()

# Check if request succeeded
        if data["status"] == "ok":
            articles = data["articles"]

            print("Top Headlines:\n")
            for i, article in enumerate(articles[:10]):
                print(f"{i+1}. {article['title']}")  # print first 10 headlines
                speak(f"{i+1}. {article['title']}")
        else:
            print("Error:", data)

#Let genAI handle the request
    else:
        output = ai_response(c)
        print(output)
        speak(output)
        




#This part only runs when you run this file directly. If you import this file in another file, It will not automatically execute the speak line
#WHy do we use if__name__=="__main__"
#BEcause it protects code from running automatically when imported.
if __name__=="__main__":
    speak("Initializing Jarvis...........")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from the microphone
        
        
        print("recognizing")
        #recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4,phrase_time_limit=1)
            word = r.recognize_google(audio)
            print("Heard:",word)

            #Wake word detected
            if "jarvis" in word.lower():
                speak("Ya")
                time.sleep(0.5)
                
                 #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                
                command = r.recognize_google(audio)
                processCommand(command)

        except sr.UnknownValueError:
            print("Sphinx could not understand audio")

        except Exception as e:
            print("Error;{0}".format(e))tand audio")

        except Exception as e:
            print("Error;{0}".format(e))
