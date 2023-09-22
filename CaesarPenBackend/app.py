from flask import Flask,request
from caesaremail import CaesarEmail
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route("/sendemail",methods=["POST","GET"])
def sendemail():
    try:
        if request.method == "GET":
            return "CaesarSendEmail is working"
        elif request.method == "POST":
            emailmessage = request.get_json()
            CaesarEmail.send(emailmessage["email"],emailmessage["subject"],emailmessage["message"])
            return {"message":"Email was sent"}
    except Exception as ex:
        return {"error":f"{type(ex)} - {ex}"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)