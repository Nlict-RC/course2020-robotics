import socket
import sys
import time

from zss_debug_pb2 import Debug_Msgs, Debug_Msg, Debug_Arc

class Debugger(object):
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.debug_address = ('localhost', 20001)

	def draw_circle(self, x, y):
		package = Debug_Msgs()
		msg = package.msgs.add()
		msg.type = Debug_Msg.ARC
		msg.color = Debug_Msg.WHITE
		arc = msg.arc
		radius = 300
		arc.rectangle.point1.x = x - radius
		arc.rectangle.point1.y = y - radius
		arc.rectangle.point2.x = x + radius
		arc.rectangle.point2.y = y + radius
		arc.start = 0
		arc.end = 360
		arc.FILL = True
		self.sock.sendto(package.SerializeToString(), self.debug_address)

if __name__ == '__main__':
	debugger = Debugger()
	while True:
		debugger.draw_circle(x=100, y=200)
		time.sleep(0.02)
