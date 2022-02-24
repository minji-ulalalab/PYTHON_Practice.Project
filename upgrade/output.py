
from queue import Queue
import time
from datetime import datetime

class Output():
    def run(self, q):
        while True:
            now = datetime.now()
            number = q.get()#첫번째 스레드에서 사용한 number와 이름만 같고 다른 변수
            print("{}분 {}초".format(now.minute, now.second), "printing:",number)
            time.sleep(1) #1초 마다

    