import time 
import urx
import logging


if __name__ == "__main__":
    rob = urx.Robot("192.168.12.248")
    try:
        l = 0.1
        v = 0.07
        a = 0.1
        r = 0.05
        pose = rob.getj()
        pose[2] += l
        rob.movej(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getj(wait=True)
            if p[2] > pose[2] - 0.05:
                break

        pose[1] += l 
        rob.movej(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getj(wait=True)
            if p[1] > pose[1] - 0.05:
                break

        pose[2] -= l
        rob.movej(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getj(wait=True)
            if p[2] < pose[2] + 0.05:
                break

        pose[1] -= l
        rob.movej(pose, acc=a, vel=v, wait=True)

    finally:
        rob.close()

