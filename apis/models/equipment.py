from apis.models.model import db


class equipment(db.Model):
    __tablename__ = 'equipments'

    id = db.Column(db.BigInteger, primary_key=True)
    code = db.Column(db.String(8))
    group_name = db.Column(db.String(8))

