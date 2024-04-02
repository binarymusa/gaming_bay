
""" models or (database tables) configured here """

from game import db,login_manager
from game import bcrypt
from flask_login import UserMixin

# import hashlib
# from itsdangerous import TimedSerializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True) # primary key

    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # Foreign-key 
    #   points to a specific role in the Role's model 

    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    phone_no = db.Column(db.String(length=10) )
    password_hash = db.Column(db.String(length=128), nullable=False)


    booking = db.relationship('Booking', backref='owned_user', lazy=True) # bi-directional connection
    role = db.relationship('Roles', backref='users') # secondary='roles_id',
   
    # - -   -   -   -   -   -   -   - password security(werkzeug)
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password_attempt):
        return bcrypt.check_password_hash(self.password_hash, password_attempt)


# class Permission(db.Model):
#     FOLLOW = 0x01
#     COMMENT = 0x02
#     WRITE_ARTICLES = 0x04
#     MODERATE_COMMENTS = 0x08
#     ADMINISTER = 0x80



class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=True, unique=True)

    # @staticmethod
    # def insert_roles():
    #     roles = {
    #     'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
    #     'Moderator': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS, False),
    #     'Administrator': (0xff, False)
    # }


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False, index=True)
    console_id = db.Column(db.Integer, db.ForeignKey('console.id'), nullable=False) 
    date_id = db.Column(db.Integer, db.ForeignKey('date_slot.id'), nullable=False) 
    time_id = db.Column(db.Integer, db.ForeignKey('time_slot.id'), nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    game = db.relationship('Game', backref='bookings')
    console = db.relationship('Console', backref='bookings')
    timeslot = db.relationship('TimeSlot', backref='bookings')
    dateslot = db.relationship('DateSlot', backref='bookings')


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    console_name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)

class TimeSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    start_time = db.Column(db.Time, nullable=False, unique=True)
    end_time = db.Column(db.Time, nullable=False, unique=True)

class DateSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    date_slot = db.Column(db.Date, nullable=False, unique=False)
    



