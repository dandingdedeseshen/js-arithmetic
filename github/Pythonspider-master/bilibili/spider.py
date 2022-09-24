# !/url/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'waiting'
import os, re, codecs, urllib, io, gzip, zlib
import requests
from bs4 import BeautifulSoup
import chardet


class SpiderHTML(object):
	# 打开页面
	def getUrl(self, url, coding='utf-8'):
		req = requests.get(url)
		req.encoding = 'utf-8'
		req.headers = ('User-Agent',
					   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
		req.headers = ('Accept-encoding', 'gzip')
		# gzipd = req.headers.get('Content-Encoding')
		# if gzipd == 'gzip':
		# 	data = zlib.decompress(req.text, 16 + zlib.MAX_WBITS)
		#
		# else:
		# 	data = req.text
		return BeautifulSoup(req.text,'lxml')

	# 保存文本内容到本地
	def saveText(self, filename, content, mode='w'):
		self._checkPath(filename)
		with codecs.open(filename, encoding='utf-8', mode=mode) as f:
			f.write(content)

	# 保存图片
	def saveImg(self, imgUrl, imgName):
		data = requests.get(imgUrl).content
		self._checkPath(imgName)
		with open(imgName, 'wb') as f:
			f.write(data)

	# 创建目录
	def _checkPath(self, path):
		dirname = os.path.dirname(path.strip())
		if not os.path.exists(dirname):
			os.makedirs(dirname)
