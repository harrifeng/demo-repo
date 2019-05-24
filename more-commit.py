import os
import time
import datetime
import random
for i in range(3):
    ds = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    os.system('echo {} >> result.txt'.format(ds))
    time.sleep(2 * random.random())
    os.system('''git commit -a -m 'Modified at {}' '''.format(ds))
    print("one---------finish---------->>")
