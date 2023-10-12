text = 'helloy Python'

fopen = open('/home/kamil/docs/crontab_log.txt', 'a')
fopen.write(text + '\n')
fopen.close()
