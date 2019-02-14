from movie import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

class User(db.Document, UserMixin):
    meta = {'collection': 'users'}
    username = db.StringField(max_length=25, required=True)
    email = db.StringField(max_length=40, required=True)
    password = db.StringField(required=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
