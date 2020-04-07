import threading
import time
from datetime import datetime


class Timer(object):
    can_record = False

    def __init__(self, interval=60):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution

    def can_video_record_start(self):
        print('is it time to record ? {}'.format( self.can_record))
        return self.can_record

    def run(self):

        """ Method that runs forever """
        while True:
            # Do something
            time.sleep(self.interval)
            now = datetime.datetime.now()

            morning_time = "05:59:60"  # leap second
            morning_time = now.strftime("%Y-%m-%d") + " " + morning_time
            my_time = time.strptime(morning_time, "%Y-%m-%d %H:%M:%S")

            morning_time_2 = "23:59:60"  # leap second
            morning_time_2 = now.strftime("%Y-%m-%d") + " " + morning_time_2
            my_time_2 = time.strptime(morning_time_2, "%Y-%m-%d %H:%M:%S")

        if my_time > now > my_time_2:
            print('It s time to start recording')
            can_record = True
        else:
            print("It s time to stop recording")
            can_record = False
