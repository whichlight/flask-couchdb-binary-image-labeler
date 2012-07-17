flask couchdb binary image labeler
===================================

This is a binary image labeler written written with the Flask python
microframework, using CouchDB to hold the image data.  You can choose
a particular attribute and use this app to cycle through them and label them
yes or no. 

You can view all of the labeled images as well, with the positives highighted. 

I made this tool to make it easier to cycle through and label images in order to
have a training set for machine learning and computer vision applications. 

To update an image, you can also POST to "/" with the attributes id for the
image id and p as 0 or 1 as true or false if the image has the attribute. 


getting started
---------------

As a quick example, you can get started with images from instagram. 
In this example I am classifying images for people.

You'll need a few things installed for this example. I use a node script to
download the images, so have node and npm installed.  I'm using python2.7 here,
but I imagine 2.6 works as well.  Have couchdb installed, and install
python-couchdb. Also install flask.  You can use pip for the python packages. 

First we need to get a set of images. To collect images run `node pull_images.js > output.txt` 

This collects image links and save them in output.txt.  The script looks up images
every 5 seconds, so stop it when you have enough. 

Navigate to /static/images and run ./process_output.sh to download only the
instagram images.  

Now we can put the images names into the db. Use `ls *.jpg` to get a list of the images, and pipe that to `python
images_into_couch.py`.  This saves all of the image names into the database to
access in the app.  

With the images downloaded and names in the db, we can go ahead and get started
on labeling.  Run `python server.py` to start the Flask app. Go to localhost:5000 to start
labeling. This will automatically pull up an unlabeled image.  You can click
'yes' or 'no' if is has the attribute, or press 'y' or 'n'.

Note
-----
Things you will want to edit for your own purposes:
* the title question of the labeled page to be specific to whatever attribute
you're looking for
* change the attribute in the couchdb.  Right now I use isperson since I am
labeling whether or not there is a person in the image. 
* change the db name to whatever makes sense for your application.  This can be
done in the images_into_couch script. I call mine pple_training since thats the
classifier I'm collecting for. 
 
author
------
kawandeep virdee, @kawantum
