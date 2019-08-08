from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, static_url_path='', template_folder='static')
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
