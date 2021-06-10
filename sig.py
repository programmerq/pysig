import os
import signal


def handler(signum, frame):
    print(f"Signal received {signal.strsignal(signum)}")


for i in signal.valid_signals():
    try:
        signal.signal(int(i), handler)
        print(f"added {str(i)}")
    except OSError as e:
        print(f"skipping {str(i)}")

while True:
    signal.pause()