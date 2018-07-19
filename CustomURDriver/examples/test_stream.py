import time
import urx
import urx.urscript
import logging


if __name__ == "__main__":
    rob = urx.Robot("192.168.12.248")
    try:
        prog = urx.urscript.URScript()
        rob.movej([0,-1.81,0,0,0,0],wait=False)
        while True:
            if abs(rob.getj()[1] + 1.81) < .01:
                break;

        rob.send_message("servoj([0,-1.80,0,0,0,0])")
        for x in range(800):
            z = 0.000002 * x * x
            y = -1.80 + 0.001 * x
            str = "servoj([{},{},0,0,0,0],gain = 100)".format(z,y)
            rob.send_message(str)
        rob.send_message("popup(\"hi\")")
    finally:
        rob.close()

