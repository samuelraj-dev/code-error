from datetime import datetime

from source.filex.Talk import Talk

def ReadTime():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    Talk(f"Its {time}")