' 快手 发送请求类 '

__author__ = 'poppy'

import requests

import hashlib, json

class KsRequest(object):

	def __init__(self, url, data):
		self.url = url
		self.queryString = "app=0&lon=0&c=360APP&sys=ANDROID_4.4.4&mod=samsung(SMG9350)&did=ANDROID_1058046460253831&ver=5.2&net=WIFI&country_code=CN&appver=5.2.3.4792&oc=UNKNOWN&ftt=&ud=643616180&language=zh-cn&lat=0"
		self.data = data
		self.data_to_str()
		self.del_sig()
		self.get_token()


	def data_to_str(self):
		''' data dict 转换成 str类型 '''
		self.data_str = ''
		data_str = ''
		for key, value in self.data.items():
			data_str += key+'='+value+'&'
			self.data_str = data_str.strip('&')



	def del_sig(self):
		# 获取数据后用‘&’来分割数组
		text = self.queryString + '&' + self.data_str
		text = text.replace('+', '')
		list_data = text.split('&')
		data = ''.join(sorted(list_data))
		#print(get_md5(data))
		self.get_md5(data)
	

	def get_md5(self, data):
		md5 = hashlib.md5()
		md5.update((data + '382700b563f4').encode('utf-8'))
		self.sig = md5.hexdigest()
		self.data['sig'] = self.sig
		


	def get_token(self):
		has256 = hashlib.sha256()
		has256.update((self.sig + 'cbf8f8efe57db87cbec65db3959fa200').encode('utf-8'))
		tokensig = has256.hexdigest()
		self.tokensig = tokensig
		self.data['__NStokensig'] = self.tokensig

	def send(self):
		resp = requests.post(self.url + self.queryString, data=self.data)
		return resp

		