# 특정 /url/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask 객체
#코드에서 부르는 상대적 이름,실제 파일명,url에 매칭되는 경로
from flask import Blueprint

cbp = Blueprint('collection', __name__, url_prefix='/board')

@cbp.route('/no1')
def hello2():
    return f"{__name__} 첫번째"

@cbp.route('/no2')
def hello3():
    return f'{__name__} 두번째'

    