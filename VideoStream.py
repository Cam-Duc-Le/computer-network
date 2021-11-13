import cv2

def countFrame(video):
		total = 0
		while True:
			(grabbed, frame) = video.read()
			if not grabbed:
				break
			total += 1
		return total
def getInfomation(filename):
		movie = cv2.VideoCapture(filename)
		total = countFrame(movie)
		fps = int(movie.get(cv2.CAP_PROP_FPS))
		movie.release()
		return total, fps

class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.frameNum = 0
		self.totalFrame, self.fps = getInfomation(filename)

	def nextFrame(self):
		"""Get next frame."""
		data = self.file.read(5) # Get the framelength from the first 5 bits
		if data: 
			framelength = int(data)	
			# Read the current frame
			data = self.file.read(framelength)
			self.frameNum += 1
		return data
	
	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
	
	def getTotalFrame(self):
		"""Get total frame ."""
		return self.totalFrame
	
	def getFps(self):
		"""Get fps of the movie."""
		return self.fps
	
	def move(self, newFrameNum):
		if self.frameNum == 0:
			self.file = open(self.filename, 'rb')

		if newFrameNum > self.frameNum:
			while self.frameNum < newFrameNum:
				data = self.nextFrame()
		elif newFrameNum < self.frameNum:
			self.frameNum = 0
			self.move(newFrameNum)
		else :
			return 