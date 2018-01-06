from webapp import app
import flask
import html_parser as hp

# importing application wide parameters and global variables that have been
# defined in __init__.py

@app.route('/')
def webapp():
    return flask.render_template('index.html')

@app.route('/parser/', methods=["POST"])
def parser():
	url = flask.request.form['url']
	message = hp.parse_link(url)
	return flask.jsonify({"message": message})
