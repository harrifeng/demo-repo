import os
import time
import datetime
import random
for i in range(10):
    ds = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    os.system('echo {} >> result.txt'.format(ds))
    time.sleep(random.random())
    os.system('''git commit -a -m 'Feature 001 Modified at {}' '''.format(ds))
    print("one---------finish---------->>")
