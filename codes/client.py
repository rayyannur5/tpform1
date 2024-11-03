import argparse
import subprocess
import time
from datetime import datetime

# Set up command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-I', '--id', default='short')
parser.add_argument('-L', '--loop', type=int, default=10)
args = parser.parse_args()

appID = args.id
loop = args.loop

def execute(command):
    return subprocess.run(command, capture_output=True, shell=True).stdout.decode()

for i in range(0, loop):
    res = execute(f"curl localhost?appID={appID}")
    print(datetime.now())
    print(res)
    time.sleep(1)