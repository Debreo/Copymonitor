import os
import shutil
import errno
import hashlib
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler  


src = os.path.realpath("C:\\path\\to\\src\\folder") #src directory
dst = os.path.realpath("C:\dst") #dst directory


class dirwatcher(PatternMatchingEventHandler):
	patterns = ["*.exe",".msi","*.dll"] # patterns to watch for 
   	def process(self, event):
		if event.event_type == "created" or event.event_type == "modified":
			dst_file = os.path.join(dst,os.path.basename(event.src_path))
			if not os.path.isfile(dst_file):
				try:
					shutil.copy(event.src_path,dst)
				except IOError as e:
					print "Error {}".format(e)

   	def on_modified(self, event):
   		self.process(event)

	def on_created(self, event):
		self.process(event)

	def on_moved(self, event):
		self.process(event)
	def on_deleted(self, event):
		self.process(event)


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
	observer = Observer()
	event_handler = LoggingEventHandler()
	observer.schedule(dirwatcher(), path=src, recursive=True)
	observer.schedule(event_handler, path=src, recursive=True)
	observer.start()


	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()

	
	observer.join()