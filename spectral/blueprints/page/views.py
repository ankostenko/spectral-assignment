from flask import Blueprint, render_template, jsonify

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def home():
    return render_template('page/home.html')

@page.route('/request_data', methods=['GET'])
def request_data():
    return jsonify({"hello": "world!"})