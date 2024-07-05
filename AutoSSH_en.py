#
# Install Python from https://www.python.org/downloads/
#
# Install pip: python get-pip.py (cmd)
#
# If it doesn't work, follow the tutorial
#
# Step 1: In cmd, type: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py (to download pip installer)
#
# Step 2: In cmd, type: python get-pip.py (to execute installation)
#
# Step 3: In cmd, type: pip --version (to verify installation)
#

import pyautogui as pa
import time

pa.PAUSE = 1.2

pa.hotkey("win","r") # open run

pa.write("cmd") # type cmd

pa.press("enter")

pa.write("ssh user@ip") # change to your user and IP | example: ssh marcelo@127.0.0.1

pa.press("enter")

time.sleep(0.5)

pa.write("password") # change to your password

pa.press("enter")

#if dont want go to root delete or comment the code below

pa.write ("sudo -s") # switch to root

pa.press("enter")

time.sleep(0.5)

pa.write("password") # change to your password again

pa.press("enter")
