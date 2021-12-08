import datetime
import webbrowser
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
         elif str(text).lower() == 'open youtube' :
            print("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            break
         elif  str(text).lower() == 'open google':
            print("Here you go to Google\n")
            webbrowser.open("google.com")
            break
         elif  str(text).lower() == 'news today':
            print("Here you go to NEWS\n")
            webbrowser.open("Twentyfournews.com")
              
              
             
            
        
                  
    
   
