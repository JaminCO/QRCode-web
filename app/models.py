from .extensions import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class QRcode(db.Model):
    __tablename__ = "qr_codes"
    id = db.Column(db.Integer, primary_key=True)
    storage_path = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"< QRcode {self.storage_path} >"


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(1000)) # long hash, not literal password
    qr_codes = db.relationship(QRcode, backref="user", lazy="dynamic")

    def __repr__(self) -> str:
        return f"< User {self.username} >"
        