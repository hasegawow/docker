# SQLAlchemyを使ってDBを操作できるようにするツール
from flask_sqlalchemy import SQLAlchemy
# マイグレーションは、DBの生成や変更履歴を管理するためのツール
from flask_migrate import Migrate

# DBを操作するためのオブジェクト生成
db = SQLAlchemy()

# flaskのappオブジェクトを受け取って、初期化（=SQLAlchemy、Migrateを使うための準備）をする関数
def init_db(app):
    db.init_app(app)
    Migrate(app, db)