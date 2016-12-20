#!/usr/bin/python
import web
import requests

urls = (
	'/proxy/(.*)', 'proxy',
)

app = web.application(urls, globals()).wsgifunc()

class proxy:
	def GET(self, url):
		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		if not url:
			return 'Usage: /proxy/www.google.com to return www.google.com'
		else:
			try:
				r = requests.get('http://' + url)
				return r.text
			except:
				return 'oops'

