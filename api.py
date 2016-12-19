import web
import requests

urls = (
	'/proxy/(.*)', 'proxy',
)

app = web.application(urls, globals())

class proxy:
	def GET(self, url):
		if not url:
			return 'Usage: /proxy/www.google.com to return www.google.com'
		else:
			r = requests.get('http://' + url);
			print r;
			return r.text;

if __name__ == "__main__":
    app.run()
