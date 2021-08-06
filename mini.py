# 用于模拟微信小程序的窗口行为
import os
import pyautogui
from pygetwindow import getWindowsWithTitle

WECHATAPPLAUNCHERPATH = "D:\\Program Files (x86)\\Tencent\\WeChat\\WechatAppLauncher.exe"

class Mini(object):
	"""模拟微信小程序的行为"""
	def __init__(self,title,launch_appid = None):
		self.title = title
		try:
			self.window = getWindowsWithTitle(self.title)[0]
		except:
			self.open(launch_appid)

		while True:
			try:
				self.window = getWindowsWithTitle(self.title)[0]
				break
			except:
				continue

		self.minimize = self.window.minimize
		self.restore = self.window.restore 
		self.close = self.window.close
		self.move = self.window.moveTo
		self.resize = self.window.resizeTo
		self.activate = self.window.activate
		self.original_width = self.window.width
		self.original_height = self.window.height


	@property
	def width(self):
		return self.window.width

	@property
	def height(self):
		return self.window.height

	@property
	def box(self):
		return self.window.box

	def open(self,launch_appid):	
		print('正在启动' + self.title)
		cmd = '"%s" -launch_appid=%s' % (WECHATAPPLAUNCHERPATH,launch_appid)
		os.system(cmd)
		print('启动成功' + self.title)
		self.is_open = True

	def close(self):
		self.window.close()


	def click(self,x,y):
		pyautogui.click(x,y)


if __name__ == '__main__':
	a = Mini('天天象棋','wx9e44d62c7ab75740')
	象棋 = (57,516)
	a.move(0,0)
	a.click(*象棋)
