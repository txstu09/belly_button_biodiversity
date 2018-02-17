#----------------------------
# IMPORTS
#----------------------------
import pandas as pd

from flask import Flask, jsonify

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
def sample_names():
    columns = inspector.get_columns('samples')
    names = []
    for column in columns:
        names.append(column['name'])
    del names[0]
    
    return jsonify(names)

@app.route('/otu')
def otu_descriptions():
    results = session.query(otu.otu_id, otu.lowest_taxonomic_unit_found).all()
    df = pd.DataFrame(results)

    otu_count = len(df.index)
    otu_info = []
    for x in range(otu_count):
        otu_info.append({df['otu_id'][x]: df['lowest_taxonomic_unit_found'][x]})
        
    return jsonify(otu_info)

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