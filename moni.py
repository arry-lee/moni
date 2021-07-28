from pygetwindow import Win32Window,getWindowsWithTitle,getAllWindows
import pyautogui
from adbutils import adb
from PIL import Image



class Moni:
	def __init__(self,title,serial):
		self.title = title
		self.serial = serial

		self.window = getWindowsWithTitle(title)[0]
		self.device = adb.device(serial=serial)

		self.move = self.window.moveTo
		self.resize = self.window.resizeTo 
		self.activate = self.window.activate
		self.is_active = self.window.isActive 

		self.click = self.device.click
		self.swipe = self.device.swipe
		self.shell = self.device.shell
		self.pull = self.device.sync.pull

	def screenshot(self,path=None):
		remote_tmp_path = "/data/local/tmp/screenshot.png"
		# self.shell(["rm", remote_tmp_path])
		self.shell(["screencap", "-p", remote_tmp_path])
		if path is None:
			path = 'tscreenshot.png'
		self.pull(remote_tmp_path,path)
		return Image.open(path)		

	def locate_on_screenshot(self,pinimage,confidence=1):
		screen = self.screenshot()
		return pyautogui.locate(pinimage,screen,confidence=confidence)


b = Moni('bilibili','emulator-5556')

# a = b.locate_on_screenshot('../Pictures/ap.png',confidence=0.8)

# print(b)


	# print(d.get_serialno())

# ws = getAllWindows()
# print(dir(Win32Window))
# for w in ws:
# 	if w.title.startswith('雷电模拟器'):
# 		print(w.title )

# ds = adb.device_list()
# for d in ds:
# 	print(d.serial)
# print(ds)


# class Moni(object):
# 	def __init__(self,title,border,dpi=(1080,1920),serial='127.0.0.1:5555'):
# 		self.title = title
# 		self.window = getWindowsWithTitle(self.title)[0]
# 		self.border_left,self.border_top,self.border_right,self.border_bottom = border
# 		self.dpi = dpi
# 		self._ge_size()

# 		self.d = adb.device(serial=serial)

# 	def _ge_size(self):
# 		self.size = self.window.size
# 		self.box = self.window.box
# 		self.rect = (self.window.left + self.border_left, self.window.top + self.border_top, 
# 			  self.window.right - self.border_right, self.window.bottom - self.border_bottom)
# 		self.left = self.border_left + self.window.left
# 		self.top = self.border_top + self.window.top 

# 		self.right = self.window.right - self.border_right
# 		self.bottom = self.window.bottom - self.border_bottom 

# 		self.width = self.right - self.left
# 		self.height = self.bottom - self.top

# 	def move(self,x,y):
# 		self.window.moveTo(x,y)
# 		self._ge_size() 

# 	def resize(self,width,height):
# 		self.window.resizeTo(width,height)
# 		self._ge_size()

# 	def pull(self,*args,**kwargs):
# 		return self.d.sync.pull(*args,**kwargs)

# 	def click(self,x,y):
# 		return self.d.click(x,y)

# 	def swipe(self,x,y,tx,ty,duration=0.5):
# 		return self.d.swipe(x,y,tx,ty,duration)

# 	def screenshot(self,path=None):
# 		self.window.activate()
# 		if not path:
# 			return pyautogui.screenshot(region=(self.left,self.top,self.width,self.height))
# 		else:
# 			return pyautogui.screenshot(path,region=(self.left,self.top,self.width,self.height))

# 	def map_on_screen(self,point):
# 		""" 将手机截图上的点映射到电脑截图 """
# 		scale_rate = round(self.width / self.dpi[0], 2)
# 		x,y = point
# 		x = x * scale_rate
# 		y = y * scale_rate
# 		x += border_left + w.left
# 		y += border_top + w.top
# 		return x,y 

# 	def screenshot(self,fp):
# 		remote_tmp_path = "/data/local/tmp/screenshot.png"
# 		self.d.shell(["rm", remote_tmp_path])
# 		self.d.shell(["screencap", "-p", remote_tmp_path])
# 		self.d.sync.pull(remote_tmp_path,fp)
# 		return Image.open(fp)


# m = Moni('雷电模拟器',border=(1,34,1,3),dpi=(1080,1920))
# m.move(0,0)
# m.screenshot('t.png')

