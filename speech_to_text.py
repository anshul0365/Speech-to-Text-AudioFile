import speech_recognition as sr
r = sr.Recognizer()

a_file = 'abc.wav'

with sr.AudioFile(a_file) as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
 
try:
    text = r.recognize_google(audio)
    print(text)
    
    
except Exception as e:
    print (e)
