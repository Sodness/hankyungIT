# flask + mediapipe 손가락 인식 + HTML,CSS,Javascript

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def mediapipe():
    return render_template('hands_1.html')

if __name__ == '__main__':
    app.run(port='5100', debug=True)




