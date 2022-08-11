import pyttsx3


engine = pyttsx3.init()

def Talk(text):
    engine.say(text)
    engine.runAndWait()