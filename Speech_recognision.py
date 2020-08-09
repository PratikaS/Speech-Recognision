import speech_recognition as sr
import pyaudio
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio=r.listen(source)
    print("Time over!!! Thanks!!!")
    try:
        print("Text  "+r.recognize_google(audio))
    except:
        print("sorry didn't get this")
