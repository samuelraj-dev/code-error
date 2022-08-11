import pywhatkit

from source.filex.CtrlYT import CtrlYT
from source.filex.Talk import Talk

def PlayYT(audio_data):
    video = audio_data.replace('play', '')
    Talk(f'playing {video}')
    pywhatkit.playonyt(video)
    CtrlYT()