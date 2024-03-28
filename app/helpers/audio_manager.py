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
        tts = gTTS(text=text, lang='pt-BR')
        tts.save(f"audio_files/{filename}.mp3")

    def play_audio(self, filename):
        try:
            pygame.mixer.music.load(f"audio_files/{filename}.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        except Exception as e:
            print(f"Erro ao reproduzir o áudio: {e}")

    def generate_all_audio_files(self):
        self.generate_audio("Seja bem vindo a Quantum Finance.", "greeting")
        self.generate_audio(
            "Por favor, escolha uma opção: Consulta ao saldo da conta, Simulação de compra internacional, Falar com um"
            "atendente, Sair do atendimento.",
            "options")
        self.generate_audio("Opção não identificada.", "not_identified")
        self.generate_audio("Você escolheu consultar saldo da conta.", "balance")
        self.generate_audio("Você escolheu simular compra internacional", "purchase")
        self.generate_audio("Você escolheu falar com um atendente.", "attendant")
        self.generate_audio("Atendimento encerrado. Obrigado pela preferencia, Quantum Finance agradece.", "exit")
