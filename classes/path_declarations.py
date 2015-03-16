import os

APP_PATH = os.path.normpath(os.path.join(
	os.path.dirname(os.path.abspath(__file__)), 
	os.pardir))

DATA_PATH = os.path.join(APP_PATH, "data")
MODULE_PATH = os.path.join(APP_PATH, "modules")

CONFIG_PATH = APP_PATH

def config(*fname):
	return os.path.join(APP_PATH, *fname)

def data(*fname):
	return os.path.join(DATA_PATH, *fname)