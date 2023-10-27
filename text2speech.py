from gtts import gTTS


language ="en"
text= "Hello world ,mai ekk chutiya hun"


speech = gTTS(text=text, lang=language, slow=True, tld="com.au")

speech.save("textToSpeech.mp3")
