import time
from source.filex.Talk import Talk
from source.filex.RecAudio import RunCmd


if __name__ == '__main__':
    Talk('Initialization complete! Welcome!')
    while 1:
        RunCmd()
        time.sleep(1)