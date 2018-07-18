import os
import requests
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return render_template('docs.html')


@app.route('/jobs/')
def jobs():
    jobs_data = requests.get('https://jobs.github.com/positions.json')
    response = app.response_class(
        response=jobs_data,
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
