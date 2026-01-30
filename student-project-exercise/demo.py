from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/v1/<word>")
def api(word):

    definition = df.loc[df['word'] == word]['definition']
    print(definition)
    if definition.empty:
        return {"word": word, "definition": f"{word} is not in the list"}

    json_format = {"word": word,
                   "definition": definition.iloc[0]}
    return json_format


if __name__ == '__main__':
    app.run(debug=True, port=5001)