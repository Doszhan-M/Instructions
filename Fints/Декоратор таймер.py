# import subprocess

#     # отрыть скрипт bash как файл и выполнить ее из python среды
#     with open('./scripts/parse.sh', 'rb') as file:
#         script = file.read()
#     rc = subprocess.call(script, shell=True)
#     return redirect('botconfig')

import time

def onceEveryCustomSeconds(f):
    f.last_execution = 0
    def wrapper(*args, **kwargs):
        seconds = args[-1]
        real_args = args[:-1]
        if f.last_execution < time.time() - seconds:
            f.last_execution = time.time()
            return f(*real_args, **kwargs)
    return wrapper

@onceEveryCustomSeconds
def function(foo):
    print(foo)

while True:
    function("Hello again", 3)
