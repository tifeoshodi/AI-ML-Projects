'''
import speech_recognition as sr

# Define the enrolled voice pattern
enrolled_voice = "God is good"

# Initialize the recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak to authenticate...")

    # Adjust for ambient noise levels
    r.adjust_for_ambient_noise(source)

    # Capture the audio
    audio = r.listen(source)

    try:
        # Recognize speech using the Google Speech Recognition API
        text = r.recognize_google(audio)
        print("You said:", text)

        # Check if the recognized speech matches the enrolled voice pattern
        if text.lower() == enrolled_voice.lower():
            print("Authentication successful!")
        else:
            print("Authentication failed!")

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")

    except sr.RequestError as e:
        print("Sorry, an error occurred during speech recognition:", str(e))

'''

'''
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the voice rate (speed)
engine.setProperty('rate', 150)

# Set the voice volume (optional)
engine.setProperty('volume', 0.8)

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")

    # Adjust for ambient noise levels
    r.adjust_for_ambient_noise(source)

    # Capture the audio
    audio = r.listen(source)

    try:
        # Recognize speech using the Google Speech Recognition API
        text = r.recognize_google(audio)
        print("You said:", text)

        # Check if the recognized speech matches the enrolled voice pattern
        if text.lower() == enrolled_voice.lower():
            print("Authentication successful!")
            response_text = "Authentication successful!"
        else:
            print("Authentication failed!")
            response_text = "Authentication failed!"

        # Convert response text to speech
        engine.say(response_text)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")

    except sr.RequestError as e:
        print("Sorry, an error occurred during speech recognition:", str(e))

'''

import speech_recognition as sr
import pyttsx3

# Get the secret question and answer from the user
user = input("Create username: ")
sq = str(input("Enter your Secret question: "))
ans = str(input("Enter your Secret Answer: "))

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the voice rate (speed)
engine.setProperty('rate', 150)

# Set the voice volume (optional)
engine.setProperty('volume', 0.8)

while True:
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Adjust for ambient noise levels
        r.adjust_for_ambient_noise(source)

        # Capture the audio
        #audio = r.listen(source)

        # Ask for the secret question
        greet= "Hello"
        form_1 = ("What's your secret question?")
        engine.say(greet)
        engine.say(user)
        engine.say(form_1)
        engine.runAndWait()

        # Capture the audio
        print("Listening...")
        audio = r.listen(source)

        # Recognize speech using the Google Speech Recognition API
        text = r.recognize_google(audio)
        
        # Validate the secret question
        if text = sq:
            error= "Incorrect question...try again"
            engine.say(error)
            engine.runAndWait()
            
            
        else:
            continue

        # Ask for the secret answer
        form_2 = "What's the secret answer? "
        engine.say(form_2)
        engine.runAndWait()
        
        # Capture the audio
        print("Listening...")
        audio = r.listen(source)

        # Recognize speech using the Google Speech Recognition API
        text = r.recognize_google(audio)

        # Validate the secret answer
        if text != ans:
            error = "Incorrect answer...retry"
            engine.say(error)
            engine.runAndWait()

        else:
            continue

        #print("Listening...")

        try:
            # Recognize speech using the Google Speech Recognition API
            text = r.recognize_google(audio)

            # Check if the recognized speech matches the enrolled voice pattern
            if text.lower() == ans.lower():
                print("Authentication successful!")
                response_text = "Authentication successful!"
            else:
                print("Authentication failed!")
                response_text = "Authentication failed!"

            # Convert response text to speech
            engine.say(response_text)
            engine.runAndWait()

        except sr.UnknownValueError:
            error = "Sorry, I could not understand your speech."
            
        except sr.RequestError as e:
            error = "Sorry, an error occurred during speech recognition:", str(e)

        engine.say(error)
        engine.runAndWait()

        break
