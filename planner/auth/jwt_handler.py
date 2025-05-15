from datetime import datetime, timedelta
from jose import jwt

SECRET_KET = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(
    data : dict, expires_delta: timedelta = None
):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode, SECRET_KET, algorithm = ALGORITHM)

def create_refresh_token(
    data : dict
):
    expire = datetime.utcnow() + timedelta(days=7)
    data.update({"exp" : expire})
    return jwt.encode(data, SECRET_KET, algorithm = ALGORITHM)