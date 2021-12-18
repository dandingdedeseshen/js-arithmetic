# !/url/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'waiting'
import os, re, codecs, urllib, io, gzip, zlib
from urllib import request
from bs4 import BeautifulSoup
import chardet


class SpiderHTML(object):
	# 打开页面
	def getUrl(self, url, coding='utf-8'):
		req = request.Request(url)
		req.add_header('User-Agent',
					   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
		req.add_header('Accept-encoding', 'gzip')
		with request.urlopen(req) as response:
			gzipd = response.headers.get('Content-Encoding')
			if gzipd == 'gzip':
				data = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS)

			else:
				data = response.read()
			return BeautifulSoup(data)

	# 保存文本内容到本地
	def saveText(self, filename, content, mode='w'):
		self._checkPath(filename)
		with codecs.open(filename, encoding='utf-8', mode=mode) as f:
			f.write(content)

	# 保存图片
	def saveImg(self, imgUrl, imgName):
		data = request.urlopen(imgUrl).read()
		self._checkPath(imgName)
		with open(imgName, 'wb') as f:
			f.write(data)

	# 创建目录
	def _checkPath(self, path):
		dirname = os.path.dirname(path.strip())
		if not os.path.exists(dirname):
			os.makedirs(dirname)
