import os
import time
import datetime
import random
for i in range(10):
    ds = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    os.system('git add .')
    os.system('echo {} >> result-{}.txt'.format(ds, i))
    time.sleep(random.random())
    os.system('''git commit -a -m 'Modified at {}' '''.format(ds))
    print("one---------finish---------->>")
