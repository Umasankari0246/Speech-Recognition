
import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : ",text)
    except:
        print("Sorry could not recognize what you said")

# pip install SpeechRecognition
#pip install PyAudio
# py -3.12 -m pip install PyAudio
# py -3.12 -m pip install SpeechRecognition
# py -3.12 Speechrecognition.py