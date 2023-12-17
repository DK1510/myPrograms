import speech_recognition as sr
import time
r = sr.Recognizer()
text = ''
count = 0
with sr.Microphone() as source:
    while True:
        if 'end' in text:
            break
        print('recording started......')
        audio = r.record(source,duration=5) #record audio for 5sec
        f = open('audio_rec'+str(count)+'.wav','wb')
        count+=1
        f.write(audio.get_wav_data())
        f.close()
        print('recorded......')
        try:
            text = r.recognize_google(audio)#recognize speech and convert to text using google
            f = open('Speech_text.txt','a+')
            f.write(text)
            f.close()
        except:
            print('something went wrong....')
        print(text)
        time.sleep(2)

