from flask import Flask
SHIPPING_MANAGMENT="arriving soon"

@app.route("/")
def home():
  return "welcome"
