from flask import Flask, request
from flasgger import Swagger

from apis.models.model import db
from apis.healthcheck import healthcheck_blueprint
from apis.data_process import data_process_blueprint


def create_app(app_name='SENSORS', test_config=False, production_conf=False):
    app = Flask(app_name)
    swagger = Swagger(app)
    app.config.from_object('config.Config')

    # Register api blueprints
    app.register_blueprint(healthcheck_blueprint)
    app.register_blueprint(data_process_blueprint, url_prefix='/data')

    db.init_app(app)

    return app


#if __name__ == "__main__":
#    app = create_app(production_conf=False)
#    app.run(host="0.0.0.0", port='5000', debug=True)
