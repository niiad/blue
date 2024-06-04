from app.core.database import database


class User(database.Model):
    __tablename__ = "users"
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    first_name = database.Column(database.String(25), nullable=False)
    last_name = database.Column(database.String(25), nullable=False)
    username = database.Column(database.String(30), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(128), nullable=False)
    profile = database.relationship("Profile", uselist=False, back_populates="user")


class Profile(database.Model):
    __tablename__ = "profiles"
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey("users.id"), nullable=False)
    gender = database.Column(database.String(15))
    eu_size = database.Column(database.Integer)
    post_address = database.Column(database.String(15))
    city = database.Column(database.String(20))
    region = database.Column(database.String(20))
    country = database.Column(database.String(25))
    phone = database.Column(database.String(20))
    user = database.relationship("User", back_populates="profile")
