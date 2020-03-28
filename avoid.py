import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import math
import random
import ctypes
import time
#from win32api import GetSystemMetrics

class Window(QWidget):

	def __init__(self):
		super().__init__()
		#window location and dimensions
		self.width = 100
		self.height = 100
		self.x = 500
		self.y = 500
		#button
		b = QPushButton('Click here!', self)
		b_width = 80
		b_height = 30
		b.resize(b_width, b_height)
		b.move(self.width / 2 - b_width / 2, self.height / 2 - b_height / 2)
		b.clicked.connect(self.close)
		#mouse tracking and mouse location
		self.setMouseTracking(True)
		self.mx = 0
		self.my = 0
		#screen dimensions
		self.screen = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
		#other
		self.setGeometry(self.x, self.y, self.width, self.height)
		self.setWindowTitle('Window')
		self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
		self.show()
		
	#move the window if the mouse is in its close vicinity
	def doStuff(self, treshold, emergency_escape, speed):
		cx = self.x + self.width / 2	#window center x
		cy = self.y + self.height / 2	#window center y
		dx = abs(self.mx - cx)
		dy = abs(self.my - cy)
		dfc = math.sqrt(dx ** 2 + dy ** 2)	#distance from center
		#emergency teleport
		if dfc < emergency_escape:
			ex = random.randint(0, self.screen[0] - self.width)
			ey = random.randint(0, self.screen[1] - self.height)
			self.move(ex, ey)
		else:
			#move the window if the mouse is too close
			if self.mx < cx and dx < treshold and self.x + self.width < self.screen[0]:
				self.x += speed
			elif self.mx > cx and dx < treshold and self.x > 0:
				self.x -= speed
			if self.my < cy and dy < treshold and self.y + self.height < self.screen[1]:
				self.y += speed
			elif self.my > cy and dy < treshold and self.y > 0:
				self.y -= speed
			self.move(self.x, self.y)
	
	#print variables for debugging
	def printStuff():
		cx = self.x + self.width / 2
		cy = self.y + self.height / 2
		dx = abs(self.mx - cx)
		dy = abs(self.my - cy)
		dfc = math.sqrt(dx ** 2 + dy ** 2)
		print("x: "+str(self.x)+"\ny: "+str(self.y)+"\ncx: "+str(cx)+"\ncy: "+str(cy))
		print("mx: "+str(self.mx)+"\nmy: "+str(self.my)+"\ndx: "+str(dx)+"\ndy: "+str(dy)+"\ndfc: "+str(dfc)+"\n")
		
	def mouseMoveEvent(self, event):
		#self.mx = event.x()
		#self.my = event.y()
		self.mx = QCursor.pos().x()
		self.my = QCursor.pos().y()
		self.doStuff(100, 10, 1)
	
	def mousePressEvent(self, event):
		#self.mx = event.x()
		#self.my = event.y()
		self.mx = QCursor.pos().x()
		self.my = QCursor.pos().y()
		
	def mouseReleaseEvent(self, event):
		#self.mx = event.x()
		#self.my = event.y()
		self.mx = QCursor.pos().x()
		self.my = QCursor.pos().y()
		
	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()
			
	def update(self):
		while True:
			self.doStuff(50, 20, 1)
			time.sleep(1)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Window()
	#w.update()
	sys.exit(app.exec_())