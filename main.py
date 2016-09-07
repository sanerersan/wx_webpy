import web
from handle import *

urls = (
	'/wx','Handle',
	)

if __name__ == '__main__':
	app = web.application(urls,globals())
	app.run()		
