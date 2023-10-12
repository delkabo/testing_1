import os
from moviepy.editor import *
from pydub import AudioSegment
import sys

sys.path.append('/usr/bin')


def edit_text():

    # work with music

    if not os.path.exists('data'):
        os.mkdir('data')

    get_path = r'./'
    name_sh = r'.mp3'
    get_name = [_ for _ in os.listdir(get_path) if _.endswith(name_sh)]
    get_name = get_name[0]
    print(get_name)

    # new_name = os.path.join('file.mp3')
    new_name = 'file.mp3'
    os.rename(get_name, new_name)

    new_title = get_name.strip('.mp3').replace('-', ' ')
    print(new_title)

    music_long = AudioSegment.from_file('file.mp3', format='mp3')
    # short_music = music_long[:10000]
    # short_music.export('data/charp1.mp3', format='mp3')

    long_len = len(music_long)/1000
    print(long_len)

    len_hours = float(long_len/60)//60
    print(" long hours " + str(len_hours))

    len_mus_minute = str(long_len % 60).split('.')[:1]
    print(len_mus_minute)

    len_mus_sc = str(51.64).split('.')[-1:]
    len_mus_sc = len_mus_sc[0]
    print(len_mus_sc)

    # transform long music from second to minute

    # text_info = input('Insert info with timeline: ')

    # with open('timeline.txt', 'a') as file:
    #     file.write(text_info)

    # work with text

    re = []

    file = open('timeline.txt', 'r')
    while True:
        line = file.readline()
        if not line:
            break
        time_code = '-'.join(line.split(' ')[:+1]).strip()
        time_text = ' '.join(line.split(' ')[1:]).strip()
        # print(time_code + ' - ' + time_text)
        re.append({
            'time_code': time_code,
            'time_text': time_text
        })

    re.append({
        'time_code': '',
        'time_text': ''
    })

    file.close()

    time_save = ''
    info_save = ''
    numb = 0
    for item in re:
        numb = numb + 1
        try:
            ts = ':'.join(str(item.get('time_code')).split(':')[-1:]).strip()
            tm = ':'.join(str(item.get('time_code')).split(':')[:1]).strip()
            bm = int(tm)
            b = int(ts)
        except:
            pass

        try:
            if bm == 0 and b == 0:
                tm = '0' + str(bm)
                ts = '0' + str(b)
            elif b == 0 and bm != 0:
                b = 60
                b = b - 1
                bm = bm - 1
                if bm < 10:
                    tm = '0' + str(bm)
                ts = str(b)
            elif b < 10:
                b = b - 1
                ts = '0' + str(b)
            else:
                b = b - 1
                ts = str(b)
        except:
            tm = ''
            ts = ''

        if numb != 1:
            end_time = tm + ':' + ts
            print(str(time_save) + ' - ' + str(end_time) + ' ' + str(info_save))

        time_save = item.get('time_code')
        info_save = item.get('time_text')

        # re_vid = re[list_vid].get('time_code')
        # print(str(re_vid) + ' - ' + str(tm) + ':' + ts)

        # print(ts)
        # print(str(time_save) + ' ' + str(item.get('time_code')))
        # time_save = item.get('time_code')


def main():
    edit_text()


if __name__ == '__main__':
    main()
