import speech_recognition as sr
import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand")
        return ""

def process_command(command):
    if "send" in command:
        speak("Processing your payment")
        print("Simulated Transaction Successful")
        speak("Transaction successful")
    else:
        speak("Command not recognized")

# Run
speak("Welcome to Voice UPI System")
command = listen()
process_command(command)
