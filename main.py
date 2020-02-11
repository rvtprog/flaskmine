from flask import Flask, render_template, request
from file_proc import read_file, write_file

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi"

@app.route('/home')
def home():
  return render_template("home.html")

@app.route('/about')
def about_html():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone="12345678")

@app.route('/params')
def params():
  args = request.args
  for key, value in args.items():
    print(f"(key):(value)")
  return args

@app.route('/params_table')
def params_table():
  args = request.args
  return render_template('params_table.html', args = args)

@app.route('/post', methods = ['POST'])
def post():
  return request.get_json()

@app.route('/read_file')
def read_from_file():
  content = read_file()
  return content

@app.route('/write_file', methods = ['POST'])
def write_to_file():
  content_type = request.content_type
  if content_type == 'application/json':
    contentJSON = request.get_json()
    write_file(contentJSON['data'])
    return f"add line {contentJSON['data']} to file."
  else:
    return f"Content type {content_type} is not supported"

@app.route('/file', methods = ['GET', 'POST'])
def workfile():
  if request.method == 'GET':
    return read_from_file()
  elif request.method == 'POST':
    return write_to_file()
  else:
    return f"Method {request.method} is not supported"

if __name__ == '__main__':
  app.run(threaded=True, port=5020, debug=True)