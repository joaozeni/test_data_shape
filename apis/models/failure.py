from apis.models.model import db


class failure(db.Model):
    __tablename__ = 'failures'

    id = db.Column(db.BigInteger, primary_key=True)
    sensor_id = db.Column(db.BigInteger, db.ForeignKey('sensors.id'))
    equipment_id = db.Column(db.BigInteger, db.ForeignKey('sensors.id'))# added for fast use, calculated during the upload
    failure_date = db.Column(db.DateTime)
    temperature = db.Column(db.Float)
    vibration = db.Column(db.Float)

