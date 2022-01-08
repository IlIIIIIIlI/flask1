## integrate things together and then input to python
# needs to import to here to make everything run
from flask import Flask

app = Flask(__name__)

from app import views
from app import admin_views
