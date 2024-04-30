from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# create_app 함수를 작성한다
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    #플라스크 인스턴스 생성
    app = Flask(__name__)
    # 앱의 config 설정
    app.config.from_mapping(
        SECRET_KEY = "ASDASDASD",
        SQLALCHEMY_DATABASE_URI=
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATON=False,
        # SQL을 콘솔로그에 출력
        SQLALCHEMY_ECHO = True,
        WTF_CSRF_SECRET_KEY ="ASDASDASD"
    )
    # SQLAlchemy와 앱 연계
    db.init_app(app)
    # Migrate와 앱 연계
    Migrate(app, db)
    csrf.init_app(app)

    # crud 패키지로부터 views를 import한다
    from apps.crud import views as crud_views

    # register_blueprint를 사용해 views의 crud를 앱에 등록한다
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app