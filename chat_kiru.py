from flask import Flask, render_template, jsonify

from chattt import response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/answer")
def answer():
    text = request.get_json().get("message")
    responded=response(text)
    message={"answer":response}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)