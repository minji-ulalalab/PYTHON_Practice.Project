#클래스화 필요
#Thread클래스를 상속받는 클래스를 만들어서 run()하여 객체 생성

from datetime import datetime
from queue import Queue
import time


class Count():
    def run(self, q):
        number = 0
        while True:
            if number > 65535:  #65535가되면 0으로 돌아간다
                number = 0
            now = datetime.now()
            q.put(number)
            print("{}분 {}초".format(now.minute, now.second), "counting:",number)
            number += 1 # 1씩 증가
            time.sleep(1) #1초 마다



