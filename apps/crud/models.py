from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash
# from werkzeug.security import generate_password_hash

today=datetime.now

# flask db init -> 데이터베이스 초기화
# flask db migrate
# flask db upgrade

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
    

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index = True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    createDate = db.Column(db.DateTime, default=today)
    updateDate = db.Column(db.DateTime, default=today, onupdate=datetime.now)

    # 비밀번호를 설정하기 위한 프로퍼티
    @property
    def password(self):
        raise AttributeError("읽어 들일 수 없음")
    # 비밀번호를 설정하기 위해 setter 함수로 해시화한 비밀번호를 설정한다.
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)