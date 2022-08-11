from pynput.keyboard import Key, Controller

from source.filex.Talk import Talk
from source.filex.GetCmd import GetCmd


keyboard = Controller()

def PressSpace():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    CtrlYT()

def PressM():
    keyboard.press('m')
    keyboard.release('m')
    CtrlYT()

def CtrlW():
    Talk('closing video')
    keyboard.press(Key.ctrl.value)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl.value)

def CtrlYT():
    yt_cmd = GetCmd('Say yt command...')

    # Pause & Play
    if 'pause video' in yt_cmd:
        PressSpace()
    elif 'boss video' in yt_cmd:
        PressSpace()
    elif 'resume video' in yt_cmd:
        PressSpace()
    elif 'play video' in yt_cmd:
        PressSpace()
    
    # Mute & Unmute
    elif 'unmute video' in yt_cmd:
        PressM()
    elif 'mute video' in yt_cmd:
        PressM()

    # Exit Video
    elif 'close video' in yt_cmd:
        CtrlW()
        pass

    else:
        CtrlYT()