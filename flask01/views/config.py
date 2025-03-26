# views/config.py

import os

BASE_DIR = os.path.dirname(__file__)

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

# app.py에서 불러올 수 있도록
config = Config
