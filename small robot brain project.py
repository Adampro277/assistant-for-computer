import turtle
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
from playsound import playsound
from PIL import Image
# === Initialize TTS ===
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

# === Create Fullscreen Turtle Window ===
screen = turtle.Screen()
screen.title("Voice Assistant")
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")

# === Draw Welcome Background ===
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("cyan")

# Draw a border
t.penup()
t.goto(-600, 300)
t.pendown()
for _ in range(2):
    t.forward(1200)
    t.right(90)
    t.forward(600)
    t.right(90)

# Write welcome text
t.penup()
t.goto(0, 0)
t.color("white")
t.write("WELCOME TO YOUR ASSISTANT", align="center", font=("Arial", 28, "bold"))

# Add a circle as button visual
t.goto(0, -100)
t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()

t.goto(0, -120)
t.color("black")
t.write("Say Something", align="center", font=("Arial", 14, "bold"))

# === Assistant Logic ===
def start_assistant():
    speak("Hello! I am your turtle assistant.")
    while True:
        query = listen()

        if 'time' in query:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")
        elif 'natural' in query:
            img = Image.open("sdsdsd.jpg")
            img.show()
            playsound("spring-forest-nature-337004.mp3")
        elif 'who am i' in query:
            speak("Adam")
        elif 'mustafa' in query:
            webbrowser.open("https://www.youtube.com/@MustafaGO/videos")
        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'date' in query:
            today = datetime.datetime.now().strftime("%A, %B %d")
            speak(f"Today is {today}")
        elif 'google' in query:
            speak("What should I search for?")
            search_query = listen()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif 'joke' in query:
            speak("Why don't scientists trust atoms? Because they make up everything!")
        elif 'wiki' in query:
            speak("What topic?")
            topic = listen()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except:
                speak("Sorry, I couldn't find that.")
        elif 'stop' in query or 'exit' in query:
            speak("Goodbye!")
            quit()
            break

# === Start on spacebar press ===
def on_space():
    start_assistant()

screen.listen()
screen.onkey(on_space, "space")

turtle.done()
def main():
  if __name__ == "__main__":
    main()