from flask import Flask
app = Flask(__name__)

@app.route('/')
def blue_app():
    return "This is the Blue version of the app (v1.0)"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

