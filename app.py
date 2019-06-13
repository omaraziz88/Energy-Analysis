from flask import Flask, jsonify, render_template
app = Flask(__name__)

topics = [
    "Consumption",
    "Production",
    "Emissions"
]

@app.route("/")
def index():
    """Energy Evolution"""
    return render_template("index.html")

#api route for data to go to client
@app.route("/ee/topics")

# define function
def maindata():
    return jsonify(topics)

if __name__ == "__main__":
    app.run()

