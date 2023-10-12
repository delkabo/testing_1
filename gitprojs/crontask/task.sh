TIMES=$(date +"%T")

echo "Bash - это круто!" $TIMES >> ~/docs/crontab_log.txt
python3 ~/docs/crontask/taskpy.py
