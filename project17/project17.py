import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from os import remove

#dizer o final da extensão dos arquivos, porque ele transforma
music_mp3 = "C:/Users/Biel/Music/Kiana Ledé - Title _ Lyrics.mp3"
#para wav mas não coloca a extensão .wav
music_wav = "project17/Kiana Ledé - Title _ Lyrics).wav"

#falar a extensão e indicar o arquivo
som = AudioSegment.from_mp3(music_mp3) 
#convertendo para wav, exportar som para extensão .wav com formarto wav
som.export(music_wav, format='wav')


#dividir o arquivo em partes por que o reconhecimento de voz ele precisa de pequenas partes de audio para fazer a tradução ou transcrição
#pegando o arquivo depois de ter transformando em wav
music = AudioSegment.from_file(music_wav, 'wav') #especificar que esta em wav
tamanho = 5000 #tamanho em milisegundos
music_parts = make_chunks(music, tamanho) #indicando o arquivo de musica e o tamanho para separar
parts_audio = []
for i, part in enumerate(music_parts):
    #numerando os arquivos em partes
    part_name = f'project17/musics parts/Kiana Ledé{i}.wav'
    #adicionando os aquivos, sem exportar, a lista
    parts_audio.append(part_name)
    #exportando as part, com os nome ou nome e caminhos e extensão part_name, .wav e convertendo para formato .wav
    part.export(part_name, format='wav')
    

#transcrição do audio com o Speech
def trans_audio(file_audio):
    recognizer = sr.Recognizer()
    #Selecionando o arquivo para reconhecer
    with sr.AudioFile(file_audio) as source: #como ele precisa ser aberto e fechado eu uso o with por que ele abre e fecha o arquivo sem problemas
        re_audio = recognizer.record(source) #leitura para a forma que ele vai reconhecer
    
    #transcrição para palavras com Google Speech Recognition
    valor = 1000
    tamanho = 8000
    try:
        print(f'\033[33m{recognizer.recognize_google(re_audio, language="en")}\033[m')
    except:
        while True:
            try:
                for part_music in parts_part:
                    remove(part_music)
            except:
                print('Não criado')

            print('tentando novamente')
            print(tamanho)
            
            music_parts = make_chunks(music, tamanho)
            parts_part = []
            for i, part in enumerate(music_parts):
                part_name = f'project17/musics parts/part/Kiana Ledé{i}.wav'
                parts_part.append(part_name)
                part.export(part_name, format='wav')
            with sr.AudioFile(file_audio) as source:
                re_audio = recognizer.record(source)
            tamanho += valor
            if tamanho <= 1500:
                valor = 500
            if tamanho == 15000:
                break
for i, musics_parts in enumerate(parts_audio):
    print('parte', i)
    trans_audio(musics_parts)
for musics_parts in parts_audio:
    remove(musics_parts)