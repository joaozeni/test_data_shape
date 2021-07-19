from apis.models.model import db


class sensor(db.Model):
    __tablename__ = 'sensors'

    id = db.Column(db.BigInteger, primary_key=True)
    equipment_id = db.Column(db.BigInteger, db.ForeignKey('equipments.id'))

