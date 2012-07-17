'''
a web application allow a user to label images for a trainer

in this particular example we label whether or not the
image contains a person. 

this information is stored in a couchdb

kawandeep virdee, @kawantum, whichlight.com
'''
from flask import render_template
from flask import Flask
import flask
import couchdb

#setup
app = Flask(__name__)
couch = couchdb.Server()
db = couch['pple_training'] 


@app.route("/", methods=['GET', 'POST'])
def tolabel():
	#POST will submit label info p is 1 if true, and 0 if false, 
	#id is the db id 
	if flask.request.method == 'POST':
		id = flask.request.args['id']
		p = flask.request.args['p']
		d = db[id]
		d['isperson']=p
		db[d.id] = d

	#load an image that needs to be labeled 
	unlabeled = '''function(doc){
			if(!doc.isperson){
				emit(doc._id,doc)
				}
			}
	'''
	data = [dict(row) for row in db.query(unlabeled)]
	return render_template('label.html',pic =data[0])

@app.route("/done")
def labeled():
	map_fun = '''function(doc){
			if(doc.isperson){
					emit(doc._id,doc)
					}
			}
	''' 	
	data = [dict(row) for row in db.query(map_fun)]

	return render_template('done.html',pics = data)

if __name__=="__main__":
	app.debug = True

	app.run()

