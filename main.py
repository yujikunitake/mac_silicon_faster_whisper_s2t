import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import time
import io

start = time.time()
model = WhisperModel('turbo', device='auto', compute_type='int8')
end = time.time()

def record_audio(duration_seconds=5, sample_rate=16000):
    print('Gravando...')
    audio = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')

    for i in range(duration_seconds, 0, -1):
        print(f'{i}...')
        time.sleep(1)

    sd.wait()
    print('Gravação finalizada')

    return audio, sample_rate

def save_audio_to_memory(audio, samplerate):
    audio_buffer = io.BytesIO()
    write(audio_buffer, samplerate, audio)
    audio_buffer.seek(0)

    return audio_buffer

def transcribe_audio(file_path):
    print('Transcrevendo...')
    start_time = time.time()

    segments, _ = model.transcribe(file_path, language='pt', beam_size=5)

    end_time = time.time()
    elapsed_time = end_time - start_time

    for segment in segments:
        print(f'[{segment.start:.2f}s - {segment.end:.2f}s] {segment.text}')

    print(f'Tempo de carregamento do modelo: {end - start:.2f} segundos')
    print(f'\n Tempo de transcrição: {elapsed_time:.2f}s')

if __name__ == '__main__':
    audio, sr = record_audio()
    path = save_audio_to_memory(audio, sr)
    transcribe_audio(path)
