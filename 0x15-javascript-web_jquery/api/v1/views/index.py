#!/usr/bin/python3
import requests
from api.v1.views import app_views
from flask import render_template, jsonify as js

@app_views.route('/status', methods=['GET'])
def status_api():
    return js({"status": "OK"})


@app_views.route('/heroes', methods=['GET'])
def heroes():
    return render_template('heroes.html')


@app_views.route('/translate', methods=['GET'])
def test_jquery():
    return render_template('0-main.html')

@app_views.route('/native-hello/<language_code>')
def proxy(language_code):
    uri = f'https://hellosalut.stefanbohacek.dev/?lang={language_code}'
    response = requests.get(uri)
    return js(response.json())
