#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
import os
import datetime

models = ['iPad3,3']
baseurl = 'http://api.ios.icj.me/v2/$MODEL$/latest/url'
downpath = "./"

def download(url,interactive=True):
	chunksize = 1024
	filenameTemp = url.split('/')[-1]+'.temp'
	filenameFinal = filenameTemp[:-5]
	sizeK = int(requests.head(url).headers['content-length'])/1024
	sizeM = sizeK/1024
	starttime = datetime.datetime.now()
	try:
		r = requests.get(url, stream=True)
		f = open(filenameTemp, 'wb')
		for chunk in enumerate(r.iter_content(chunk_size=1024)): 
			if chunk: # filter out keep-alive new chunks
				f.write(chunk[1])
				f.flush()
				os.fsync(f)
				if interactive:
					downloadedK= chunk[0]*chunksize/1024
					downloadedM=downloadedK/1024
					downloaded_perc = downloadedK * 100 / sizeK
					out = "Downloading %s for %s     [%s] %s Mb of %s Mb (%s)" % (model, filenameFinal, chunk[0], downloadedM, sizeM, downloaded_perc)
					sys.stdout.write("\r\x1b[K"+out)
					sys.stdout.flush()
	except KeyboardInterrupt:
		os.remove(filenameTemp)
		if interactive:
			print "\nDownload interrupted and file removed."
		sys.exit()
	os.rename(filenameTemp,filenameFinal)


for model in models:
	url = requests.get(baseurl.replace('$MODEL$',model)).text.strip()
	if url:
		download(url)
	else:
		print "Unable to find any firmware for '%s'"%(model)
	



	