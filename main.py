
import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
from openai import OpenAI
from config import apikey

#SETUP 
engine = pyttsx3.init()
client = OpenAI(api_key=apikey)

chatStr = ""

#SPEAK FUNCTION
def say(text):
    engine.say(text)
    engine.runAndWait()

#CHAT FUNCTION
def chat(query):
    global chatStr
    print(chatStr)

    chatStr += f"User: {query}\nJarvis: "

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
            {"role": "user", "content": chatStr}
        ]
    )

    reply = response.choices[0].message.content

    say(reply)

    chatStr += f"{reply}\n"
    return reply

#AI-FUNCTION
def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt}\n*************************\n\n"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text += response.choices[0].message.content

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    filename = f"Openai/{prompt[:30].replace(' ', '_')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

#SPEECH RECOGNITION
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return str(query)

        except Exception:
            return ""

#MAIN-PROGRAM
if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis AI started")

    while True:
        query = takeCommand()

        if not query:
            continue

        query = query.lower()

        #WEBSITES
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"]
        ]

        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        #COMMANDS
        if "open music" in query:
            os.system("start music.mp3")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Time is {hour} {minute}")

        elif "open facetime" in query:
            os.system("start facetime")

        elif "open pass" in query:
            os.system("start passky")

        elif "using artificial intelligence" in query:
            ai(prompt=query)

        elif "jarvis quit" in query:
            say("Goodbye")
            exit()

        elif "reset chat" in query:
            chatStr = ""

        else:
            chat(query)
