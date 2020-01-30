from flask import Flask, render_template, url_for
 #Flask knows to look in template dir for index.html

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug=True)