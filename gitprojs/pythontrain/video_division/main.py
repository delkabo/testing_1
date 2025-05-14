import os
import time
import subprocess
from datetime import datetime
from datetime import timedelta
from moviepy import *
#from moviepy.editor import *
from pydub import AudioSegment
import wave
import soundfile as sf
import contextlib
import sys

sys.path.append('/usr/bin')

re=[]
musics_dir='musics'

def edit_text():
#####################
# part editor
#    # work with music

# Get name and info
    if not os.path.exists('data'):
        os.mkdir('data')

    get_path = r'./'
    name_sh = r'.mp3'
    get_name = [_ for _ in os.listdir(get_path) if _.endswith(name_sh)]
    print("get_name", get_name[0])
    get_name = get_name[0]
    # print(get_name)

    new_name = os.path.join('file.mp3')
    new_name = 'file.mp3'
    os.rename(get_name, new_name)

    new_title = get_name.strip('.mp3').replace('-', ' ')
    print("Новое имя file.mp3 new_title. Результат: ", new_title)

    info_mp3 = sf.info(new_name)
    duration = int(info_mp3.frames / info_mp3.samplerate)
    print(f"Длительность: {duration} сек")
    duration=time.strftime('%H:%M:%S', time.gmtime(duration))
    print("Длительность в формате %H:%M:%S ", duration)



    # with contextlib.closing(wave.open(new_name,'r')) as f:
    #     frames = f.getnframes()
    #     rate = f.getframerate()
    #     music_long = frames / float(rate)
    #     print(music_long)

    # music_long = AudioSegment.from_file('file.mp3', format='mp3')
    # short_music = music_long[:10000]
    # short_music.export('data/charp1.mp3', format='mp3')

    # long_len = len(music_long)/1000
    # print(long_len)

    # len_hours = float(long_len/60)//60
    # print(" long hours " + str(len_hours))

    # len_mus_minute = str(long_len % 60).split('.')[:1]
    # print(len_mus_minute)

    # len_mus_sc = str(51.64).split('.')[-1:]
    # len_mus_sc = len_mus_sc[0]
    # print(len_mus_sc)

#    transform long music from second to minute

#    text_info = input('Insert info with timeline: ')

#    # with open('timeline.txt', 'a') as file:
#    #     file.write(text_info)
###########################3
#    # work with text
    # re = []



# Calculate time for even music
    re_next=[]

    file_t = open('timeline.txt', 'r')
    sum_lines = len(file_t.readlines())
    print('Количество строк в файле: ', sum_lines)
    file_t.close()
    file_t = open('timeline.txt', 'r')
    time_code_prew=0
    time_code_end=0
    time_code=0
    # получить длину видео
    count_x=0
    for i in range(sum_lines):
        line = file_t.readline()
        # if not line:
        #     break
# Загоняем в переменную время и название, получаем следующее время, вычитаем 1 и кладём в кортеж
        if i > 0:
            # print("счётчик -----: ", i)
            if (i > sum_lines):
                print("БОЛЬШЕ sum_lines--------------------------")
                time_code_end=duration
                print("ДЛИНА time_code_end",len(time_code_end))
            else:
                time_code = '-'.join(line.split(' ')[:+1]).strip()
                time_code_end = time_code
            # time.sleep(10)
            if len(time_code_end) <= 5:
                # print("TEST time_code", str(time_code))
                time_code_end = datetime.strptime(time_code, '%M:%S')
                time_code_end = time_code_end - timedelta(seconds=1)
                time_code_end = time_code_end.strftime('%M:%S')
            else:
                time_code_end = datetime.strptime(time_code_end, '%H:%M:%S')
                time_code_end = time_code_end - timedelta(seconds=1)
                time_code_end = time_code_end.strftime('%H:%M:%S')
            print(str(time_code_prew),':',str(time_code_end) + ' - ' + time_text)
            re.append({
                'time_code_start': time_code_prew,
                'time_code_end': time_code_end,
                'time_text': time_text_prew
            })
            time_code_prew = time_code
        
        time_text = ' '.join(line.split(' ')[1:]).strip()
        time_text_prew = time_text


    with open('timeline.txt', 'r') as file_t:
        lines = file_t.read().splitlines()
        data_info_playlist = lines[-1]
    time_code_prew = '-'.join(data_info_playlist.split(' ')[:+1]).strip()
    time_code_end = "6:59:59"
    time_text_prew = ' '.join(line.split(' ')[1:]).strip()
    re.append({
            'time_code_start': time_code_prew,
            'time_code_end': duration,
            'time_text': time_text_prew
        })

    file_t.close()
    print(re)

    if not os.path.exists(musics_dir):
        os.makedirs(musics_dir)

    music_long = AudioSegment.from_file('file.mp3', format='mp3')
    a = AudioSegment.from_mp3(new_name) 
    # short_music = music_long[:10000]
    # short_music.export('data/charp1.mp3', format='mp3')

    # first_second = a[:1000] # get the first second of an mp3 
    slice = a[5000:10000] # get a slice from 5 to 10 seconds of an mp3
    slice.export('musics/charp1.mp3', format='mp3')
    duration = int(info_mp3.frames / info_mp3.samplerate)
    print(f"Длительность: {duration} сек")

def print_array():
    # print(re)
    for x1 in re:
        print(x1["time_text"])



def main():
    edit_text()
    print_array()


if __name__ == '__main__':
    main()
