from flask import Flask, request, send_from_directory
import requests

app = Flask (__name__)

# Google Analytics Property Id ...
_TID = 'UA-XXXXXX-X'

@app.before_request
def collect ():
	d = {
		'v': '1',
		't': 'pageview',
		'dp': request.headers.environ.get ('PATH_INFO', ''),
		'tid': _TID,
		'cid': request.headers.environ.get ('REMOTE_ADDR', ''),
		'uip': request.headers.environ.get ('REMOTE_ADDR', ''),
		'cn': request.args.get ('cn', ''),
		'cs': request.args.get ('cs', ''),
		'cm': request.args.get ('cm', ''),
	}

	p = requests.post ('https://www.google-analytics.com/collect', data = d)

@app.route ('/<path:p>')
def img (p):
	return send_from_directory ('img', p)


