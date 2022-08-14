from source.filex.Talk import Talk
from source.filex.GetCmd import GetCmd

def GetContent(audio_data):
    Talk(f'Please say the content for {audio_data}.txt...')
    file_content = GetCmd(f'Content for {audio_data}.txt')
    file_content = file_content.strip()

    if file_content != '':
        DumpContent(audio_data, file_content)
    else:
        Talk(f'Audio not clear for {audio_data}.txt, try again!')
        GetContent(audio_data)

def DumpContent(audio_data, file_content):
    with open(f'C:\\david\\{audio_data}.txt', 'a') as file_append:
        file_append.write(file_content)
        print(f'>> Your content was successfully dumped into \'{audio_data}.txt\'...\n')
        Talk(f'your content was successfully dumped into {audio_data}.txt...')

def CreateFile(audio_data):
    audio_data = audio_data.replace('create', '')
    audio_data = audio_data.strip()
    print(f'>> Creating \'{audio_data}.txt\'...')
    Talk(f'creating {audio_data}.txt')

    with open(f'C:\\david\\{audio_data}.txt', 'w') as file:
        audio_data = audio_data.strip()
        print(f'>> Successfully created \'{audio_data}.txt\'...\n')
        Talk(f'successfully created {audio_data}.txt...')

    GetContent(audio_data)