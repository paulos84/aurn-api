from flask import Flask
import pymysql

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)