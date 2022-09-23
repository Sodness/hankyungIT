from flask import Flask, render_template, request, redirect, url_for
# mysql 사용을 위해 라이브러리 가져오기
import pymysql

# db에 접속
db = pymysql.connect(host='localhost', 
                     port=3306, 
                     user='root', 
                     password='tiger', 
                     database='newdata',
                     charset='utf8')
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('form.html', title='처음')

@app.route("/quiz1/<username>")
def quiz1(username):
    return render_template('quiz1.html', username=username)

@app.route("/quiz2", methods=['GET', 'POST'])
def quiz2():
    print('quiz2')
    if request.method == 'GET':
        print('get')
        return render_template('quiz2.html')
    if request.method == 'POST':
        print('post')
        # dan = request.form['dan']
        dan = request.form.get('dan')
        print(dan)
        return render_template('quiz2.html', dan=dan)

@app.route("/gugudan", methods=['GET', 'POST'])
def quiz2_action():
    if request.method == 'GET':
        return render_template('quiz2.html')
    if request.method == 'POST':
        # dan = request.form['dan']
        dan = request.form.get('dan')
        return render_template('quiz2.html', dan=dan)

@app.route("/namelist/<username>")
def namelist(username):
    return render_template('namelist.html', user=[username,'aaa', 10])

@app.route("/first")
def first():
    return render_template('form1.html')

@app.route("/login")
def login():
    return "<p>login</p>"

# @app.route("/login_process", methods=["GET"])
# def login_process():
#     print(request.args)
#     username = request.args['username']
#     pwd = request.args['pwd']
#     if username == 'aaa' and pwd == '111':
#         return "로그인되었습니다."
#     else:
#         return "다시 로그인하세요."

# @app.route("/login_process", methods=["POST"])
# def login_process_post():
#     print(request.form)
#     username = request.form['username']
#     pwd = request.form['pwd']
#     if username == 'aaa' and pwd == '111':
#         return "로그인되었습니다."
#     else:
#         return "다시 로그인하세요."

@app.route("/login_process", methods=["GET", "POST"])
def login_process():
    if request.method == "GET":
        #print(request.args)
        username = request.args['username']
        pwd = request.args.get('pwd')
        if username == 'aaa' and pwd == '1111':
            return redirect("/")
        else :
            return redirect("/login")
    elif request.method == "POST":
        username = request.form['username']
        pwd = request.form.get('pwd')
        data = [username, pwd]

        cur = db.cursor()
        sql = 'select * from users where userid = %s and pwd = %s;'
        res = cur.execute(sql, data)
        if res == 1:
            return redirect(url_for('hello_world'))
        else :
            return redirect(url_for('login'))


@app.route("/user/<userid>", methods=['GET', 'POST'])
def user(userid):
    if request.method == 'GET':
        db = pymysql.connect(host='localhost', 
                     port=3306, 
                     user='root', 
                     password='tiger', 
                     database='newdata',
                     charset='utf8')
        print('get')
        cur = db.cursor()
        data = [userid]
        print(data)
        sql = 'select username from users where userid = %s;'
        res = cur.execute(sql, data)
        print(res)
        username = cur.fetchone()[0]
        print(username)
        db.close()
        return render_template('info.html', username=username, userid=userid)
        # return 'get'
    elif request.method == 'POST':
        print('post')
        telno = request.form['telno']
        cur = db.cursor()
        data = [telno, userid]
        print(data)
        sql = 'update newdata.users set telno=%s where userid=%s;'
        res = cur.execute(sql, data)
        print(res)
        db.commit()
        if res == 1:
            db.close()
            return 'success'
        elif res == 0:
            db.close()
            return 'failed'
    

@app.route("/fileServer")
def fileServer():
    return "<p>fileServer</p>"


if __name__ == '__main__':
    app.run(port='5100', debug=True)