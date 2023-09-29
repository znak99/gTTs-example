from gtts import gTTS
import sys

language_config = sys.argv[1]
text = sys.argv[2]

if language_config == "en" or language_config == "ja" or language_config == "ko":
    if text != "":
        speech = gTTS(text=text, lang=language_config, slow=False)
        speech.save("tts_example.mp3")
    else:
        print("text blank error")
else:
    print(f"lang code error: {language_config}")


