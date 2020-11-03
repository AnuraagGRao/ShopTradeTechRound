# -------------- Imports -----------------

from flask import Flask, request, jsonify
from tool.settings import Config, Secret

# -------------- init.py  ----------------

application = app = Flask(__name__)

app.config.from_object(Config)

sk = Secret

# ----------------------------------------

from tool.routes import *

# ----------------------------------------