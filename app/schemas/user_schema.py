from pydantic import BaseModel

class UserBase(BaseModel):
    nome: str
    email: str
    cpf: str
    telefone: str

class UserCreate(UserBase):
    senha: str
    
class User(UserBase):
    id_usuario: int
    funcao: str
