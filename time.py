import time
import datetime
ts = time.time()
tp = datetime.datetime.now().timestamp()
td = datetime.datetime.now()
print(ts)
print(td.strftime("%x"))
print(tp)