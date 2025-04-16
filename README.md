# Transcrição de Áudio com FasterWhisper

Este projeto grava um trecho de áudio pelo microfone e transcreve automaticamente utilizando o modelo `faster-whisper`.

## Como rodar no macOS

1. Abra o Terminal e navegue até o diretório do projeto:
   ```bash
   cd /caminho/para/o/projeto
   ```
2. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   ```
3. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Rode o projeto:
   ```bash
   python3 -m main
   ```
## Modelo utilizado
- faster-whisper com o modelo large-v2 ou turbo, dependendo da configuração.

## Dependências principais
* faster-whisper

* sounddevice

* scipy
