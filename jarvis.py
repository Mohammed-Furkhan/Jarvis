import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import comtypes.client
import distutils

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("good morning!")
        
    elif hour >=12 and hour <18:
        speak("good afternoon!") 

    else:
        speak("good evening!")

    speak("I am jarvis please tell  what may i help you ")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "none"
    return query

    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'hey jarvis' in query:
            speak('hello boss how may i help you')
            
        if 'who are you' in query:
            speak('Iam jarvis iam your personal assistance')
            
        if 'can you speak tamil' in query:
            speak('sorry! i dont know tamil')
            
        if 'can you speak telugu' in query:
            speak('sorry! i dont know telugu if you teach me i will learn ')
            
        if 'can you speak hindi' in query:
            speak('yes! i speak hindi , can i speak boss!')
            
        if 'yes you can' in query:
            speak('haan boll mere yaar')
            
        if 'who is captain cool' in query:
            speak('mahendra singh dhoni')
            
        if 'what are the things you can do' in query:
            speak('i will tell time, i will tell jokes for you , i will open youtube , i will open goole')
       
        if 'can you hear me' in query:
            speak('yes boss!')   
    
        if 'tell me a joke' in query:
            speak("This might make you laugh. How do robots eat guacamole?   With computer chips. hahahaha")
        
        if 'anothor one' in query:
            speak("What falls, but never needs a bandage? The rain.")    

        if 'one more' in query:
            speak("What month is the shortest of the year? May, it only has three letters.")

        
             
        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query =query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'weather' in query:
            webbrowser.open("https://www.msn.com/en-in/weather/hourlyforecast/in-Madhavaram,Tamil-Nadu?loc=eyJsIjoiTWFkaGF2YXJhbSIsInIiOiJUYW1pbCBOYWR1IiwiYyI6IkluZGlhIiwiaSI6IklOIiwiZyI6ImVuLWluIiwieCI6IjgwLjE4NDc1MzQxNzk2ODc1IiwieSI6IjEzLjE0MTQ3MjgxNjQ2NzI4NSJ9&weadegreetype=C&ocid=winp2fptaskbar&cvid=e3221e9fa69a4dbebaeb80541a73a727&fcsttab=temperature")
            
        elif 'ishq murshid song in youtube' in query:
            webbrowser.open('https://www.youtube.com/watch?v=HFHl_tXSyaE&pp=ygUQaXNocSBtdXJzaGlkIG9zdA%3D%3D')
         
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")  
            
        elif 'open netflix' in query:
            webbrowser.open("netflix.com") 

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")



        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play tum hi ho song' in query:
            webbrowser.open("https://open.spotify.com/search/tum hi ho")
            
        elif 'play mujhe peene do song' in query:
            webbrowser.open("https://open.spotify.com/search/mujhe%20peene%20do")

        elif 'play music' in query:
            music_dir = 'D:\\songs\\Favorite'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")


        
    
