from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/v1/<word>")
def api(word):
    uppercase_word = word.upper()
    json_format = {"word": word,
                   "uppercase": uppercase_word}
    return json_format

print(__name__)
if __name__ == '__main__':
    app.run(debug=True, port=5001)