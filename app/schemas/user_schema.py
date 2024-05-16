from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    nome: str
    email: EmailStr
    cpf: str = Field(min_length=11, max_length=11)
    telefone: str = Field(min_length=8, max_length=8)

class UserCreate(UserBase):
    senha: str
    
class User(UserBase):
    id_usuario: int
    funcao: str
