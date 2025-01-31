from flask import Flask,redirect,render_template,request
import random as r
from twilio.rest import Client
import time

app = Flask(__name__)

account_sid = '4811ACed5aa947afd57525662e61713f2ee3f9'
auth_token = 'dhan1178abfcbb9cdf049d6b933274413435'

client = Client(account_sid,auth_token)

@app.route("/", methods = ["GET"])
def homepage():
    return render_template("index.html")

@app.route("/smssend", methods = ["GET", "POST"])
def sms_send():
    if request.method == "POST":
        num = request.form["num"]
        n = int(request.form["n"])
        
        for i in range(n):
            otp = otps()
            try:
                message = client.messages.create(
                    body = f"we are from ......Your otp is {otp} valid for 5 sec",
                    from_ = '+12183806547',
                    to = f"+91{num}"
                    )
                print(f"OTP sent! SID: {message.sid}")
                time.sleep(2)
            except Exception as e:
                print(f"Failed to send OTP: {e}")
        return "Sent"
    return render_template("index.html")


def otps():
    return r.randint(1000,10000)

app.run(port=4811  ,debug=True)