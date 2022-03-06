# AutoClassJoiner

This python script permit to access to class_link via selenium

This script is scheduled in crontab file by AutoRecording 

`mm HH DD MM * export DISPLAY=:1 && /bin/bash ClassJoiner.sh #DYNAMIC JOIN - 'FISICA GENERALE I'`

ClassJoiner.sh simply contain 

`/venv_path/bin/python /project_path/AutoClassJoiner/main.py`
