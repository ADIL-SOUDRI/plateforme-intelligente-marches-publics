from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):

    email: EmailStr
    mot_de_passe: str
    role: str


class TokenResponse(BaseModel):

    access_token: str
    token_type: str
    class Config:
        from_attributes = True