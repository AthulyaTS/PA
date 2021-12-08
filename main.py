import datetime
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("listening...")
    while True:
         audio = r.listen(source)
         text = r.recognize_google(audio)
         if str(text).lower() == 'what is the time now':
             print(text)
             print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
             break
              
             
            
        
                  
    
   
