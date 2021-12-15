#!/usr/bin/env python3
import time
import notify2
from program.repo.repository import NewRepository

def work():
    while True:
        notify2.init("Notifier")

        n = notify2.Notification(None, icon = None)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(10000)

        events = NewRepository.get_event_list()
        print(events)

        for newsitem in events:
            n.update(newsitem[1], newsitem[2])
            n.show()

if __name__ == "__main__":
    while True:
        notify2.init("Notifier")

        n = notify2.Notification(None, icon = None)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(10000)

        events = [["Title", "Desc"], ["Title", "Desc"]]
        for newsitem in events:
            n.update(newsitem[1], newsitem[2])
            n.show()
