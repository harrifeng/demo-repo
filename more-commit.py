import os
import time
for i in range(10):
    os.system('''echo `date` >> result.txt''')
    time.sleep(1)
    print("one second later")
