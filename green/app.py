from flask import Flask
app = Flask(__name__)

@app.route('/')
def green_app():
    return "This is the Green version of the app (v2.0)"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

