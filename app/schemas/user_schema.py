from typing_extensions import Self
from pydantic import BaseModel, Field, EmailStr, model_validator

class UserBase(BaseModel):
    nome: str
    email: EmailStr
    cpf: str = Field(min_length=11, max_length=11)
    telefone: str = Field(min_length=8, max_length=8)
    is_active: bool = True

class UserCreate(UserBase):
    senha: str
    senha2: str
    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        pw1 = self.senha
        pw2 = self.senha2
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return self
    
class User(UserBase):
    id_usuario: int
    funcao: str