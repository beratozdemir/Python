#!/usr/bin/python
import time
t = time.localtime()
h = t.tm_hour
m = t.tm_min
s = t.tm_sec
file = open (str(h)+"-"+str(m)+"-"+str(s)+".txt","w")
