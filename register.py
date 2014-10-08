
class WordRegister:
	word = 0
	byteH = 0
	byteL = 0
	def __init__(self, word=False, byteH=False, byteL=False):
		self.word = 0
		self.byteH = 0
		self.byteL = 0
		if type(word) is int:
			self.word = word & 0xFFFF
			self.byteH = (word & 0xFF00)>>8
			self.byteL = word & 0x00FF
		else:
			if type(byteH) is int:
				self.word = (byteH<<8)&0xFF00
				self.byteH = byteH & 0x00FF
			elif type(byteL) is int:
				self.word = self.word|(byteL&0x00FF)
				self.byteL = byteL & 0x00FF
	

	def __setattr__(self, name, val):
		if name == "word":
			self.__dict__[name] = val&0xFFFF
			self.__dict__["byteH"] = val & 0xFF00
			self.__dict__["byteL"] = val & 0x00FF
		elif name == "byteH":
			self.__dict__[name] = val&0x00FF
			self.__dict__["word"] = (self.word&0x00FF) | (val<<8)&0xFF00
		elif name == "byteL":
			self.__dict__[name] = val&0x00FF
			self.__dict__["word"] = (self.word&0xFF00) | (val&0x00FF) 


