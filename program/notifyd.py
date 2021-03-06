#!/usr/bin/env python3
from program.repo.repository import NewRepository
import time
from plyer.utils import platform
from plyer import notification
from datetime import datetime
import os

def work():
    time.sleep(2)
    shown = []
    while True:
        events = NewRepository.get_event_list()

        for item in events:
            if item[3] in shown:
                continue
            date_str = datetime.now().strftime("%Y-%m-%d %H:%M").split(" ")
            date_date_now = date_str[0].split("-")
            date_str2 = item[2].split(" ")
            date_date = date_str2[0].split("-")
            print()

            if (int(date_date[0]) == int(date_date_now[0]) and int(date_date[1]) == int(date_date_now[1]) and
                ((int(date_date[2]) == int(date_date_now[2]) + 1) or (int(date_date[2]) == int(date_date_now[2])))): # Day
                notification.notify(
                    title=item[0],
                    message=item[1],
                    app_name='Studento Atmintine',
                    app_icon=os.path.abspath("icon") + ('.ico' if platform == 'win' else '.png')
                )
                shown.append(item[3])

        time.sleep(10)
