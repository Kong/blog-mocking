import requests
from flask import Flask
from logging.config import dictConfig


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route("/")
def request():
    r = requests.get("http://captains-log_my-services_svc_5000.mesh:80")
    log = r.json()

    r2 = requests.get("http://crew_my-services_svc_5000.mesh:80")
    crew = r2.json()

    output = dict(captainsLog=log, crew=crew)

    return output
