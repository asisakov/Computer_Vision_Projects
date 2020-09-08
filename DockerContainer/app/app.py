from flask import Flask, send_file
from plotdata import regression_plot

"""
Flask application placed in localhost:5000
"""

app = Flask(__name__) # if it runs standalone, the app will be assigned main

@app.route('/', methods=['GET']) # get from user/browser request
def regr_plot():
    image = regression_plot()

    return send_file(image,
                     attachment_filename='regplot.png',
                     mimetype='image/png')

if __name__ == '__main__':
    """
    If it is running as standalone application, it will 
    run in host http://0.0.0.0:5000/
    """
    app.run(host='0.0.0.0', debug=False)