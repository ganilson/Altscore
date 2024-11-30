from pydub import AudioSegment
import ogg
import tempfile
import ogg.vorbis

# Abrir o arquivo de áudio de entrada (substitua 'input_audio.mp3' pelo caminho do seu arquivo)
audio = AudioSegment.from_file('input_audio.mp3')

# Converter para formato WAV
wav_audio = audio.export(format='wav')

# Inicializar o codificador Ogg Vorbis
vorbis_encoder = ogg.vorbis.VorbisEncoder(wav_audio.channels, wav_audio.frame_rate, 0.4)  # Taxa de bits de 0.4

# Codificar os dados de áudio WAV para Ogg Vorbis
vorbis_data = vorbis_encoder.encode(wav_audio.raw_data, len(wav_audio.raw_data))

# Salvar os dados codificados em um arquivo Ogg Vorbis (substitua 'output_audio.ogg' pelo nome do arquivo de saída)
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(vorbis_data.read())
        temp_file_path = temp_file.name
with open('output_audio.ogg', 'wb') as ogg_file:
    ogg_file.write(vorbis_data)
