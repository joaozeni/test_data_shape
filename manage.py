from flask_migrate import Migrate

from apis.app import create_app
from apis.models.model import db
from apis.models.equipment import equipment
from apis.models.sensor import sensor
from apis.models.failure import failure

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, equipment=equipment, sensor=sensor, failure=failure)


#if __name__ == '__main__':
#    make_shell_context()[app].run(host="0.0.0.0", port='5000', debug=True)
