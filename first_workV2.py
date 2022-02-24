#스레드 두 개를 생성
#첫번째 스레드는 0부터 65535까지 1초에 1씩 증가하는 스레드, 65535가되면 0부터 다시 시작
#두번째 스레드는 첫번째 스레드의 값을 1초에 한번씩 출력하는 스레드
#멀티스레딩으로 첫번째 스레드가 카운팅진행하면서 두번째 스레드가 해당 값을 받아 출력

from datetime import datetime
from queue import Queue
import time
import threading


#1초에 1씩 증가하는 스레드(65535가 되면 다시 0부터 시작)//10으로 시험하기
def counting(q):
    number=0
    
    while True:
        if number > 10:  #65535가되면 0으로 돌아간다
            number = 0

        #print("counting:", number)
        now = datetime.now()
        
        q.put(number)
        print("{}분 {}초".format(now.minute, now.second), "counting:", number)
        number += 1 # 1씩 증가
        time.sleep(1) #1초 마다
        

def printing(q):
    while True:
        number = q.get()
        print("printing:", number)#첫번째 스레드에서 실행한 함수
        time.sleep(1) #1초 마다
        

if __name__ == "__main__":
    
    queue = Queue()
    #첫번째 스레드로 실행할 함수 counting 선언
    first_thread = threading.Thread(target = counting, args=(queue, ))
    #두번째 스레드로 실행할 함수 printing 선언
    second_thread = threading.Thread(target = printing, args=(queue, ))

    #스레드 실행
    first_thread.start()
    second_thread.start()
    

    first_thread.join()
    second_thread.join()