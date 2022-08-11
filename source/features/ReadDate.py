from datetime import datetime

from source.filex.Talk import Talk

def ReadDate():
    now = datetime.now()
    date = now.strftime('%A %d %B, %Y')
    Talk(f"Its {date}")