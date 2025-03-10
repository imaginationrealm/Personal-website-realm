from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()
import datetime as dt
import os
import smtplib

PORT = os.getenv('PORT')
MY_EMAIL = "kibetpeter95@gmail.com"
PASSWORD = "rissnibgzstkmfhy" 

app = Flask(__name__)
CORS(app)

@app.route("/api")
def home():
    return { "msg": "Home" }


@app.route("/api/contact")
def contact():
    return { "msg": "Contact" }

@app.route("/api/date_year")
def date_year():
    now = dt.datetime.now()
    year = now.year
    print(year)
    return { "msg": year }

@app.route("/api/experience")
def experience():
    python_exp = 5
    js_exp = 4
    return {"python_exp": python_exp, "js_exp": js_exp }

@app.route("/api/mail", methods=["GET", "POST"])
def mail():
    contact_name = request.json.get("name")
    email = request.json.get("email")
    message = request.json.get("message")
    print(contact_name, email, message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: FROM {contact_name} \n\n {message}"
        )
    return { "msg": f"Thanks {contact_name} your message has been sent!" }

@app.route("/api/hire", methods=["GET", "POST"])
def hire():
    location = request.json.get('location')
    email = request.json.get('email')
    address = request.json.get('address')
    city = request.json.get('city')
    country = request.json.get('country')
    code = request.json.get('code')
    print(location, email, address, city, country, code)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: YOU ARE HIRED! \n\n Location: {location}, Email: {email}, Address: {address}, City: {city}, Country: {country}, Code: {code}"
        )

    return { "msg": "Thanks message sent" }, 200



