import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

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

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")

    except sr.RequestError as e:
        print("Sorry, an error occurred during speech recognition:", str(e))
