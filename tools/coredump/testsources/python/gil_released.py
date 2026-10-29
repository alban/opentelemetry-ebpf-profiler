#!/usr/bin/env python3
# Sleeps in a C call that released the GIL (time.sleep), under distinctively
# named Python functions. Since Python 3.13, releasing the GIL clears
# _Py_tss_tstate, so the thread state must be read from the gilstate.
#
# Usage: python3.14 gil_released.py &
#        ./coredump new -pid $! -name <name>
import time


def sleeps_without_gil():
    time.sleep(3600)


def calls_sleep():
    sleeps_without_gil()


calls_sleep()
