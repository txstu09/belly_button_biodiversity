#----------------------------
# IMPORTS
#----------------------------
import pandas as pd

from flask import Flask

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

#----------------------------
# SQLALCHEMY SETUP
#----------------------------
engine = create_engine("sqlite:///datasets/belly_button_biodiversity.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

otu = Base.classes.otu
samples = Base.classes.samples
samples_meta = Base.classes.samples_metadata

session = Session(engine)
inspector = inspect(engine)

#----------------------------
# BUILD FLASK ROUTES
#----------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return #dashboard homepage


@app.route('/names')
def names():
    return #list of sample names

@app.route('/otu')
def otu():
    return #list of OTU descriptions

@app.route('/metadata/<sample>')
def metadata():
    return #metadata for given sample

@app.route('/wfreq/<sample>')
def wfreq():
    return #weekly washing freq. as a number

@app.route('/samples/<sample>')
def samples():
    return #OTU IDs & sample values for given sample

if __name__ == '__main__':
    app.run()