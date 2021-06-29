from flask import Flask

app = Flask(__name__)

i = 0

@app.route("/")
def hello_world():
    global i
    i = i + 1
    return "<p>You are the number <b><i>" + str(i) + "</i></b> person that visited this site.</p>"
    


app.run(debug=True)