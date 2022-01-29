import imp
from flask import Flask
from .config import DevConfig

# instance of the application
app = Flask(__name__)

# setting up application configurations
app.config.from_object(DevConfig)

from app import views