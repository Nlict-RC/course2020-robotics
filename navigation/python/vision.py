import sys
import socket
import threading

from vision_detection_pb2 import Vision_DetectionFrame, Vision_DetectionRobot

class Vision(object):
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.vision_address = '127.0.0.1'
		self.vision_port = 23333
		self.sock.bind((self.vision_address, self.vision_port))
		self.sock.settimeout(1.0)
		self.vision_thread = threading.Thread(target=self.receive_vision)
		self.vision_thread.start()
		self.vision_frame = Vision_DetectionFrame()
		# store blue robot 0's information
		self.my_robot = Robot()
		
	def receive_vision(self):
		while True:
			try:
				data, server = self.sock.recvfrom(4096)
				# print('received message from', server)
				self.vision_frame.ParseFromString(data)
				self.parse_vision()
			except socket.timeout:
				print('VISION TIMED OUT')

	def parse_vision(self):
		for robot_blue in self.vision_frame.robots_blue:
			# print('Robot Blue {} pos: {} {}'.format(robot_blue.robot_id, robot_blue.x, robot_blue.y))
			if robot_blue.robot_id == 0:
				self.my_robot.x = robot_blue.x
				self.my_robot.y = robot_blue.y
				self.my_robot.vel_x = robot_blue.vel_x
				self.my_robot.vel_y = robot_blue.vel_y
				self.my_robot.orientation = robot_blue.orientation
		# for robot_yellow in self.vision_frame.robots_yellow:
			# print('Robot Yellow {} pos: {} {}'.format(robot_yellow.robot_id, robot_yellow.x, robot_yellow.y))


class Robot(object):
	def __init__(self, x=0, y=0, vel_x=0, vel_y=0, orientation=0):
		self.x = x
		self.y = y
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.orientation = orientation


if __name__ == '__main__':
	vision_module = Vision()
