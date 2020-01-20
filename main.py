from flask import Flask, render_template

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

if __name__ == '__main__':
  app.run(threaded=True, port=5020, debug=True)