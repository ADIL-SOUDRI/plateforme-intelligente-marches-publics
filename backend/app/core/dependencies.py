from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.security import decode_access_token
# from app.exceptions.auth_exceptions import InvalidTokenException


from app.exceptions.auth_exceptions import InvalidTokenException,AccessDeniedException
security = HTTPBearer()


# def get_current_user(
#     credentials: HTTPAuthorizationCredentials = Depends(security)
# ):
#     try:
#         token = credentials.credentials

#         payload = decode_access_token(token)

#         if not payload:
#             raise InvalidTokenException()

#         return payload

#     except Exception:
#         raise InvalidTokenException()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    payload = decode_access_token(token)

    if not payload:
        raise InvalidTokenException()

    return payload


def get_current_utilisateur(current_user=Depends(get_current_user)):
    if current_user["role"] != "utilisateur":
        raise AccessDeniedException()

    return current_user
def get_current_admin(current_user=Depends(get_current_user)):
    if current_user["role"] != "administrateur":
        raise AccessDeniedException()

    return current_user