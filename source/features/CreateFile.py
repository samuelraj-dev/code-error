from source.filex.Talk import Talk

def CreateFile(audio_data):
    audio_data = audio_data.replace('create', '')
    print(f'>> dumping into file.txt: {audio_data}')

    with open(f'C:\\david\\file.txt', 'w') as file:
        audio_data = audio_data.strip()
        file.write(audio_data)
        print('>> successfully created the file...\n')
        Talk('>> successfully created the file...')