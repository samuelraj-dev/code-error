import os
from source.filex.Talk import Talk

NotFound = True

def ReadFile(audio_data):
    path = 'C:\\david'
    file_list = os.listdir(path)

    audio_data = audio_data.replace('read', '').replace('reed', '').replace('reid', '')
    audio_data = audio_data.strip()

    for file in file_list:
        if f'{audio_data}.txt' in file.lower():
            print(f'>> open file: {file}')
            Talk(f'opening {file}')
            select = f'{path}\\{file}'
            with open(select, 'r') as read_file:
                data = read_file.read()
                print(f'>> Content: {data}\n')
                Talk(data)
                global NotFound
                NotFound = False
                break
        else:
            pass

    if NotFound == True:
            Talk('File Not found!')