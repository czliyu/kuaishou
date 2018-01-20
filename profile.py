#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests

import hashlib, json



def HttpResponse(user_id):

	url = 'http://123.59.169.36/rest/n/user/search?'
	querystring = 'app=0&lon=0&c=360APP&sys=ANDROID_4.4.4&mod=samsung(SMG9350)&did=ANDROID_1058046460253831&ver=5.2&net=WIFI&country_code=CN&appver=5.2.3.4792&oc=UNKNOWN&ftt=&ud=643616180&language=zh-cn&lat=0'

	data = "user_name=" + user_id + "&token=2a2e13a2da2b4d76b96e7699a1ba6655-643616180&os=android&client_key=3c2cd3f3"

	sig = del_sig(querystring + '&' + data)

	tokensig = get_token(sig)

	print(sig + '\n' + tokensig)

	parms = {
		'user_name': user_id,
		'token': '2a2e13a2da2b4d76b96e7699a1ba6655-643616180',
		'__NStokensig': tokensig,
		'os': 'android',
		'client_key': '3c2cd3f3',
		'sig': sig
	}

	resp = requests.post(url + querystring, data=parms)
	return resp

def del_sig(text):
	# 获取数据后用‘&’来分割数组
	text = text.replace('+', '')
	list_data = text.split('&')
	data = ''.join(sorted(list_data))
	#print(get_md5(data))
	return get_md5(data)
	

def get_md5(text):
	md5 = hashlib.md5()
	md5.update((text + '382700b563f4').encode('utf-8'))
	return md5.hexdigest()


def get_token(sig):
	has256 = hashlib.sha256()
	has256.update((sig + 'cbf8f8efe57db87cbec65db3959fa200').encode('utf-8'))
	return has256.hexdigest()

if __name__ == '__main__':
	resp = HttpResponse('Yuebaobao8989')
	print(resp.text)


