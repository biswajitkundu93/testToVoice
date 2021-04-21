from gtts import gTTS
import os

text = input("Enter whatever you want...")

voice = gTTS(text=text,lang='en')
file_name ="voice.mp3"
voice.save("Test to voice/"+file_name)
os.system('vlc '+file_name)
