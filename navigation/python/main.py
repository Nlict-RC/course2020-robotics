from vision import Vision
from action import Action
from debug import Debugger
import time

if __name__ == '__main__':
	vision = Vision()
	action = Action()
	debugger = Debugger()
	while True:
		# Do something(path planning)
		action.sendCommand(vx=100, vy=0, vw=0)
		debugger.draw_circle(vision.my_robot.x, vision.my_robot.y)
		time.sleep(0.02)
