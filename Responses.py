from datetime import datetime


from datetime import datetime
from sqlite3 import Date


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey!, How's is it going?"

    if user_message in ("who are you?", "who are you?"):
        return "I'm am you Software Downloader."

    if user_message in ("time", "time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
        
    return "I didn't understand that. Try again"