import os
import time
import datetime
for i in range(3):
    ds = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    os.system('echo {} >> result.txt'.format(ds))
    time.sleep(1)
    os.system('''git commit -a -m 'Modified at {}' '''.format(ds))
    print("one second later")
