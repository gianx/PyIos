PyIos
=====

This is a simple Python script (no external libraries needed) to download latest iOS firmware.

It uses [IJC](https://www.icj.me) API to query Apple servers and return the right url to download.

Easy to use, you've only to specify the list of device you want the software according to this example:
    
    models = ['iPad3,3','iPhone4,1']

... and the path where you want the file will be downloaded:

    downpath = "./"

At the end, run the script
