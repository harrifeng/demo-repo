import os
import time
import datetime
for i in range(3):
    ds = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    # os.system({}.format('''echo `date` >> result.txt'''))
    os.system('echo {} >> result.txt'.format(ds))
    time.sleep(1)
    print("one second later")
