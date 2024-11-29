import jwt
import datetime
from config.config import config

SECRET_KEY = config.get('SECRET_KEY')

def generate_token(user_id, expiration_minutes=60):
    """
    Generates a JWT token with an expiration time.
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
