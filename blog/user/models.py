# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt
from blog.extensions import bcrypt, db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Binary(128), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    token: str = ''

    def __init__(self, username, email, password=None):
        """Create instance."""
        self.username = username
        self.email = email
        if password:
            self.password = self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        return bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)

    @classmethod
    def get_by_id(cls, record_id):
        """Get record by ID."""
        basestring = (str, bytes)
        if any(
                (isinstance(record_id, basestring) and record_id.isdigit(),
                 isinstance(record_id, (int, float))),
        ):
            return cls.query.get(int(record_id))
