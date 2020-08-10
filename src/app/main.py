from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
from flask import render_template
import os
import sys
sys.path.append(os.getcwd)

def make_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/report")
    def report():
        return render_template('report_page.html')

    @app.route("/report_data", methods = ["POST"])
    def report_data():
        short_description = request.headers.get('short_description')
        description = request.headers.get('description')


        return jsonify({"status": "success"})


    return app