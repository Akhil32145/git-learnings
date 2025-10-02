from __future__ import annotations

import os
import time
from pathlib import Path

import psutil
from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder="templates")  


@app.route("/")
def index(): 
    return render_template("index.html")  


@app.route("/metrics")
def metrics():
   
    cpu = psutil.cpu_percent(interval=0.2)  
    mem = psutil.virtual_memory().percent  
    return jsonify(cpu_percent=cpu, mem_percent=mem, ts=time.time())  

if __name__ == "__main__":
   
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)