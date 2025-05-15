from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from auth.jwt_handler import SECRET_KET, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/users/login")

def get_current_user(token : str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KET, algorithms = [ALGORITHM])
        user_email : str = payload.get("sub")
        if user_email is None:
            raise credentials_exception
        return user_email
    except JWTError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "토큰이 유효하지 않습니다.")
