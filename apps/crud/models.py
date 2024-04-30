from datetime import datetime

from apps.app import db
# from werkzeug.security import generate_password_hash

today=datetime.now

# db.Model을 상속한 Memo 클래스를 작성한다
class WorkOut(db.Model):
    # Tablename
    __tablename__="workout"
    # column
    id = db.Column(db.Integer, primary_key = True) 
    exName = db.Column(db.String)
    weight = db.Column(db.Integer)
    repeat = db.Column(db.Integer)
    setRp = db.Column(db.Integer)
    text = db.Column(db.Integer)
    createDate =db.Column(db.DateTime, default=today)
