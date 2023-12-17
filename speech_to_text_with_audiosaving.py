import speech_recognition as sr
r = sr.Recognizer()
text = ''
file = open('C://logic 360//speech_text.txt','w')
count = 0
with sr.Microphone() as source:
    while('end' not in text):
        print('audio rec started.....')
        audio = r.record(source,duration=5)
        f = open("C://logic 360//microphone-results"+str(count)+".wav", "wb")
        f.write(audio.get_wav_data())
        f.close()
        print(audio)
        print('audio recorded.....')
        count += 1
        try:
            text = r.recognize_google(audio)
            print(text)
            file.write(text)
        except:
            print('please talk something')
        file.write('\n')


file.close()
