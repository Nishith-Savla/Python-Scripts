from multiprocessing import Process
a = 3
def loopA():
    global a
    print("LoopA called")
    while True:
        if (a == 1):
            print("worked")
            break

def loopB():
    print("LoopB called")
    global a
    while True:
        if(a==3):
            a = 1
            break
    print("B done")
    print(a)

if __name__ == "__main__":
    Process(target=loopB).start()
    Process(target=loopA).start()
