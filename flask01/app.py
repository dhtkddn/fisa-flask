#입구 파일을 만들어줍니다
#flask run --debug --port 5001
#debug모드 off이면 app.route('/')안의 값을 app.rout('/hello')로 바꿔도 안의 localhello주소 바로 변경 안됨
# 입구 파일을 만들어줍니다

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from views.main_views import mbp  # Blueprint 가져오기
from views.board_views import cbp

from views.config import config

db=SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM을 적용
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(mbp)  # Blueprint 등록
    app.register_blueprint(cbp)
    
    return app

# 아래 코드는 create_app() 안에 넣으면 안 됨
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)

