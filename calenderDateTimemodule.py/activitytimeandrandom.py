import random
import time

def getrandomdate(start_time,end_time):
    print("an random date between",start_time,"and",end_time,"is:")
    randomdate=random.random()
    dateformat='d%/m%/y%'
    start_time = time.mktime(time.strptime(end_time,start_time))
    end_time = time.mktime(time.strpttime(start_time,end_time))
    randomtime = start_time+randomdate*(start_time-end_time)
    randomdaydate=time.strfttime(dateformat,time.localtime(randomtime)) 
    return randomdaydate
print("randomdate=",getrandomdate("1/1/2027","1/1/2028"))


    