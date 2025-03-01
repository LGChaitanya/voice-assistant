import time
import wolframalpha as wolframalpha
from  ecapture import ecapture as ec
import speech_recognition as sr
import webbrowser
import datetime
import win32com.client
import pyjokes
import requests

speaker=win32com.client.Dispatch("SAPI.SpVoice")
def say(text):
    speaker.Speak(text)
    print(f"Assistant: {text}")

def takeCommand():
    r = sr.Recognizer() #Creates an instance of Recognizer from the speech_recognition library.
    with sr.Microphone() as source:
        audio = r.listen(source)  #r.listen(source) records the user's voice until they stop speaking.
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in") # Uses Google Speech Recognition API (recognize_google()) to convert speech to text.
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

#
# def takeCommand():
#     print("Type query...")
#     query=input()
#     return query

if __name__ == '__main__':
    print('Welcome to Harya Assistant ')
    say("Harya's assistant")
    # print("Listening...")


    while True:
        print("Listening...")
        query = takeCommand()



        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
            time.sleep(3)

        #The first datetime refers to the module.
           #The second datetime refers to the class inside the module.


        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")  #string format time 
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} and {min} minutes")
            # print(f"Sir time is {hour} and {min} minutes")

        elif "Quit".lower() in query.lower():
            exit()

        elif 'how are you' in query or 'how r u' in query:
            say("I am fine, Thank you")
            say("How are you, Sir")

        elif 'fine' in query or "good" in query:
            say("It's good to know that your fine")

        elif "weather" in query:
            api_key = "669f75b81ab68aa7f72bbf4b516a81ea"
            base_url = "https://api.openweathermap.org/data/2.5/weather?q="
            say(" City name ")
            # print("City name : ")
            city_name = takeCommand()

            complete_url = base_url +city_name + "&appid=" +api_key
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))
                say(weather_description)

            else:
                say(" City Not Found ")

        elif 'joke' in query:
            say(pyjokes.get_joke())

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
            say("captured")

        elif "what is" in query or "who is" in query:

            question=query
            client = wolframalpha.Client("GKPJLA-L28EXQQRYL")
            res = client.query(question)

            try:
                print(next(res.results).text)
                say(next(res.results).text)
            except StopIteration:
                print("No results")

        else:
            print("Chatting...")
