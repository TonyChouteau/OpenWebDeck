from flask import Flask, send_from_directory, render_template
from flask_session import Session

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

@app.get("/")
def home():
   return render_template("index.html")


@app.get('/dist/<path:path>')
def dist(path):
    return send_from_directory("dist", path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
