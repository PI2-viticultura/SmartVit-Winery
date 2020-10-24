from flask import Flask
from flask_cors import CORS
from views.winery import app as winery

app = Flask(__name__)
app.register_blueprint(winery)
CORS(app, automatic_options=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
