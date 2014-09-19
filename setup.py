from distutils.core import setup
import py2exe
import glob


data_files = [("selenium/webdriver/firefox", ["webdriver_prefs.json", "webdriver.xpi"])]

setup(
	console=['automatedcheckout.py'],
	data_files = data_files,
	options ={
		'py2exe':{
			"optimize": 1,
			"bundle_files": 3,
			"skip_archive": True
      }})