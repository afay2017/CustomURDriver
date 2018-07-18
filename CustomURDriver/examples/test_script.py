import time
import urx
import urx.urscript
import logging


if __name__ == "__main__":
    rob = urx.Robot("192.168.12.50")
    try:
        prog = urx.urscript.URScript()
        prog.add_line_to_program("movej([0,-1.81,0,0,0,0])")
        prog.add_line_to_program("servoj([0,-1.80,0,0,0,0])")
        for x in range(800):
            z = 0.000002 * x * x
            y = -1.80 + 0.001 * x
            str = "servoj([{},{},0,0,0,0],gain = 100)".format(z,y)
            prog.add_line_to_program(str)
        prog.add_line_to_program("popup(\"hi\")")
        #for x in range(80):
         #   z = 0.0001 * (80-x) * (80-x)
          #  y = -1.0 - 0.01 * x
           # str = "servoj([{},{},0,0,0,0])".format(z,y)
            #prog.add_line_to_program(str)
        rob.send_program(prog.__call__())

    finally:
        rob.close()

