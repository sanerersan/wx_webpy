import xml.etree.ElementTree as ET

def parser_xml(webData):
	if len(webData) == 0:
		return None

	xmlData = ET.fromstring(webData)
	msgType = xmlData.find('MsgType').text
	if 'text' == msgType:
		return TextMsg(xmlData)
	elif 'image' == msgType:
		return ImageMsg(xmlData)


class Msg(object):
	def __init__(self,xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.MsgId = xmlData.find('MsgId').text

class TextMsg(Msg):
	def __init__(self,xmlData):
		Msg.__init__(self,xmlData)
		self.Content = xmlData.find('Content').text.encode('utf-8')

class ImageMsg(Msg):
	def __init__(self,xmlData):
		Msg.__init__(self,xmlData)
		self.PicUrl = xmlData.find('PicUrl').text
		self.MediaId = xmlData.find('MediaId').text

