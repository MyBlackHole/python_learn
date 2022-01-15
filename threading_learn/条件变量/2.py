import threading

cv = threading.Condition()
#消费者线程
cv.acquire()
while not available():
	cv.wait()
cv.release()

#生成者线程
cv.acquire()
make_available()
cv.notify()
cv.release()

