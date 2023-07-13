import speech_recognition as sr
import pyttsx3

# Create recognizer and engine objects
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function for voice recognition and response
def voice_assistant():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print("Recognized Text:", text)
        
        # Perform actions based on recognized text
        if "hello" in text:
            response = "Hello there!"
        elif "what is the time" in text:
            response = "The current time is 12:00 PM."
        else:
            response = "Sorry, I didn't understand that."
        
        # Convert response to speech
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the voice assistant function
voice_assistant()
