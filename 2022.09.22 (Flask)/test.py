from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('form.html')

@app.route("/namelist/<username>")
def namelist(username):
    return render_template('namelist.html')

@app.route("/first")
def first():
    return render_template('form1.html')

@app.route("/login")
def login():
    return "<p>login</p>"

@app.route("/login_process", methods=["GET"])
def login_process():
    print(request.args)
    username = request.args['username']
    pwd = request.args['pwd']
    if username == 'aaa' and pwd == '111':
        return "로그인되었습니다."
    else:
        return "다시 로그인하세요."

@app.route("/login_process", methods=["POST"])
def login_process_post():
    print(request.form)
    username = request.form['username']
    pwd = request.form['pwd']
    if username == 'aaa' and pwd == '111':
        return "로그인되었습니다."
    else:
        return "다시 로그인하세요."

@app.route("/user/<username>")
def user(username):
    return "user: " + username

@app.route("/fileServer")
def fileServer():
    return "<p>fileServer</p>"


if __name__ == '__main__':
    app.run(host='192.168.4.161', port='5100', debug=True)