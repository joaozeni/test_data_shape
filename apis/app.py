from flask import Flask, request

#from apis.models.model import db
from apis.healthcheck import healthcheck_blueprint


def create_app(app_name='SENSORS', test_config=False, production_conf=False):
    app = Flask(app_name)
    #swagger = Swagger(app)
    app.config.from_object('config.Config')

    # Register api blueprints
    app.register_blueprint(healthcheck_blueprint)

    from apis.models.model import db
    db.init_app(app)

    return app


#if __name__ == "__main__":
#    app = create_app(production_conf=False)
#    app.run(host="0.0.0.0", port='5000', debug=True)
