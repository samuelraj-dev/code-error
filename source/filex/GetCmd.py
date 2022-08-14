import speech_recognition as sr

from source.filex.Talk import Talk

r = sr.Recognizer()


def GetCmd(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(f'>> {ask}')
        r.adjust_for_ambient_noise(source)
        r.pause_threshhold = 1

        try:
            audio = r.listen(source)
            audio_data = r.recognize_google(audio)
            audio_data = audio_data.lower()
            print(f'>> User Said: {audio_data}')
            return audio_data

        except sr.UnknownValueError:
            audio_data = ''
            Talk('Your audio wasn\'t clear, please try again')
            return audio_data

        except sr.RequestError:
            audio_data = ''
            Talk('Application error!')
            return audio_data