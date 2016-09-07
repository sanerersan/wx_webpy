import hashlib
import web
import receive
import reply

class Handle(object):
	def GET(self):
		try:
			print('234')
			data = web.input()
			if len(data) == 0:
				return 'hello,this is handle view'

			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = 'mirrorworld'

			validList = [token,timestamp,nonce]
			validList.sort()
			sha1 = hashlib.sha1()
			
			for item in validList:
				sha1.update(item.encode('ascii'))

			hashCode = sha1.hexdigest()
			print(hashCode)
			print(signature)
			if hashCode == signature:
				return echostr
			else:
				return ''
		except Exception as e:
			print(e)
			return ''

	def POST(self):
		return '123'
		try:
			print('123')
			webData = web.data()
			print(webData)
			recvMsg = receive.parser_xml(webData)
			if isinstance(recvMsg,receive.Msg) and recvMsg.MsgType == 'text':
				toUser = recvMsg.FromUserName
				fromUser = recvMsg.ToUserName
				content = 'test'

				replyMsg = reply.TextMsg(toUser,fromUser,content)
				return replyMsg.send()
			else:
				print('not handle')
				return 'success'

		except Exception as e:
			print(e)
			return ''			