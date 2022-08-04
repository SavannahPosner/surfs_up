from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/girlboss/', methods = ['GET','POST'])
def upload_image():
    return render_template('index_html')

