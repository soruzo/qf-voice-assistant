# QuantumFinance Voice Assistant

## Descrição
Este é um assistente virtual simples para a QuantumFinance que permite a interação do usuário por meio de voz. O assistente oferece várias opções de atendimento, como consulta de saldo, simulação de compra internacional, falar com um atendente e sair do atendimento.

## Pré-requisitos
Certifique-se de ter Python 3.8 ou superior instalado em seu sistema. Além disso, é necessário ter as seguintes bibliotecas Python instaladas:
- gTTS (Google Text-to-Speech)
- SpeechRecognition
- Pygame

Você pode instalar essas bibliotecas usando pip:
```pip install gtts SpeechRecognition pygame```


## Configuração e Execução
Para executar o assistente virtual, siga os passos abaixo:
1. Clone o repositório para sua máquina local.
2. Navegue até o diretório do projeto.
3. Execute o arquivo `main.py` usando Python:
```python app/main.py```


## Como Usar
Após iniciar o assistente, você ouvirá uma saudação seguida de opções de atendimento. Responda verbalmente com a opção desejada. O assistente processará sua resposta e realizará a ação correspondente.

## Estrutura do Projeto
```
qf-voice-assistant/
│
├── app/
│ ├── main.py
│ ├── audio_manager.py
│ └── speech_recognizer.py
│
└── audio_files/
```
- `main.py`: Ponto de entrada principal do assistente virtual.
- `audio_manager.py`: Gerencia a geração e reprodução de áudio.
- `speech_recognizer.py`: Lida com o reconhecimento de voz.

## Contribuição
- Anthony Moura
- Bruno Bittencurt
- Bruno Neves
- Carla Scherer
---