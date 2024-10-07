from flask import Flask, jsonify, Request, Response, url_for, send_file, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")   

@app.get("/") 
def home():
    return render_template("homepage.html")  

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug = True ) 

