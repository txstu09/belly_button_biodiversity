from flask import Flask

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