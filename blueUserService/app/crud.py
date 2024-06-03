from app.models import User, Profile, database
from app.core.security import get_password_hash


def get_all_users():
    return User.query.all()


def get_user_by_email(email: str) -> User:
    return User.query.filter_by(email=email).first()


def get_user_by_username(username: str) -> User:
    return User.query.filter_by(username=username).first()


def create_user(data: dict) -> User:
    hashed_password = get_password_hash(data["password"])

    user = User(
        first_name=data["first_name"],
        last_name=data["last_name"],
        username=data["username"],
        email=data["email"],
        password=hashed_password
    )

    database.session.add(user)
    database.session.commit()

    return user


def get_user(user_id: int) -> User:
    return User.query.get(user_id)


def create_profile(user_id: int, data: dict) -> Profile | None:
    user = get_user(user_id)

    if not user:
        return None

    profile = Profile(
        user_id=user_id,
        gender=data.get("gender"),
        eu_size=data.get("eu_size"),
        post_address=data.get("post_address"),
        city=data.get("city"),
        region=data.get("region"),
        country=data.get("country"),
        phone=data.get("phone")
    )

    database.session.add(profile)
    database.session.commit()

    return profile


def update_profile(user_id: int, data: dict) -> Profile | None:
    profile = Profile.query.filter_by(user_id=user_id).first()

    if not profile:
        return None

    profile.gender = data.get("gender", profile.gender)
    profile.eu_size = data.get("eu_size", profile.eu_size)
    profile.post_address = data.get("post_address", profile.post_address)
    profile.city = data.get("city", profile.city)
    profile.region = data.get("region", profile.region)
    profile.country = data.get("country", profile.country)
    profile.phone = data.get("phone", profile.phone)

    database.session.commit()

    return profile
