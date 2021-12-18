from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://username:password@localhost:5432/trains"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

inner_db = SQLAlchemy(app)

association_table = inner_db.Table('association', inner_db.Base.metadata,
                                   inner_db.Column('train_id', inner_db.Integer, inner_db.ForeignKey(
                                       'train.id'), primary_key=True),
                                   inner_db.Column('time_id', inner_db.Integer, inner_db.ForeignKey(
                                       'time.id'), primary_key=True)
                                   )


class Train(inner_db.Model):
    __tablename__ = 'trains'

    id = inner_db.Column(inner_db.Integer(), unique=True, primary_key=True)
    name_id = inner_db.Column(inner_db.String(4), unique=True)
    times = inner_db.relationship("Time", secondary=association_table, back_populates="trains",
                                  cascade="all, delete",
                                  passive_deletes=True
                                  )

    def __init__(self, id, times):
        self.id = id
        self.times = times

    def save_to_db(self):
        inner_db.session.add(self)
        inner_db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


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
