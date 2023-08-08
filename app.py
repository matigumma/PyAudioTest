from gtts import gTTS
from playsound import playsound


lang="es"

text="hola bonito como estas hoy?, ya compraste el huevo de chocolate para jazmin?"

speech = gTTS(text=text, lang=lang, slow=False)

speech.save("audio.mp3")

playsound("audio.mp3")
