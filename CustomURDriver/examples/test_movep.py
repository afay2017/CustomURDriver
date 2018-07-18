import time 
import urx
import logging


if __name__ == "__main__":
    rob = urx.Robot("192.168.12.248")
    try:
        L = 0.1
        v = 0.1
        a = 1.2
        r = 0.05
        pose = rob.getl()
        pose[2] += L
        rob.movep(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getl(wait=True)
            if p[2] > pose[2] - 0.05:
                break

        pose[1] += L
        rob.movep(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getl(wait=True)
            if p[1] > pose[1] - 0.05:
                break

        pose[2] -= L
        rob.movep(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getl(wait=True)
            if p[2] < pose[2] + 0.05:
                break

        pose[1] -= L
        rob.movep(pose, acc=a, vel=v, wait=False)

    finally:
        rob.close()

