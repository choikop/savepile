from flask import render_template, Flask, request, url_for
from apps import app

from google.appengine.ext import db

class Photo(db.Model):
	photo = db.BlobProperty()
	string = db.StringProperty(default='', multiline=True)



def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

	return '.' in filename and \
	filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
	return render_template("upload.html", all_list=Photo.all())



@app.route('/upload', methods=['POST'])
def upload_db():
	post_data = request.files['photo']
	text_data = request.forms['string']

	if post_data and allowed_file(post_data.filename) and text_data:
		filestream = post_data.read()

		upload_data = Photo()
		upload_data.photo = db.Blob(filestream)
		upload_data.put()	

		comment = "uploaded!"

	
	else:
		comment = "please upload valid image file"


	return render_template("upload.html", text_data=text_data, comment=comment, all_list=Photo.all())



@app.route('/show/<key>')
def shows(key):
	uploaded_data = db.get(key)
	return app.response_class(uploaded_data.photo)


