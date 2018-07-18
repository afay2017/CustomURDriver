import time 
import urx
import logging


if __name__ == "__main__":
    rob = urx.Robot("192.168.12.248")
    try:
        lookahead_time = 0.5
        t = 0.09
        sleepTime = 0.1
        gain = 100

        pose = rob.getj()
        pose = [0, -1.7, 0, 0, 0, 0]
        while abs(rob.getj()[1] - pose[1]) > .001:
            rob.servoj(pose, t, lookahead_time, gain)
            time.sleep(sleepTime)
        pose = [0.5, -1.7, 0, 0, 0, 0]
        while abs(rob.getj()[0] - pose[0]) > .001:
            time.sleep(sleepTime)
            rob.servoj(pose, t, lookahead_time, gain)
        pose = [0.5, -1.3, 0, 0, 0, 0]
        while abs(rob.getj()[1] - pose[1]) > .001:
            time.sleep(sleepTime)
            rob.servoj(pose, t, lookahead_time, gain)
        pose = [0, -1.3, 0, 0, 0, 0]
        while abs(rob.getj()[0] - pose[0]) > .001:
            time.sleep(sleepTime)
            rob.servoj(pose, t, lookahead_time, gain)

    finally:
        rob.close()

