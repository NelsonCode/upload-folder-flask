from flask import Flask
from flask_cors import CORS
from routes import routes_folder
app = Flask(__name__)
app.register_blueprint(routes_folder)

CORS(app)



if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
    