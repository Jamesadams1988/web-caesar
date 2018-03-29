from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method='POST'>
        <label>Rotate by:
            <input type="text" name="rot" value="0" />
            <p>
            <input type="textarea" name="text"  />
            </p>
            <p>
            <input type="submit"/>
            </p>
        </label>
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rots = request.form['rot']
    rots = int(rots)
    texts = request.form['text']
    texts = rotate_string(texts, rots)
    return "<h1>" + texts + "</h1>"


app.run()