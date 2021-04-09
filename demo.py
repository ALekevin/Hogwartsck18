import _thread
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 4]

class Mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
    def run(self):
        self.func(*self.args)



def loop(nloop, time):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    sleep(time)
    logging.info("end loop" + str(nloop) + " at " + ctime())


def main():
    logging.info("start all at " + ctime())
    locks = []
    loop_n = range(len(loops))
    for i in loop_n:
        t=Mythread(func=loop, args=(i, loops[i]),name=loop.__name__)
        locks.append(t)
    for i in loop_n:
        locks[i].start()
    for i in loop_n:
        locks[i].join()

    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
