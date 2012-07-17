'''
takes the image links and putting them into a couch db

input from stdin, list of links

you can change 'pple_training' to be whatever name 
makes sense for your application

'''

import couchdb
import sys

def start_db(name):
	couch = couchdb.Server()
	try: 
		db = couch.create(name)
	except:
		print 'db exists, opening...'
		db = couch[name]
	return db


def file_to_list(infile):
	file = open(infile,'r')
	return [line.strip() for line in file]


if __name__=="__main__":
	db = start_db('pple_training')
	
	for line in sys.stdin.readlines():
		src = line.strip()
		d = {}
		d['src'] = src
		db.save(d)
