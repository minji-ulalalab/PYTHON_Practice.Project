from queue import Queue
import threading
from count import Count
from output import Output


queue = Queue()
counting = Count()
printing = Output()

#첫번째 스레드로 실행할 함수 counting 선언
first_thread = threading.Thread(target = counting.run, args=(queue, ))
#두번째 스레드로 실행할 함수 printing 선언
second_thread = threading.Thread(target = printing.run, args=(queue, ))
#스레드 실행
first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()