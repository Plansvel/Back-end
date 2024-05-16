from fastapi import HTTPException
from schemas import user_schema
from settings import supabase
from settings import security

connection = supabase.create_supabase_client()

def user_exists(key: str = "email", value: str = None):
    user = connection.table("usuario").select("*").eq(key, value).execute()
    return len(user.data) > 0

def create_user(user: user_schema.UserCreate):
    try:
        user_email = user.email.lower()
        
        if user_exists(value=user_email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_senha = security.get_password_hash(user.senha)
        
        user_created = connection.table("usuario").insert({
            "nome":user.nome,
            "email":user.email,
            "cpf":user.cpf, 
            "telefone": user.telefone,
            "senha":hashed_senha
            }).execute()
        
        if user_created:
            user_created_copy = dict(user_created.data[0])
            user_created_copy["funcao"] = create_role(user_created.data[0]["id_usuario"])
            user_response = user_schema.User(**user_created_copy)
            return user_response
        else:
            raise HTTPException(status_code=412, detail="User creation failed")
    
    except HTTPException as http_exception:
        raise http_exception

def create_role(id_user: int):
    try:
        
        connection.table("usuario_funcao").insert({
            "id_usuario": id_user,
            "id_funcao": 1,
        }).execute()
        
        id_role = connection.table("usuario_funcao").select("id_funcao").eq("id_usuario", id_user).execute()
        
        funcao = connection.table("funcao").select("nome_funcao").eq("id_funcao", id_role.data[0]["id_funcao"]).execute()
        
        return funcao.data[0]["nome_funcao"]
        
    except HTTPException as http_exception:
        raise http_exception