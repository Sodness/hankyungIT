from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# 프로젝트에 활용할거 
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signlang')
def signlang():
    return render_template('signlang.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5100, debug=True)