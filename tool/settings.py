# -------------- Imports --------------

from dotenv import load_dotenv
from pathlib import Path
import os

# -------------------------------------

# ------------- settings.py -----------

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config():
    
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Secret():
    API_KEY = os.getenv('API_KEY')
    API_PASSWORD = os.getenv('API_PASSWORD')
    STORE_DOMAIN = os.getenv('STORE_DOMAIN')

# --------------------------------------