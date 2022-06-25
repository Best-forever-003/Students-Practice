from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'

spp = gTTS(text= "Hi Pycharm",lang=language, slow=False)

spp.save(audio)
playsound(audio)