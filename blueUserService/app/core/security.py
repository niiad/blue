from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return password_context.hash(password)


def verify_password(plain: str, cipher: str):
    return password_context.verify(plain, cipher)
