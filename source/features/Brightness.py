import speech_recognition as sr
import screen_brightness_control as sbc

from source.filex.Talk import Talk

r = sr.Recognizer()


def Brightness(audio_data):
    audio_data = audio_data.replace('brightness', '')
    try:
        audio_data = int(audio_data)
        sbc.set_brightness(audio_data)
        Talk(f'Brightness is now {str(sbc.get_brightness()[0])}')
    except:
        Talk('Please say a number, try again')
