from re import T
from flask import Flask
from os import path
from .config import Config
app = Flask(__name__)

def Create_App(ocnfig_class = Config):
    app =  Flask(__name__, static_folder = 'static')
    app.config.from_object(Config)

    from SkinCancer_Flask.main.routes import main
    from SkinCancer_Flask.realtime.routes import realtime
    from SkinCancer_Flask.detection.routes import detection
    from SkinCancer_Flask.info_ungthuda.routes import infoUngThuDa

    app.register_blueprint(main)
    app.register_blueprint(realtime)
    app.register_blueprint(detection)
    app.register_blueprint(infoUngThuDa)

    return app
