#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template

from collections import OrderedDict

from ksRequest import KsRequest

import json

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def search_form():
# 	return render_template('search.html')
@app.route('/')
def index():
	context = {'text': '', 'user_id':''}
	return render_template('search.html', context=context)
@app.route('/search', methods=['GET'])
def search():
	# 需要从request对象读取表单内容
	user_id = request.args.get('user_id');
	text = ''
	if not user_id:
		pass
	else:
		url = 'http://123.59.169.36/rest/n/user/search?'
		parms = {
			'user_name': user_id,
			'token': '2a2e13a2da2b4d76b96e7699a1ba6655-643616180',
			'os': 'android',
			'client_key': '3c2cd3f3',
		}	
		
		resp = KsRequest(url, parms).send()
		
	# 获取用户信息
	data_json = json.loads(resp.text)
	# print(data_json)
	context = {'text': data_json, 'user_id': user_id}

	return render_template('search.html', context=context)


@app.route('/detail/<user_id>')
def detail(user_id):
	if not user_id:
		pass
	else:
		url = 'http://123.59.169.36/rest/n/user/profile/v2?'
		parms = {
			'user': user_id,
			'token': '2a2e13a2da2b4d76b96e7699a1ba6655-643616180',
			'os': 'android',
			'client_key': '3c2cd3f3',
		}

		resp = KsRequest(url, parms).send()

		url_feed = 'http://123.59.169.36/rest/n/feed/profile2?'
		parms_feed = {
			'token': '2a2e13a2da2b4d76b96e7699a1ba6655-643616180',
			'user_id': user_id,
			'lang': 'zh',
			'count': '30',
			'privacy': 'public',
			'referer': 'ks%3A%2F%2Fself',
			'os': 'android',
			'client_key': '3c2cd3f3'
		}

		resp_feed = KsRequest(url_feed, parms_feed).send()
	data_json = json.loads(resp.text)
	data_feed = json.loads(resp_feed.text)
	# print(data_json)
	context = {'text': data_json, 'user_id': user_id, 'feed': data_feed}
	return render_template('detail.html', context=context)




if __name__ == '__main__':
	app.run(debug=True)
