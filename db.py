from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://username:password@localhost:5432/trains"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

inner_db = SQLAlchemy(app)

association_table = inner_db.Table('association', inner_db.Base.metadata,
                                   inner_db.Column('train', inner_db.ForeignKey(
                                       'train.id'), primary_key=True),
                                   inner_db.Column('time', inner_db.ForeignKey(
                                       'time.id'), primary_key=True)
                                   )


class Train(inner_db.Model):
    __tablename__ = 'trains'

    id = inner_db.Column(inner_db.String(4), unique=True, primary_key=True)
    times = inner_db.relationship("Time", back_populates="trains",
                                  cascade="all, delete",
                                  passive_deletes=True
                                  )


class Time(inner_db.Model):
    __tablename__ = 'times'

    id = inner_db.Column(inner_db.Integer, primary_key=True)
    time = inner_db.Column(inner_db.Time)
    train = inner_db.relationship("Train", back_populates="times")


class Database:
    def __init__(self):
        self.session = inner_db

    def get(self, key):
        self.session.get
        return

    def set(self, key, val):
        return

    def keys(self):
        """ Implement a function to return database keys """
        raise NotImplementedError
