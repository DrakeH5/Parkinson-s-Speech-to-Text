import speech_recognition as sr

r = sr.Recognizer()

from pynput.keyboard import Controller

keyboard  = Controller()


while(1):
    with sr.Microphone() as source:
        audio_text = r.listen(source)
        words = r.recognize_google(audio_text) + " "
        print(words)
        for x in range(len(words)):
            for y in words[x]:
                keyboard.press(y)
                keyboard.release(y)

        words = []