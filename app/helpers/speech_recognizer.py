import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_and_recognize(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Ouvindo...")
            audio_data = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Reconhecendo...")
            try:
                recognized_text = self.recognizer.recognize_google(audio_data, language="pt-BR")
                print(f"Reconhecido: {recognized_text}")
                return recognized_text
            except sr.UnknownValueError:
                return "Opção não identificada."
            except sr.RequestError:
                return "Serviço indisponível."
