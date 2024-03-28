from helpers.audio_manager import AudioManager
from helpers.speech_recognizer import SpeechRecognizer


def main():
    audio_manager = AudioManager()
    speech_recognizer = SpeechRecognizer()

    audio_manager.play_audio("greeting")
    while True:
        audio_manager.play_audio("options")
        user_choice = speech_recognizer.listen_and_recognize().lower()

        if "saldo" in user_choice:
            audio_manager.play_audio("balance")
        elif "compra" in user_choice:
            audio_manager.play_audio("purchase")
        elif "atendente" in user_choice:
            audio_manager.play_audio("attendant")
        elif "sair" in user_choice:
            audio_manager.play_audio("exit")
            break
        else:
            audio_manager.play_audio("not_identified")


if __name__ == "__main__":
    main()
