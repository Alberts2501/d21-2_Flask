from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")

def getIndex():
  return "<h1><a href='/about'>Alberts Korols</a></h1>"

@app.route('/home')
def home():
  return  render_template('home.html')

@app.route("/about")
def getAbout():
  return render_template('about.html')

@app.route("/contact")
def contact():
  return render_template('contact.html', phone = 87654321)


@app.route("/contact2")
def contact2():
  return render_template('contact.html', phone = 12345678)

  
app.run(host = '0.0.0.0', port=8020)