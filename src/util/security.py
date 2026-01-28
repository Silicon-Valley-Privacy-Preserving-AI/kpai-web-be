from passlib.context import CryptContext
from src.config.environments import SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compare plain password with hashed password."""
    return pwd_context.verify(plain_password + SECRET_KEY, hashed_password)

def get_password_hash(password: str) -> str:
    """Hashs the password"""
    return pwd_context.hash(password + SECRET_KEY)