from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

#플라스크 애플리케이션을 생성하는 코드
#__name__ 이란 변수에 모듈명이 담김
#현재 페이지는 pybo.py 라는 모듈이 실행되기에, pybo라는 문자열이 담김



def create_app(): #애플리케이션 팩토리 -> app객체를 생성하는 함수
                    #app 객체를 전역으로 설정하면 순환참조같은 문제가 생긴덴다...
                    #그래서 애플리케이션 팩토리 안에서 선언하도록 한다.
                    #create_app 이라는 이름으로만 선언해야 함. 플라스크 내부에서 정의 된 함수임
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models


    # 블루프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)


    return app


