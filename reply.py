import time

class Msg(object):
	def __init__(self):
		pass

	def send(self):
		return 'success'

class TextMsg(Msg):
	def __init__(self,toUser,fromUser,content):
		self.__dict = dict()
		self.__dict['ToUserName'] = toUser
		self.__dict['FromUserName'] = fromUser
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['Content'] = content

	def send(self):
		xmlForm = '''
		<xml>
		<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
		<MsgType><![CDATA[text]]></MsgType>
		<Content><![CDATA[{Content}]]></Content>
		</xml>
		'''	

		return xmlForm.format(**self.__dict)

class ImageMsg(Msg):
	def __init__(self, toUserName, fromUserName, mediaId):
		self.__dict = dict()
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['MediaId'] = mediaId
	def send(self):
		XmlForm = """
		<xml>
		<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
		<CreateTime>{CreateTime}</CreateTime>
		<MsgType><![CDATA[image]]></MsgType>
		<Image>
		<MediaId><![CDATA[{MediaId}]]></MediaId>
		</Image>
		</xml>
		"""
		return XmlForm.format(**self.__dict)	