from gtts import gTTS
import pygame
import time
import os


class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.ensure_audio_directory()
        self.generate_all_audio_files()

    def ensure_audio_directory(self):
        if not os.path.exists('audio_files'):
            os.makedirs('audio_files')

    def generate_audio(self, text, filename):
        tts = gTTS(text=text, lang='en')
        tts.save(f"audio_files/{filename}.mp3")

    def generate_all_audio_files(self):
        self.generate_audio("Welcome to QuantumFinance.", "greeting")
        self.generate_audio("Please choose an option.", "options")
        self.generate_audio("Option not identified.", "not_identified")

    def play_audio(self, filename):
        try:
            pygame.mixer.music.load(f"audio_files/{filename}.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        except Exception as e:
            print(f"Erro ao reproduzir o áudio: {e}")


    def generate_all_audio_files(self):
        self.generate_audio("Welcome to QuantumFinance.", "greeting")
        self.generate_audio(
            "Please choose an option: Check balance, International purchase simulation, Speak to an attendant, Exit.",
            "options")
        self.generate_audio("Option not identified.", "not_identified")
        self.generate_audio("You chose to check your balance.", "balance")
        self.generate_audio("You chose international purchase simulation.", "purchase")
        self.generate_audio("You chose to speak to an attendant.", "attendant")
        self.generate_audio("Exiting. Thank you for calling QuantumFinance.", "exit")
