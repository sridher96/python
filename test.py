print("hi")
x = 8 
y = 5
z = 1j
print (int(x))
print (int(x*y))
print (complex(z))
a = 10.1
b = 6.8
print (float(a+b))
print (float(a*b))
c = "hello, world!"
print(len(c))
d = "Hello, world!"
print(d.lower())
e = "hello, world!"
print(e. upper())
f = "Hello, world!"
print(f.replace("He", "Te"))
import threading
y = 10
z = 8
def add():
    print(f"Addition: {y+z}")
def subtract():
    print(f"subtract: {y-z}")
def multiply():
    print(f"multiplication: {y*z}")
def division():
    print(f"division: {y/z}")
#create threads
t1 = threading.Thread(target = add)
t2 = threading.Thread(target = subtract)
t3 = threading.Thread(target = multiply)
t4 = threading.Thread(target = division)
#start threads
t1.start()
t2.start()
t3.start()
t4.start()
import datetime
time_after = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(time_after)
  