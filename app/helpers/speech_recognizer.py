import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_and_recognize(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio_data = self.recognizer.listen(source)
            print("Recognizing...")
            try:
                return self.recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                return "Sorry, I did not understand that."
            except sr.RequestError:
                return "Sorry, the service is down."
