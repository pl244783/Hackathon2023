from flask import Flask, render_template, request, redirect, session, Response, jsonify
import cv2, math, numpy as np
import time

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=8888, threaded=True, debug=True)