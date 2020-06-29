import os
from os import path
import sys
import _thread

mtimes = {}

def init():
	for fpath, mtime in iter_jinja2_mtimes():
		mtimes[fpath] = mtime

def check():
	changed = []
	for fpath, mtime in iter_jinja2_mtimes():
		old_mtime = mtimes.get(fpath)
		if not old_mtime or mtime > old_mtime:
			changed.append(fpath)
		mtimes[fpath] = mtime

	return changed

def iter_jinja2_mtimes():
	for dirpath, dirnames, filenames in os.walk('.'):
		for filename in filenames:
			if not filename.endswith('.jinja2'):
				continue
			fpath = path.join(dirpath, filename)
			yield fpath, os.stat(fpath).st_mtime
