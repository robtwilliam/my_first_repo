import os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
words = os.getcwd() + '/words.txt'
with open(words, 'a') as word_file:
    word_file.write(f"Smithwicks is a great beer. 1337. The current time is {current_time} \n")