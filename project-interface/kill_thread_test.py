from threading import Thread
import time
m=0
class CountdownTask:
      
    def __init__(self):
        self._running = True
      
    def terminate(self):
        self._running = False
    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            global m
            m=m+1
            time.sleep(1)
  
c = CountdownTask()
t = Thread(target = c.run, args =(10, ))
t.start()
# Signal termination
if(m>5):
    c.terminate() 