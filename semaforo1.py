# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import BoundedSemaphore, Semaphore, Lock
import time
import random

N = 8

def is_anybody_inside(critical, tid):
    found = False
    i = 0
    while i<len(critical) and not found:
        found = tid!=i and critical[i]==1
        i += 1
    return found

def task(common, tid, sem):
    a=0
    for i in range(20):
        print(f'{tid}−{i}: Non−critical Section')
        time.sleep(random.random())
        print(f'{tid}−{i}: End of non−critical Section')
        sem.acquire() 
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section')
        time.sleep(random.random())
        common.value = v
        print(f'{tid}−{i}: End of critical section',flush=True)
        sem.release()
            
def main():
    lp = []
    common = Value('i', 0)
    sem=Lock()
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, sem)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")

if __name__ == "__main__":
    main() 