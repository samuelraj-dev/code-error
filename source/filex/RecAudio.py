import speech_recognition as sr

from source.features.WebSearch import WebSearch
from source.features.PlayYT import PlayYT
from source.features.Brightness import Brightness
from source.features.ReadTime import ReadTime
from source.features.ReadDate import ReadDate
from source.features.Close import Close
from source.features.ReadFile import ReadFile
from source.features.CreateFile import CreateFile
from source.filex.Talk import Talk
from source.filex.GetCmd import GetCmd


r = sr.Recognizer()

# Main Function
def RunCmd():
    audio_data = GetCmd('Say Something...\n')

    if 'david' in audio_data:
        audio_data = audio_data.replace('david', '')
        audio_data = audio_data.strip()
        print(f'>> Command to be executed: {audio_data}\n')

        # Google Search
        if 'search' in audio_data:
            WebSearch(audio_data)     

        # Play YouTube
        elif 'play' in audio_data:
            PlayYT(audio_data)
        
        # Brightness
        elif 'brightness' in audio_data:
            Brightness(audio_data)

        # Time
        elif 'time' in audio_data:
            ReadTime()

        # Date
        elif 'date' in audio_data:
            ReadDate()

        # Read File
        elif 'read' in audio_data:
            ReadFile(audio_data)
        elif 'reid' in audio_data:
            ReadFile(audio_data)
        elif 'reed' in audio_data:
            ReadFile(audio_data)

        # Create File
        elif 'create' in audio_data:
            CreateFile(audio_data)

        # Close David
        elif 'exit' in audio_data:
            Close()

        else:
            audio_data = ''
            Talk('Sorry didn\'t get it')
            RunCmd()
    else:
        print(f'>> No \'david\' in command. so ignored...\n')