import time
import threading
def test():
    a , b = 10 , 5
    print ("addition of a+b value is:" , a+b)
    time.sleep(5)
    print ("subraction of a-b value is:" , a-b)

def test1():
    a , b = 10 , 5
    print ("multiple of a*b value is:" , a*b)
    time.sleep(5)
    print ("division of a/b value is:" , a/b)

thread1 = threading.Thread(target = test)
thread2 = threading.Thread(target = test1)    
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("both thread completed")

# test()
# test1()


