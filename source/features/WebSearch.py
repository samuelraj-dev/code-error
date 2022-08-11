import pywhatkit

from source.filex.Talk import Talk

def WebSearch(audio_data):
    audio_data = audio_data.replace('search', '')
    Talk(f'searching {audio_data}')
    pywhatkit.search(audio_data)