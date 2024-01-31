from database import db
from datetime import datetime
import pytz

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default = datetime.now(pytz.timezone('Asia/Tokyo')).replace(second=0, microsecond=0))